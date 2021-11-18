from django.urls import path
from graphene_django.views import GraphQLView

from . import views
from backend.schema import schema

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name='add'),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]

