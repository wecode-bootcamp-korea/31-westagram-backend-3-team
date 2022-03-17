import re

from django.core.exceptions import ValidationError
from django.db import models

# models.py에 사용자를 관리할 클래스를 생성합니다.
# 생성된 테이블을 사용해 회원가입과 로그인 기능을 작성하게 됩니다.
# 회원가입을 할 때에는 아래와 같은 사용자의 정보를 입력해야 합니다.

# 이름
# 이메일
# 비밀번호
# 연락처(휴대폰)

def validate_email(email):
    email_expression = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    if not email_expression.match(email):
        raise ValidationError(
            '%(value)s is not an email expression',
            params={'email': email},
        )

def validate_password(password):
    password_expression = re.compile('[a-zA-Z0-9+-_.]')

    if not password_expression.match(password):
        raise ValidationError(
            ('%(value)s is not an password expression'),
            params={'password': password},
        )

class User(models.Model):
    name        = models.CharField(max_length=45, db_column='name')
    email       = models.EmailField(validators=[validate_email], db_column='email')
    password    = models.CharField(validators=[validate_password],max_length=30, db_column='password')
    cell_phone  = models.CharField(max_length=30, db_column='cell_phone')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name