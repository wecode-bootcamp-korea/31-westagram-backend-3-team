from django.db import models

class User(models.Model) :
    name = models.CharField(max_length=100), 
    email = models.EmailField(unique = True), # 중복되면 안된다는 조건에 맞춰 unique 속성 사용
    password= models.CharField(max_length=300), #추후에 패스워드 값 암호화 고려해서 최대길이 설정하였음.
    phone_number = models.CharField(max_length=11, unique= True) #뷰 에서 정규표현식으로 핸드폰 값 조건 True or Flase 판단 

class Meta :
    db_table = "users"
# Create your models here.
