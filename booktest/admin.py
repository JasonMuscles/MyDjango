from django.contrib import admin
from booktest.models import BookInfo
from booktest.models import HeroInfo


# User-defined manage class Model（books）
class BookInfoAdmin(admin.ModelAdmin):
    """manage class model for book """
    list_display = ('id', 'book_title', 'book_pub_data')


# User-defined manage class Model（hero's）
class HeroInfoAdmin(admin.ModelAdmin):
    """manage class model for hero """
    list_display = ('id', 'Hero_name', 'Hero_gender', 'Hero_comment')


# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

