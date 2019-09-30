import os
import sys

from app import app

if 'YANDEX_TRANSLATE_API_KEY' not in os.environ:
    print('You have to provide Yandex Translate Api key, set YANDEX_TRANSLATE_API_KEY and restart')
    sys.exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
