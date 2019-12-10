from django.contrib import admin
from .models import Account, User, Address, Order, Item, ProductCase, ItemsQuantity,\
    Book, Author
   


class AccountAdmin (admin.ModelAdmin):
     list_display = [field.name for field in Account._meta.fields]
     
     class Meta:
         model = Account

class UserAdmin (admin.ModelAdmin):
     list_display = [field.name for field in User._meta.fields]
     
     class Meta:
         model = User
 

class AddressAdmin (admin.ModelAdmin):
     list_display = [field.name for field in Address._meta.fields]
     
     class Meta:
         model = Address       
    
     
class OrderAdmin (admin.ModelAdmin):
     list_display = ('title',)
     search_fields = ['title']
     filter_horisontal = ('similar', 'items',)
     
     class Meta:
         model = Order
         

class ItemAdmin (admin.ModelAdmin):
     list_display = [field.name for field in Item._meta.fields]
     
     class Meta:
         model = Item

class ProductCaseAdmin (admin.ModelAdmin):
     list_display = [field.name for field in ProductCase._meta.fields]
     
     class Meta:
         model = ProductCase
 
class ItemsQuantityAdmin (admin.ModelAdmin):
     list_display = [field.name for field in ItemsQuantity._meta.fields]
     
     class Meta:
         model = ItemsQuantity



from .models import Group, Person 


class MembershipInline(admin.StackedInline):
    model = Group.members.through
    extra = 1
    
class PersonAdmin(admin.ModelAdmin):
    inlines = [ MembershipInline,]

class GroupAdmin(admin.ModelAdmin):
    inlines = [MembershipInline,]
    exclude = ('members',)




admin.site.register(Person)
admin.site.register(Group, GroupAdmin)

        
admin.site.register(Account, AccountAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ProductCase, ProductCaseAdmin)
admin.site.register(ItemsQuantity, ItemsQuantityAdmin)

