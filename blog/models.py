from django.db import models

class Blog(models.Model):

    # id = 1, 2, 3, 4, ...自動保存
    # 文字数
    content = models.CharField(max_length=140)
    # 投稿日時
    posted_date = models.DateTimeField(auto_now_add=True)  