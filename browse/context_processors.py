from .models import Label


def labels(request):
    return {'labels': Label.objects.all().order_by('number')}
