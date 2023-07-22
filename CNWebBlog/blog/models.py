from django.db import models

class News(models.Model):
    title = models.TextField()  # Tiêu đề bài báo
    point = models.IntegerField()  # Điểm
    title_href = models.URLField()  # Link dẫn tới bài báo
    time = models.TextField()  # Thời gian

    def __str__(self):
        return self.title
    # class Meta:
    #     db_table = 'news'  # Đảm bảo tên bảng là 'news'