from django.db import models
from users import models as user_model

class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Post(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User,
                null=True,
                on_delete=models.CASCADE,
                related_name = 'post_author'
            )
    image = models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d')
    caption = models.TextField(blank=True)
    image_likes = models.ManyToManyField(user_model.User, related_name='post_image_likes')


class Comment(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User,
                null=True,
                on_delete=models.CASCADE,
                related_name = 'comment_author'
            )
    posts = models.ForeignKey(
                user_model.User,
                null=True,
                on_delete=models.CASCADE,
                related_name = 'comment_post'
            )
    contents = models.TextField(blank=True)
