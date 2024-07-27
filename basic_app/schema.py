import graphene
from graphene_django import DjangoObjectType
from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model= Book
        fields = ('id','name', 'desc')
        


class Queryp(graphene.ObjectType):
    allbooks = graphene.List(BookType)
   
    def resolve_allbooks(root, info):
         return Book.objects.all()
    
    

schema = graphene.Schema(query=Queryp)
    