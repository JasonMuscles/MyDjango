from django.db import models

# Create your models here.


# class for books
class BookInfo(models.Model):
    """Books model"""
    # definition books title name
    book_title = models.CharField(max_length=20)
    # definition books publish data
    book_pub_data = models.DateField()

    def __str__(self):
        # return books name
        return self.book_title


# class for Hero's
class HeroInfo(models.Model):
    """Hero's model"""
    Hero_name = models.CharField(max_length=20)
    # default is man(=False)
    Hero_gender = models.BooleanField(default=False)
    Hero_comment = models.CharField(max_length=128)
#   # configure one-to-many（BookInfo-HeroInfo）on_delete=models.CASCADE,删除关联数据,与之关联也删除
    Hero_book = models.ForeignKey("BookInfo", on_delete=models.CASCADE)

    def __str__(self):
        # return Hero's name
        return self.Hero_name
