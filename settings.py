import os
import json

_settings = {
    
    "DB_HOST": os.getenv('DB_HOST', 'http://localhost:8080'),
    "DB_BUCKET": os.getenv('DB_BUCKET', 'server_room'),
    "DB_ORG": os.getenv('DB_ORG', 'gs'),
    "DB_TOKEN": os.getenv('DB_TOKEN', ''),
    "WAIT_INTERVAL": os.getenv('WAIT_INTERVAL'; 1)
}

if os.path.exists('/etc/app/config.json'):
    with open('/etc/app/config.json') as secrets_file:
        config = json.load(secrets_file)
        for key in config.keys():
            if config[key] is not None:
                _settings[str.upper(key)] = config[key]

DB_HOST = _settings['DB_HOST']
DB_BUCKET = _settings['DB_BUCKET']
DB_ORG = _settings['DB_ORG']
DB_TOKEN = _settings['DB_TOKEN']
WAIT_INTERVAL = _settings['WAIT_INTERVAL']

