from decouple import config

BOT_TOKEN=config('BOT_TOKEN')
ADMINS=[int(admin) for admin in config('ADMINS', cast=lambda v: v.split(','))]
