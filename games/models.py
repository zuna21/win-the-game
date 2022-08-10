from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import Profile

# Create your models here.
class Game(models.Model):
    LOW = 'LOW'
    MEDIUM = 'MED'
    HIGH = 'HIG'
    PREMIUM = 'PRE'
    CATEGORY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (PREMIUM, 'Premium'),
    ]

    PLUS = 'PL'
    NON_PLUS = 'NP'
    SUBSCRIPTION_CHOICES = [
        (PLUS, 'Plus game'),
        (NON_PLUS, 'Not plus game'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, blank=True, null=True)
    subscription = models.CharField(max_length=2, choices=SUBSCRIPTION_CHOICES, blank=True, null=True, default=NON_PLUS)
    is_history = models.BooleanField(blank=True, null=True, default=False)
    image = models.ImageField(blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return '%s' % (self.title)


class Comment(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, blank=True, related_name='comments', null=True, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return '%s - %s' % (self.owner.username, self.game.title)

    class Meta:
        ordering = ['-created']



class Reply(models.Model):
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='replies', blank=True, null=True, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return '%s - %s' % (self.owner.username, self.comment.owner.username)