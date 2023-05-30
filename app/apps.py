from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'app'
    
    def ready(self):
    	import app.signals