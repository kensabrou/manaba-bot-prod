# manaba bot
これは**manaba**を利用する学生に向けて作成したプロジェクトです。<br>
manaba専用のLINEボットを使用することで講義ごとの未提出課題・レポート情報をLINEから確認できます。<br>
<LINE画像>

# 友達追加
以下のQRまたはIDから友達追加できます。<br>
<QR画像> <br>
ID: **@673ndnlk**

# 使用技術
- Python 3.9.7
- Django 4.26
- MySQL 8.0.33
- Nginx
- Gunicorn
- AWS
  - VPC
  - EC2
  - S3
  - RDS
  - Route53
- Docker/Docker-compose

# AWS構成図
<AWS構成画像>

# 機能一覧
- ユーザー登録（自動ログイン時使用）
- 課題確認
  - 自動ログイン
  - スクレイピング
