from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.constraints import UniqueConstraint


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    publication_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=250)
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'author'],
                             name='unique_constraint')
        ]

    def __str__(self):
        return f'{self.title}'


class Tracking(models.Model):
    READING = 'RG'
    READ = 'RD'
    UNREAD = 'UR'
    STATUS_CHOICES = [
        (READING, 'reading'),
        (READ, 'read'),
        (UNREAD, 'unread'),
    ]
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=UNREAD)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='tracking_users')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='tracking_books')

    def __str__(self):
        return f'{self.status}'


class Note(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='note_users')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='note_books')
    date_created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=250)
    privacy = models.BooleanField(default=True)
    page_number = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.notes}'
