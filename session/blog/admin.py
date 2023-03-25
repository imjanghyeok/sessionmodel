from django.contrib import admin
from .models import Blog
# Register your models here.
# web site에서 조작할 수 있도록 admin 계정을 만듦.(슈퍼계정)
# models에 있는 클래스를 다 가져올 수 있게 *로 하는 게 좋음

admin.site.register(Blog)