import json
from django.core.management.base import BaseCommand, CommandParser
from api.models import Author, Session, Concept, Course, Category

class Command(BaseCommand):
    help = 'Imports data from JSON file into a model'
    
    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--json_file', type=str, help = 'Path to JSON file')
        parser.add_argument('--model_name', type=str, help = 'Model name')
        
    def handle(self, *args, **options):
        json_file = options['json_file']
        model_name = options['model_name']
        if model_name == 'Author':
            selected_model = Author
        elif model_name == 'Session':
            selected_model = Session
        elif model_name == 'Course':
            selected_model = Course
        elif model_name == 'Category':
            selected_model = Category
        elif model_name == 'Concept':
            selected_model = Concept
        else:
            self.stderr.write(self.style.ERROR(f'Unknown model type {model_name}'))
            return
        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data:
                self.stdout.write(self.style.HTTP_INFO(f'Running Command for {model_name} {item}'))
                (object, created) = selected_model.objects.update_or_create(id = item['id'], defaults = item)            
                self.stdout.write(self.style.SUCCESS(f'Command output {object} {created}'))