from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Creating superuser admin account')
        User.objects.create_superuser(email=os.environ.get('DJANGO_SU_EMAIL'),
                                      username=os.environ.get('DJANGO_SU_NAME'),
                                      password=os.environ.get('DJANGO_SU_PASSWORD'))
