# manaba bot

>[!WARNING]
>**manaba+Rのログインに多要素認証が採用されたため現在は使用できません。** <br>
>**現在、ユーザ登録できません。**

これは**manaba**を利用する学生に向けて作成したプロジェクトです。<br>
立命館大学のポータルサイトmanaba+Rはメールでの通知にしか対応しておらず、使いにくかったので作成しました。<br>
manaba専用のLINEボットを使用することで講義ごとの未提出課題・レポート情報をLINEから確認できます。<br>

### LINEチャット画面
<p>
  <img src="https://github.com/kensabrou/manaba-bot-prod/assets/86251649/c20458ef-1a0d-48c8-a0bf-62589e183653" width=320 height=400>
  <img src="https://github.com/kensabrou/manaba-bot-prod/assets/86251649/26f2c2d0-88b2-4d71-9e3e-b31239b737ed" width=320 height=400>
</p>

### manabaのID, パスワードを登録
<p>
  <img src="https://github.com/kensabrou/manaba-bot-prod/assets/86251649/5df9742c-a827-495b-bda8-550a022d1fc7" width=640 height=250>
</p>

# 友達追加
以下のQRまたはIDから友達追加できます。<br>
![673ndnlk](https://github.com/kensabrou/manaba-bot-prod/assets/86251649/a8de84fb-6505-4d8e-b350-40ec3d42158a)
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
<img src="https://github.com/kensabrou/manaba-bot-prod/assets/86251649/658e6841-62e5-4b5e-a8ff-f5489ac2917f" width=650 height=550>

# 機能一覧
- ユーザー登録（自動ログイン時使用）
- 課題確認
  - 自動ログイン
  - スクレイピング
