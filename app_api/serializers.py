from rest_framework.serializers import Serializer, ModelSerializer

from app_main.models import Product, ProductFeature, Category, Comment, User, MultiMedia

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'user', 'category', 'status', 'rating']

class ProductFeatureSerializer(ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['id', 'product', 'feature_name', 'feature_value']
        read_only_fields = ['id']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

