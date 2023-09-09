from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run bot'

    def handle(self, *args, **kwargs):
        from bot.telegram_bot import run
        run()
