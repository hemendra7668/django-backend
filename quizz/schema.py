import graphene
from .query import Queryy, Query1
from .mutation import *
from graphql_auth.schema import UserQuery, MeQuery


class Mutation(graphene.ObjectType):
    
    addcategory = CategoryMutation.Field()
    updatedcategory = CategoryMutation.Field()
    deletedcategory= CategoryMutation.Field()



schema = graphene.Schema(query=Queryy, mutation= Mutation)

class Mmutation(AuthMutation, graphene.ObjectType):
    pass

SSchema= graphene.Schema(query=Query1,mutation=Mmutation)