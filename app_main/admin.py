from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Product, ProductFeature, Category, Comment, User, MultiMedia

admin.site.unregister(Group)

admin.site.register([User,Category,MultiMedia])


admin.sites.AdminSite.site_header = 'Online Shop Manager'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'status', 'text']
    list_display_links = ['text', 'user', 'content']
    list_filter = ['user', 'status']
    list_editable = ['status']
    search_fields = ['text']

class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 1  
    can_delete = True
    fields = ['field_name', 'field_content']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFeatureInline]
    list_display = ['name', 'status', 'user', 'rating', 'category', 'price']
    list_display_links = ['name', 'user']
    list_filter = ['price', 'rating', 'category']
    list_editable = ['status', 'category']
    search_fields = ['name', 'description', 'features']
