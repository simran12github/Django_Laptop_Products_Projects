from django.contrib import admin
from  .models import Person,Product,Profile

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "desc","rating","org_email"]
    list_filter = ["name", "price"]
    search_fields = ("name",)
    ordering = ("rating", "price")


# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Profile)
admin.site.register(Person)