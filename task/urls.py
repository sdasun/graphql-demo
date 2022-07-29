import os
# improt GraphQLView from ariadne_django
from ariadne_django.views import GraphQLView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from task.apis.graphql import schema


urlpatterns = [
    path(
        "graphql/",
        csrf_exempt(
            GraphQLView.as_view(
                schema=schema
            )
        ),
        name="graphql",
    ),
]
