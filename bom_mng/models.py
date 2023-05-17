from django.db import models
from django.contrib.auth.models import User

class bom1(models.Model):
    jepum_code = models.CharField(max_length=20)
    seq = models.CharField(max_length=3)
    level = models.CharField(max_length=2)
    jaje_code = models.CharField(max_length=20)
    pumname = models.CharField(max_length=50)
    descript = models.CharField(max_length=50)
    place = models.CharField(max_length=10)
    danwi = models.CharField(max_length=5)
    soyo = models.CharField(max_length=10)
    jodal = models.CharField(max_length=2)
    last_update = models.CharField(max_length=20)
    man_edit_yn = models.CharField(max_length=3, null = True)
    editor = models.ForeignKey(User, on_delete=models.PROTECT, null = True)
    man_edt_modifydate = models.DateTimeField(null = True)



class bom2(models.Model):
    jepum_code = models.CharField(max_length=20)
    jaje_code = models.CharField(max_length=20)
    pumname = models.CharField(max_length=50)
    descript = models.CharField(max_length=50)
    danwi = models.CharField(max_length=5)
    soyo = models.CharField(max_length=10)
    last_update = models.CharField(max_length=20)


class bom_history(models.Model):
    jepum_code = models.CharField(max_length=20)
    seq = models.CharField(max_length=3)
    level = models.CharField(max_length=2)
    jaje_code = models.CharField(max_length=20)
    update_date = models.CharField(max_length=8)
    update_sayu = models.CharField(max_length=50)




