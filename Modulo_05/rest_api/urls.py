from django.urls import include, path, re_path

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import routers

from rest_api import views

# Fazendo isntacia para as rotas
router = routers.DefaultRouter()
# Criando a rota da minha api de produtos, usando 'r' rejects, dever ser tratado como uma string regular.
# Indicar qual url irá usar, no caso é produts, e a view utilizada na sequencia.
router.register(r'products', views.ProductApiViewSet)



#Configurando urlpatterns
urlpatterns = [
    # Na rota abaixo inclui todas as rotas que eu criar usando o router.register nas linhas acima.
    path('',include(router.urls)),
    # Rota para CategoryApiViews
    path('categories/', views.CategoryListOnlyAPIView.as_view()),
    path(r'vendas/(?P<pk>\d+)?', views.OrderAPIView.as_view()),
    path('get_token', obtain_auth_token),
    # username e password
]
