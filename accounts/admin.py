from django.contrib import admin
from .models import CustomUser

# CustomUserを管理サイトで編集できるようにする
admin.site.register(CustomUser)
