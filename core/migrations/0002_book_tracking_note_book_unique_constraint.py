# Generated by Django 4.1.1 on 2022-09-13 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(max_length=250)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('RG', 'reading'), ('RD', 'read'), ('UR', 'unread')], default='UR', max_length=2)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracking_books', to='core.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracking_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(max_length=250)),
                ('privacy', models.BooleanField(default=True)),
                ('page_number', models.IntegerField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_books', to='core.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_constraint'),
        ),
    ]
