# manaba bot
これは**manaba**を利用する学生に向けて作成したプロジェクトです。<br>
manaba専用のLINEボットを使用することで講義ごとの未提出課題・レポート情報をLINEから確認できます。<br>

### LINEチャット画面
<p>
  <img src="https://github.com/kensabrou/manaba-bot-prod/assets/86251649/7aa7e2f5-7fc1-40e0-a169-dcb4e32b03f7" width=320 height=400>
  <img src="https://github.com/kensabrou/manaba-bot-prod/assets/86251649/56316337-c070-4efb-b0cf-633fafcb06d0" width=320 height=400>
</p>

### manabaのID, パスワードを登録
<p>
  <img src="https://github.com/kensabrou/manaba-bot-prod/assets/86251649/d3d7eaa9-cc9c-4a16-a6da-e65d1731e7ac" width=640 height=250>
</p>

# 友達追加
以下のQRまたはIDから友達追加できます。<br>
![673ndnlk](https://github.com/kensabrou/manaba-bot-prod/assets/86251649/b9eef0da-d21f-4557-b5dc-eecda10dc057)
 <br>
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
