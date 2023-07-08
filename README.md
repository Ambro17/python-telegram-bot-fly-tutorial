## Parrotbot

### Instructions
```bash
mkdir parrotbot
cd parrotbot
python3 -m venv .virtualenv
source .virtualenv/bin/activate
python3 -m pip install python-telegram-bot==13.15
pip freeze > requirements.txt
TOKEN=<REPLACE_WITH_YOUR_TOKEN_HERE> python bot.py
```

