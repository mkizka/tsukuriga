# Contributionについて
貢献の際は以下を参考にして下さい  
Ownerもよく分かってないのでよく分からない部分があるかもしれませんがご了承ください

## コミットについて
### コミットメッセージ
実験的に[Angular.js](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines)を参考にコミットメッセージをつけています  
完全に従う必要はないですが、見やすいので推奨

### 分割単位
GitHubでファイルの隣に表示されるコミットメッセージを読んで、ファイルとコミットの関係がなんとなく意味が分かるくらいのレベルで

## Issue
質問から提案までどんなものでも歓迎。  
Projectsと合わせてメモ代わりに使うこともあるので適当に参考にすること

## Pull Request
フォーク後、変更内容についてのブランチを切ってから開発を行って下さい  
名前は何でもいいですがprefix/detailの形式だと分かりやすくなるかもしれません。PRは`master`ブランチに向けてください

PRが大きくなりそうな場合は事前にIssueを建てて相談してくれると助かります
* モデルの新規作成が必要
* UIの追加が必要 など

また、**masterは常にデプロイ可能な状態である**ことが望ましいです  
大きいPRは分割するか、一つのPR内で段階的にレビューを仰いでください

## 本番環境への適用
masterブランチからリファクタリングなど緊急性の低いものを除く最新のものが適用されていると思います
