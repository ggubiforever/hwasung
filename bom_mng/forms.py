from django import forms
from bom_mng.models import bom1


class bom1Forms(forms.ModelForm):
    class Meta:
        model = bom1
        fields = ['jepum_code','seq','level', 'jaje_code','pumname','descript','danwi','soyo','last_update']
        labels = {'jepum_code':'제품코드','seq':'순번', 'level':'레벨','jaje_code':'자재코드','pum_name':'품명','descript':'규격','danwi':'단위','soyo':'단위소요량','last_update':'수정일자'}




