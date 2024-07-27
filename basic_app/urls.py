from django.urls import path 
from . import views
from graphene_django.views import GraphQLView
from basic_app.schema import schema

urlpatterns = [
    path("", views.hello, name="faltu name"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david"),
    path("index", views.index, name="the next"),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema))
 ]