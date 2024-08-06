from django.urls import path 
from . import views
from graphene_django.views import GraphQLView
from quizz.schema import schema, SSchema
from django.views.decorators.csrf import csrf_exempt
urlpatterns =[
    path('', GraphQLView.as_view(schema=schema, graphiql=True) ),
     path('graphql', csrf_exempt(GraphQLView.as_view(schema=SSchema,graphiql=True)))
]