from django.contrib import admin
from django.apps import apps
from .models import AddUser
# Register your models here.
admin.site.register(AddUser)

app=apps.get_app_config('graphql_auth')

for model_name,model in app.models.items():
    admin.register(model)