import json

class ConfigReader():
    def get_config(self):
        try:
            with open(r'E:\Coding\u4sem\lab7-9\labasevennine\labasevennine\db_settings.json') as f:
                settings = json.load(f)
            db_settings = {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': settings['DATABASE']['NAME'],
                    'USER': settings['DATABASE']['USER'],
                    'PASSWORD': settings['DATABASE']['PASSWORD'],
                    'HOST': settings['DATABASE']['HOST'],
                    'PORT': settings['DATABASE']['PORT'],
                }

            return db_settings
        
        except Exception as e:
            print(f"Error reading configuration file: {e}")
            return None

conf_reader = ConfigReader()
