from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name="products_index"),
url(r'^products/new$', views.new, name="products_new"),
url(r'^products/create$', views.create, name="products_create"),
url(r'^products/show/(?P<product_id>\d+)$', views.show, name='products_show'),
url(r'^products/edit/(?P<product_id>\d+)$', views.edit, name='products_edit'),
url(r'^products/update/(?P<product_id>\d+)$', views.update, name='products_update'),
url(r'^products/destroy/(?P<product_id>\d+)$', views.destroy, name='products_destroy'),
]
