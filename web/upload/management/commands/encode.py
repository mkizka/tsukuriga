import traceback
from multiprocessing import Process

from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        # ファイルトップでimportするとAppRegistryNotReadyエラーが出る(encode()内のimportが無視される？)
        from upload.models import UploadedPureVideo
        pure_videos = UploadedPureVideo.objects.all().order_by('-created_at')

        for pure in pure_videos:
            # エラーを送出してもメインプロセスは終了しないため、try-exceptはtarget内部で行う
            process = Process(target=encode, args=[pure.id])
            process.start()
            process.join()


def encode(pk):
    import django
    django.setup()
    from upload.models import UploadedPureVideo

    pure = UploadedPureVideo.objects.get(pk=pk)
    if pure.is_encoding:
        return

    try:
        pure.make()
        pure.delete()
    except:
        pure.is_failed = True
        pure.traceback = traceback.format_exc()
        pure.save()

        if not settings.DEBUG:
            send_mail(
                subject='エンコード中のエラー通知',
                message=f'{pure.traceback}\nhttps://tsukuriga.net/admin/upload/uploadedpurevideo/{pure.id}/change/',
                from_email=settings.SERVER_EMAIL,
                recipient_list=[email for name, email in settings.ADMINS]
            )