from django.db import models

# Create your models here.

PRIORITY = (('danger','high'),('info','normal'),('success','low'))
class TodoModel(models.Model):
    # 小 - 大サイズの文字列のフィールドです。
    title = models.CharField(max_length=100)
    # 多量のテキストのフィールドです。
    memo=models.TextField()
    # 優先度
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    # 締切日
    duedate = models.DateField()
    # 文字列を返すメソッド
    def __str__(self):
        # 数字を返すとエラーになる
        #return 100
        return self.title