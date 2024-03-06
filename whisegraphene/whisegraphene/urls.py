# from django.urls import include, path
# from rest_framework import routers
# from app.views import ProdutoViewSet

# router = routers.DefaultRouter()
# router.register(r'produtos', ProdutoViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

# from django.contrib import admin

# from django.urls import include, path
# from app.views import ProdutoViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'produtos', ProdutoViewSet, basename="produtos")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls))
# ]

# from django.urls import path
# from graphene_django.views import GraphQLView

# urlpatterns = [
#     path('graphql/', GraphQLView.as_view(graphiql=True)),
# ]

from django.urls import path
from django.contrib import admin
from graphene_django.views import GraphQLView
from app.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("admin/", admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]