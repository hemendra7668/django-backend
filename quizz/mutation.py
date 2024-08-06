import graphene
from .models import *
from .query import *
from graphql_auth import mutations

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



class CategoryupdateMutation(graphene.Mutation):
    
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
    
    
    
class CategorydeleteMutation(graphene.Mutation):
    
    class Arguments:
        id= graphene.ID(required = True)
       

    
    deletecategory = graphene.Field(CategoryType)
    @classmethod
    def mutate(cls, root, info, id):
        
        updatedcategory= Category.objects.get(id=id)
       
        Category.delete(updatedcategory)
        return "deleted"
    

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify = mutations.VerifyAccount.Field()
    pass_change= mutations.PasswordChange.Field()
    deleteuser= mutations.DeleteAccount.Field()
    passreset = mutations.PasswordReset.Field()
    update= mutations.UpdateAccount.Field()


