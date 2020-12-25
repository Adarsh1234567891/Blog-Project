from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

#MODEL FOR STORING THE POST PUBLISHED BY DIFFERENT USERS
class Post(models.Model):
    author = models.ForeignKey('auth.User')         #Connects a Author As A Authorized User
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    #Navigates The user to the Post Detail Page After A Blog is Published
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

#MODEL FOR STORING THE COMMENTS ON DIFFERENT BLOGS
class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments')      #Connects Each Comment To A Post
    author = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
