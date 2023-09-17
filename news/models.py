from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Article(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_articles"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='article_likes', blank=True)

    # Sorts the articles based on the field
    # created_on in descending order
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Release(models.Model):
    # Data model for upcoming releases section
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    release_date = models.DateTimeField()
    platform = models.CharField(max_length=80)

    class Meta:
        ordering = ["-release_date"]
   
    def __str__(self):
        return self.name


class Review(models.Model):
    # Data model for review roundup section
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    review_date = models.DateField()
    score = models.IntegerField()
    content = models.TextField()
    reviewer = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='review_likes', blank=True)

    class Meta:
        ordering = ["review_date"]

    def __str__(self):
        return self.title
  
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="comments", null=True, blank=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name="review_comments",
                               null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True, related_name="user_comment")
    name = models.CharField(max_length=80)
    email = models.EmailField(null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
