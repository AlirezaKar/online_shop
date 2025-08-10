from django.urls import path

from .views import (api_page_view,
                ProductView,
                ProductDetailView,
                CategoryView,
                CategorydetailView,
                
 )


from rest_framework .urlpatterns import format_suffix_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
        path('', api_page_view, name='api_page_view'), 
        path('product', ProductView.as_view(), name='product_api_view'), 
        path('product/<int:id>', ProductDetailView.as_view(), name='product_detail_api_view'), 
        path('category/', CategoryView.as_view(), name='category_api_view'),
        path('category/<int:id>', CategorydetailView.as_view(), name='category_detail_api_view'),
        


        path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# urlpatterns = format_suffix_patterns(urlpatterns)