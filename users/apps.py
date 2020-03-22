from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    
    
    def ready(self):
        """This avoids side effects of importing: creates the user profile"""
        import users.signals 