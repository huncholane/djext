from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Create a new secret key for the .env file.'

    def handle(self, *args, **options):
        # Generate a django secret key
        # https://stackoverflow.com/questions/4664720/how-to-generate-a-random-secret-key-in-django 
        from django.core.management.utils import get_random_secret_key
        new_secret_key = get_random_secret_key()
        # Update the .env file
        from backend.settings import BASE_DIR
        env_file = BASE_DIR / '.env'
        with open(env_file, 'w') as f:
            f.write(f'SECRET_KEY="{new_secret_key}"')
        self.stdout.write(self.style.SUCCESS('Succesfully updated new key into .env file.'))