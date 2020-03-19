from django.contrib import admin
from menu_order_app.models import Menu,Order,Order_Item,register
# Register your models here.

# admin.site.register(Member)
# admin.site.register(Menu)
# admin.site.register(Order)
# admin.site.register(Order_Item)

class menuAdmin(admin.ModelAdmin):
    list_display = ['dish_name','price','photo','categories']
    list_filter = ['price']
    search_fields = ['dish_name','categories']
    fieldsets = (
        (None,{
            'fields':(
                'categories',
                'photo',
                'dish_name',
                'price'
            )
        }),
    )

admin.site.register(Menu,menuAdmin)


class orderAdmin(admin.ModelAdmin):
    list_display = ['name','mobile_no','date']
    fieldsets = (
        (None,{
            'fields':(
                'name',
                'mobile_no',
            )
        }),

    )

admin.site.register(Order,orderAdmin)
admin.site.register(register)

class order_itemAdmin(admin.ModelAdmin):
    list_display = ['id','menu_id','order_id']

admin.site.register(Order_Item,order_itemAdmin)