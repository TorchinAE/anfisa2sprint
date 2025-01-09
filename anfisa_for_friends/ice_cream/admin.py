from django.contrib import admin

# Register your models here.
from .models import Category, Topping, Wrapper, IceCream
admin.site.empty_value_display= 'Не задано'

class IceCreamInLine(admin.StackedInline):
    model = IceCream
   

class CategoryAdmin(admin.ModelAdmin):
    inlines =(IceCreamInLine,)


class IceCreamAdmin(admin.ModelAdmin):
    list_display=('title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper')
    list_editable=('is_published',
        'is_on_main',
        'category','wrapper')
    search_fields = ('title',)
    list_filter = ('is_published','category')
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper) 

