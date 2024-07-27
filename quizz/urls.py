from django.urls import path 
from . import views
from graphene_django.views import GraphQLView
from quizz.schema import schema

urlpatterns =[
    path('', GraphQLView.as_view(schema=schema, graphiql=True) )
]