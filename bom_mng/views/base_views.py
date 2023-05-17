from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import bom1
from ..forms import bom1Forms
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q



def index(request):
    user = request.user
    if user.is_authenticated:
        page = request.GET.get('page', '1')
        kw = request.GET.get('kw', '')  # 검색어
        kw_type = request.GET.get('type','')
        bom = bom1.objects.filter(seq = '1')# 페이지
        if kw:
            if kw_type == 'jepum_code':
                bom = bom1.objects.filter(jepum_code = kw, seq = '1')
            elif kw_type == 'jaje_code':
                bom = bom1.objects.filter(jaje_code = kw)
            elif kw_type == 'pumname':
                bom = bom1.objects.filter(pumname = kw)
        paginator = Paginator(bom, 15)  # 페이지당 15개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'bom1_list': page_obj, 'page':page, 'kw':kw, 'kw_type':kw_type}
        return render(request, 'bom_mng/bom1_list.html', context)
    else:
        return redirect('common:login')


def detail(request, bom1_id):
    bom = get_object_or_404(bom1, pk=bom1_id)
    jepum_code = bom.jepum_code
    bom = bom1.objects.filter(jepum_code = jepum_code)
    context = {'bom': bom}
    return render(request, 'bom_mng/bom1_detail.html', context)


