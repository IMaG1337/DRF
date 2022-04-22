
from attr import field
from graphene import ObjectType, Schema, String, List
from graphene_django import DjangoObjectType
from todo.models import TODO, Project
from users.models import Users


class TODOType(DjangoObjectType):
    

    class Meta:
        model = TODO
        fields = '__all__'


class ProjectType(DjangoObjectType):
    

    class Meta:
        model = Project
        fields = '__all__'


class UsersType(DjangoObjectType):
    

    class Meta:
        model = Users
        fields = '__all__'




class Query(ObjectType):
    
    all_todo = List(TODOType)
    all_project = List(ProjectType)
    all_users = List(UsersType)

    def resolve_all_todo(root, info):
        return TODO.objects.all()

    def resolve_all_project(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return Users.objects.all()
    


schema = Schema(query=Query)