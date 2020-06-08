from django.apps import AppConfig



class SocialsiteappConfig(AppConfig):
    name = 'SocialSiteApp'
    def ready(self):
        import SocialSiteApp.signals