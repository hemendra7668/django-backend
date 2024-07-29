import graphene
from .query import Queryy
from .mutation import *
from graphql_auth.schema import UserQuery, MeQuery


class Mutation(graphene.ObjectType):
    
    addcategory = CategoryMutation.Field()
    updatedcategory = CategoryMutation.Field()
    deletedcategory= CategoryMutation.Field()



schema = graphene.Schema(query=Queryy, mutation= Mutation)