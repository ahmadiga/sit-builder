import os
from os.path import join
from subprocess import call
from os import rename
from sit_builder.utils import *
from django.conf import settings

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)

    def handle(self, *args, **options):
        for name in options['name']:
            package = os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/')
            CURRENT_PATH = settings.BASE_DIR
            call(["tar", "xvzf", join(package, "app_template.tar.gz"), "-C", CURRENT_PATH])
            rename(join(CURRENT_PATH, "app_template"), join(CURRENT_PATH, name))
            replace_app_template(join(CURRENT_PATH, name), name)
            add_app_to_settings(name, CURRENT_PATH)
            self.stdout.write(self.style.SUCCESS('APP "%s" Created' % name))
