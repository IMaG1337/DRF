from django.core.management import BaseCommand
from users.models import Users
from todo.models import Project, TODO 

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(username='magomed', password='magomed1996', email='007mail.ru96@mail.ru')
        project_data = {
            'name':'test',
            'link': 'https://github.com/'
        }
        project = Project.objects.create(**project_data)
        project.users.add(user)
        todo = TODO.objects.create(text='test text', active=True,project=project, user_created=user)