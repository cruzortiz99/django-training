from django.db import models

from domain.db.models.Post import Post
from domain.db.models.User import User


class PostComment(models.Model):
    class Meta:
        db_table = "\"post_comment\""
    post = models.ForeignKey(to=Post, on_delete=models.deletion.CASCADE,
                             null=False)
    createBy = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                 null=False)
    comment = models.TextField(max_length=500, null=False, blank=False)
