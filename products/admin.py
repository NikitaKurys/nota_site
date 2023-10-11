from django.contrib import admin

from products.models import MainCategory, ProductCards, SlaveCategory, SiteContent


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]
    ordering = ["name", ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductCards)
class ProductCardsAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "slave", "price", "gender_name",]
    search_fields = ["name", ]
    ordering = ["name", ]


@admin.register(SlaveCategory)
class SlaveCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "main", ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SiteContent)
class SlaveCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "description", ]
