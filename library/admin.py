from django.contrib import admin
from .models import CustomUser, Book, Tracking, Note
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Book)
admin.site.register(Tracking)
admin.site.register(Note)


