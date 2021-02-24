from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Product, ProductInfoItems, HomePageContent, SliderPhoto


@admin.register(SliderPhoto)
class SliderPhotoAdmin(admin.ModelAdmin):
    list_display = ("name", 'get_image')
    readonly_fields = ['get_image']

    def get_image(self, obj):
        print(obj.image.url)
        return mark_safe(f"<img src={obj.image.url} width=100 height=100>")

    get_image.short_description = "Миниатюра"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "get_image")
    readonly_fields = ("get_image", 'created_at')
    search_fields = ("name", "product_info_1", 'product_info_2', 'product_info_3')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'image', 'slug')
        }),
        ('Столбик информации 1', {
            'fields': ('product_info_1', 'product_info_items_1',)
        }),
        ('Столбик информации 2', {
            'classes': ('collapse', ),
            'fields': ('product_info_2', 'product_info_items_2',)
        }),
        ('Столбик информации 3', {
            'classes': ('collapse', ),
            'fields': ('product_info_3', 'product_info_items_3',)
        }),
        ('SEO настройки', {
            'classes': ('collapse', ),
            'fields': ('title', 'keywords', 'header_description',)
        }),
        ('Миниатюра и дата создания', {
            'classes': ('collapse', ),
            'fields': ('get_image', 'created_at',)
        }),
    )
    prepopulated_fields = {
        "slug": ('name',)
    }

    def get_image(self, obj):
        print(obj.image.url)
        return mark_safe(f"<img src={obj.image.url} width=100 height=100>")

    get_image.short_description = "Миниатюра"


@admin.register(ProductInfoItems)
class ProductInfoItemsAdmin(admin.ModelAdmin):
    list_display = ('name',)


class HomePageContentAdminForm(forms.ModelForm):
    description = forms.CharField(label="Текст под слайдером", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = HomePageContent
        fields = '__all__'


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('header', 'map_latitude', 'map_longitude')
    form = HomePageContentAdminForm
    fieldsets = (
        ('Основная информация', {
            'fields': ('header', 'slider_images', 'description')
        }),
        ('SEO настройки', {
            'classes': ('collapse',),
            'fields': ('title', 'keywords', 'header_description',)
        }),
        ('Карта', {
            'classes': ('collapse',),
            'fields': ('map_latitude', 'map_longitude',)
        }),
    )

