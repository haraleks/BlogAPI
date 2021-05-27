import logging

from django.core.management.base import BaseCommand

from users.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.create_user(
                **{
                    'email': 'super@user.do',
                    'password': '12312300',
                    'is_superuser': True,
                    'is_staff': True
                })
            print('Superuser created')
        except Exception as e:
            logger.error(str(e), exc_info=True)