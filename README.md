## Parrotbot
Tutorial: https://wordpress.com/post/ambrodesigns.wordpress.com/15

### Run
```bash
mkdir parrotbot
cd parrotbot
python3 -m venv .virtualenv
source .virtualenv/bin/activate
python3 -m pip install python-telegram-bot==13.15
pip freeze > requirements.txt
TOKEN=<REPLACE_WITH_YOUR_TOKEN_HERE> python bot.py
```
_The token can be obtained by sending `/newbot` to [@Botfather](https://t.me/BotFather)_

## Deploy
```
fly launch
fly secrets set TOKEN=<REPLACE_WITH_YOUR_TOKEN_HERE>
fly deploy
```
