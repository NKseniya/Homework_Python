import os

BASE_URL = "https://ru.yougile.com/api-v2"

# Токен берётся из окружения. Перед запуском:
#   Windows (PowerShell): $env:YOUGILE_TOKEN = "ваш_ключ"
#   Linux / macOS:        export YOUGILE_TOKEN="ваш_ключ"
TOKEN = os.environ.get("YOUGILE_TOKEN", "")
