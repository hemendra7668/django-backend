import graphene
from .models import *
from .query import *


class CategoryMutation(graphene.Mutation):
    
    class Arguments:
        # id= graphene.ID()
        name = graphene.String(required=True)

    
    addcategory = graphene.Field(CategoryType)
    @classmethod
    def mutate(cls, root, info, name):
        
        addcategory=Category(name=name)
        Category.save(addcategory)
        return CategoryMutation(addcategory=addcategory)



class CategoryMutation(graphene.Mutation):
    
    class Arguments:
        id= graphene.ID(required = True)
        name = graphene.String(required =True)

    
    updatecategory = graphene.Field(CategoryType)
    @classmethod
    def mutate(cls, root, info, name, id):
        
        updatecategory= Category.objects.get(id=id)
        updatecategory.name= name
        Category.save(updatecategory)
        return CategoryMutation(updatecategory=updatecategory)
    
    
    
class CategoryMutation(graphene.Mutation):
    
    class Arguments:
        id= graphene.ID(required = True)
       

    
    deletecategory = graphene.Field(CategoryType)
    @classmethod
    def mutate(cls, root, info, id):
        
        updatedcategory= Category.objects.get(id=id)
       
        Category.delete(updatedcategory)
        return "deleted"