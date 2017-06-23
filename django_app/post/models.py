from django.contrib.auth.models import User
from django.db import models


# Post모델
# author(User 모델로 연결)
# photo
# comment
# created_date
# modify_date

class Post(models.Model):
    author = models.ForeignKey(User)

    comment = models.TextField(max_length=100)



        # * http://127.0.0.1:8000/post/로 들어가면 post목록 출력하게 url view templates 설정
        #
        # * post를 삭제하는 post_delete 생성 url은  http://127.0.0.1:8000/post/(숫자)/delete
        #
        # * post를 수정하는 post_modify 생성
        # url은 http://127.0.0.1:8000/post/(숫자)/modify
