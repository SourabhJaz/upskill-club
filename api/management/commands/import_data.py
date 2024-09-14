import json
from django.core.management.base import BaseCommand, CommandParser
from api.models import *

class Command(BaseCommand):
    help = 'Imports data from JSON file'
    
    def add_arguments(self, parser: CommandParser):
        parser.add_argument('json_file', type=str, help = 'Path to JSON file')
        
    def handle(self, *args, **options):
        json_file = options['json_file']
        self.stdout.write(self.style.SUCCESS('Ran Command'))