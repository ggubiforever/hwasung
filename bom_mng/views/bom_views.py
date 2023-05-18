from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import bom1
from ..forms import bom1Forms
from django.core.paginator import Paginator
from django.contrib import messages
from ..forms import ExcelUploadForm
import openpyxl



def add_bom(request):
    jepumcode = request.POST.get('jepum_code','')
    b = bom1.objects.filter(jepum_code=jepumcode)
    if b:
        cond = True
        messages.warning(request, "이미 존재하는 BOM 이어서 입력할 수 없습니다.")
        context =  {"bom1_list":b,'cond':cond,'edtbom':'N'}
        return render(request, 'bom_mng/add_bom.html', context)
    if request.method == 'POST':
        form = bom1Forms(request.POST)
        if form.is_valid():
            bom = form.save(commit=False)
            bom.save()
            print(jepumcode,b)
            cond = True
            context = {"bom1_list":b,'cond':cond,'edtbom':'Y'}
            return render(request, 'bom_mng/add_bom.html', context)
    else:
        form = bom1Forms()
    context = {'form': form,'cond':True,'edtbom':'Y'}
    return render(request, 'bom_mng/add_bom.html', context)


def edit_bom(request,bom1_id):
    bom = get_object_or_404(bom1,pk=bom1_id)
    jepum_code = bom.jepum_code
    if request.method == 'POST':
        form = bom1Forms(request.POST, instance=bom)
        if form.is_valid():
            bom = form.save(commit=False)
            bom.man_edt_modifydate = timezone.now()  # 수정일시 저장
            bom.last_update = bom.man_edt_modifydate.strftime('%Y%m%d')
            bom.save()
            bom = bom1.objects.filter(jepum_code = jepum_code)
            cond = False
            context = {'bom1_list':bom,'cond':cond,'edtbom':'Y'}
            return render(request, 'bom_mng/add_bom.html', context)
    else:
        form = bom1Forms(instance=bom)
        page = request.GET.get('page', '1')  #
        print(1,jepum_code)
        bom = bom1.objects.filter(jepum_code = jepum_code)
        paginator = Paginator(bom, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        cond = False
        context = {'form': form, 'bom1_list':page_obj,'cond':cond,'edtbom':'Y'}
        return render(request, 'bom_mng/add_bom.html', context)


def delete_bomitm(request):
    jepum_code = request.GET.get('jepum','')
    seq = request.GET.get('seqs','')
    b = bom1.objects.filter(jepum_code = jepum_code, seq = seq)
    b.delete()
    form = bom1Forms()
    page = request.GET.get('page', '1')  #
    bom = bom1.objects.filter(jepum_code=jepum_code)
    paginator = Paginator(bom, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'form': form, 'bom1_list': page_obj,'edtbom':'Y'}
    return render(request, 'bom_mng/add_bom.html', context)


def upload_bom(request):
    print("start")
    if "GET" == request.method:
        print(2)
        bom = bom1.objects.filter(seq='1')
        paginator = Paginator(bom, 15)  # 페이지당 15개씩 보여주기
        page_obj = paginator.get_page(1)
        context = {'bom1_list': page_obj, 'page': 1, 'kw': '', 'kw_type': '제품코드'}
        return render(request,'bom_mng/upload_bom.html')
    else:
        print(1)
        excel_file = request.FILES['excel_file']
        wb = openpyxl.load_workbook(excel_file, read_only=True)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)
        bom = bom1.objects.filter(seq='1')
        paginator = Paginator(bom, 15)  # 페이지당 15개씩 보여주기
        page_obj = paginator.get_page(1)
        context = {'bom1_list': page_obj, 'page': 1, 'kw': '', 'kw_type': '제품코드'}
        return render(request, 'bom_mng/bom1_list.html', context)




