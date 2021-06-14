from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.html import format_html
from django.contrib.auth import login as auth_login
from .models import *
from .forms import *
from .resources import *
from tablib import Dataset
from django.http import JsonResponse, request
import json
from django.db.models import Max


from django.contrib import messages


def index(request):
    context = {
        'page_title': 'LOGIN',
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'auth/login.html', context)

    elif request.method == "POST":

        user = None
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login,
                            password=password_login)

        if user is not None:
            auth_login(request, user)
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'username atau password salah')
            return redirect('/')

    return render(request, 'auth/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def pengguna(request):
    data = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('pengguna')

    context = {
        'data': data
    }
    return render(request, 'auth/pengguna.html', context)


@login_required
def ubah_pass(request, id):
    user = User.objects.get(id=id)
    data = {
        'user': user.password
    }
    if request.method == 'POST':
        form = Form_ubah_pass(request.POST or None,
                              initial=data, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('pengguna')


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user.username
        t_kub_awal = kub_awal.objects.count()
        t_kub = kub.objects.count()
        t_kop = koperasi.objects.count()

        context = {
            'user': user,
            'pagetitle': 'Dashboard',
            't_kub_awal': t_kub_awal,
            't_kub': t_kub,
            't_kop': t_kop
        }
        return render(request, 'dashboard.html', context)
    else:
        return render(request, '404.html')

# ini adalah controlller data kelompok awal


def kelompok_awal(request):
    if request.user.is_authenticated:
        data = kub_awal.objects.all
        context = {
            'data': data,
            'pagetitle': 'Kelompok Awal'
        }
        return render(request, 'kub_awal/kub.html', context)
    else:
        return render(request, '404.html')


@login_required
def tambah_ka(request):
    if request.method == 'POST':
        simpan = kelompok_a(request.POST or None)
        if simpan.is_valid():
            simpan.save()
            return redirect('kelompok_awal')


@login_required
def ubah_ka(request, id):
    kelompok = kub_awal.objects.get(id=id)
    data = {
        'nama_kelompok': kelompok.nama_kelompok,
        'alamat': kelompok.alamat
    }
    if request.method == 'POST':
        simpan = kelompok_a(request.POST or None,
                            initial=data, instance=kelompok)
        if simpan.is_valid():
            simpan.save()
            return redirect('kelompok_awal')


@login_required
def hapus_ka(request, id):
    kub_awal.objects.filter(id=id).delete()
    return redirect('kelompok_awal')

# ini adalah controller kelompok


@login_required
def kelompok_u(request):
    data = kub.objects.all()
    context = {
        'data': data,
        'pagetitle': 'Kelompok Usaha Bersama'
    }
    return render(request, 'kub/kub.html', context)


@login_required
def kelompok_u_ubah(request, id):
    kelom = kub.objects.get(id=id)
    data = {
        'nama_kub': kelom.nama_kub,
        'no_registrasi': kelom.no_registrasi,
        'alamat': kelom.alamat,
        'nama_ketua': kelom.nama_ketua,
        'jumlah_anggota': kelom.jumlah_anggota,
        'status': kelom.status
    }
    if request.method == 'POST':
        simpan = kelompok(request.POST or None,
                          initial=data, instance=kelom)
        if simpan.is_valid():
            simpan.save()
            return redirect('kelompok_u')


@login_required
def kelompok_u_tambah(request):
    if request.method == 'POST':
        simpan = kelompok(request.POST or None)
        if simpan.is_valid():
            simpan.save()
            return redirect('kelompok_u')
        else:
            return redirect('kelompok_u')


@login_required
def kelompok_u_hapus(request, id):
    kub.objects.filter(id=id).delete()
    return redirect('kelompok_u')

# manajemen koperasi


@login_required
def koperasi_t(request):
    data = koperasi.objects.all()
    context = {
        'data': data,
        'pagetitle': 'Manajemen koperasi'
    }
    return render(request, 'koperasi/koperasi.html', context)


@login_required
def tambah_kop(request):
    if request.method == 'POST':
        simpan = Formkoperasi(request.POST or None)
        if simpan.is_valid():
            simpan.save()
            return redirect('koperasi_t')


@login_required
def ubah_kop(request, id):
    kelom = koperasi.objects.get(id=id)
    data = {
        'nama_koperasi': kelom.nama_koperasi,
        'alamat': kelom.alamat,
        'no_hp': kelom.no_hp,
        'ketua': kelom.ketua,
        'jumlah_anggota': kelom.jumlah_anggota
    }
    if request.method == 'POST':
        simpan = Formkoperasi(request.POST or None,
                              initial=data, instance=kelom)
        if simpan.is_valid():
            simpan.save()
            return redirect('koperasi_t')


@login_required
def hapus_kop(request, id):
    koperasi.objects.filter(id=id).delete()
    return redirect('koperasi_t')


@login_required
def bantuan_kub_t(request):
    bantu = bantuan_kub.objects.select_related('kub')
    data = kub.objects.all()
    print(bantu)
    id = request.POST.get('id')
    jaring = request.POST.get('jaring')
    fish_finder = request.POST.get('fish_finder')
    kapal = request.POST.get('kapal')
    gn = request.POST.get('gn')
    jaring_insang = request.POST.get('jaring_insang')
    print(id, jaring, fish_finder, kapal, gn, jaring_insang)

    if request.method == 'POST':
        simpan = bantuan_kub(jaring=jaring, fish_finder=fish_finder,
                             kapal=kapal, gn=gn, jaring_insang=jaring_insang, kub_id=id)
        simpan.save()

    context = {
        'bantu': bantu,
        'data': data
    }

    return render(request, 'bantuan/bantuan_kub.html', context)


@login_required
def tambah_bantuan(request, id):
    data = bantuan_kub.objects.filter(kub_id=id)
    Kub = kub.objects.get(id=id)
    nomer = id
    if not data:
        context = {
            'Kub': Kub,
            'data': data
        }
        return render(request, 'bantuan/tambah_bantuan.html', context)
    else:
        context = {
            'Kub': Kub,
            'data': data
        }
        return render(request, 'bantuan/peringatan.html', context)


@login_required
def edit_bantuan(request, id):
    data = bantuan_kub.objects.filter(kub_id=id)
    Kub = kub.objects.get(id=id)
    nomer = id
    if not data:
        context = {
            'Kub': Kub,
            'data': data
        }
        return render(request, 'bantuan/peringatan_edit.html', context)
    else:
        context = {
            'Kub': Kub,
            'data': data
        }
        return render(request, 'bantuan/edit_bantuan.html', context)


@login_required
def proses_edit(request):
    nomer = request.POST.get('id')
    angka = request.POST.get('angka')
    dak = request.POST.get('dak')
    kkp = request.POST.get('kkp')
    apbd = request.POST.get('apbd')
    simpan = bantuan_kub.objects.get(id=nomer)
    simpan.dak = dak
    simpan.kkp = kkp
    simpan.apbd = apbd
    simpan.save()
    return redirect('edit_bantuan', angka)


@login_required
def proses_hapus(request):
    nomer = request.POST.get('nomer')
    angka = request.POST.get('angka')
    bantuan_kub.objects.filter(id=nomer).delete()
    return redirect('edit_bantuan', angka)


@login_required
def tambah_bantu(request):
    nomer = request.POST.get('id')
    if request.method == 'POST':
        data = bantuan_kub.objects.filter(kub_id=nomer)
        Kub = kub.objects.get(id=nomer)
        context = {
            'Kub': Kub,
            'data': data
        }
        return render(request, 'bantuan/tambah_bantuan.html', context)


@login_required
def proses_tambah(request):
    nomer = request.POST.get('id')
    dak = request.POST.get('dak')
    kkp = request.POST.get('kkp')
    apbd = request.POST.get('apbd')
    if request.method == 'POST':
        simpan = bantuan_kub(dak=dak, kkp=kkp, apbd=apbd, kub_id=nomer)
        simpan.save()
        return redirect('bantuan_kub_t')


@login_required
def ubah_bantu_kub(request, id):
    bantuan = bantuan_kub.objects.get(id=id)
    data = {
        'jaring': bantuan.jaring,
        'fish_finder': bantuan.fish_finder,
        'kapal': bantuan.kapal,
        'gn': bantuan.gn,
        'jaring_insang': bantuan.jaring_insang
    }
    if request.method == 'POST':
        return redirect('ubah_bantu_kub')


@login_required
def hapus_bantuan_kub(request, id):
    bantuan_kub.objects.filter(id=id).delete()
    return redirect('bantuan_kub_t')


@login_required
def bantuan_koperasi(request):
    data = koperasi.objects.all()
    bantuan = bantuan_kop.objects.select_related('koperasi')
    id = request.POST.get('id')
    dak = request.POST.get('dak')
    kkp = request.POST.get('kkp')

    if request.method == 'POST':
        simpan = bantuan_kop(dak=dak, kkp=kkp, koperasi_id=id)
        simpan.save()
        return redirect('bantuan_koperasi')
    context = {
        'bantuan': bantuan,
        'data': data
    }
    return render(request, 'bantuankop/bantuan_koperasi.html', context)


@login_required
def proses_tambahkop(request):
    nomer = request.POST.get('id')
    dak = request.POST.get('dak')
    kkp = request.POST.get('kkp')
    apbd = request.POST.get('apbd')
    if request.method == 'POST':
        simpan = bantuan_kop(dak=dak, kkp=kkp, apbd=apbd, koperasi_id=nomer)
        simpan.save()
        return redirect('bantuan_koperasi')


@login_required
def tambah_bantuankop(request, id):
    data = bantuan_kop.objects.filter(koperasi_id=id)
    Kop = koperasi.objects.get(id=id)
    nomer = id
    if not data:
        context = {
            'Kop': Kop,
            'data': data
        }
        return render(request, 'bantuankop/tambah_bantuan.html', context)
    else:
        context = {
            'Kop': Kop,
            'data': data
        }
        return render(request, 'bantuankop/peringatan.html', context)


@login_required
def edit_bantuankop(request, id):
    data = bantuan_kop.objects.filter(koperasi_id=id)
    Kop = koperasi.objects.get(id=id)
    nomer = id
    if not data:
        context = {
            'Kop': Kop,
            'data': data
        }
        return render(request, 'bantuankop/peringatan_edit.html', context)
    else:
        context = {
            'Kop': Kop,
            'data': data
        }
        return render(request, 'bantuankop/edit_bantuan.html', context)


@login_required
def proses_editkop(request):
    nomer = request.POST.get('id')
    angka = request.POST.get('angka')
    dak = request.POST.get('dak')
    kkp = request.POST.get('kkp')
    apbd = request.POST.get('apbd')
    simpan = bantuan_kop.objects.get(id=nomer)
    simpan.dak = dak
    simpan.kkp = kkp
    simpan.apbd = apbd
    simpan.save()
    return redirect('edit_bantuankop', angka)


@login_required
def proses_hapuskop(request):
    nomer = request.POST.get('nomer')
    angka = request.POST.get('angka')
    bantuan_kop.objects.filter(id=nomer).delete()
    return redirect('edit_bantuankop', angka)


@login_required
def tambah_bantukop(request):
    nomer = request.POST.get('id')
    if request.method == 'POST':
        data = bantuan_kop.objects.filter(koperasi_id=nomer)
        Kop = koperasi.objects.get(id=nomer)
        context = {
            'Kop': Kop,
            'data': data
        }
        return render(request, 'bantuankop/tambah_bantuan.html', context)


@login_required
def ubah_bantuan_kop(request, id):
    bantu = bantuan_kop.objects.get(id=id)
    data = {
        'dak': bantu.dak,
        'kkp': bantu.kkp
    }
    if request.method == 'POST':
        form = Form_bantuan_kop(request.POST or None,
                                initial=data, instance=bantu)
        if form.is_valid():
            form.save()
            return redirect('bantuan_koperasi')


@login_required
def hapus_bantuan_kop(request, id):
    bantuan_kop.objects.filter(id=id).delete()
    return redirect('bantuan_koperasi')


@login_required
def c_bantuan_kub(request):
    bantu = bantuan_kub.objects.select_related('kub')
    context = {
        'bantu': bantu
    }
    return render(request, 'laporan/c_bantuan_kub.html', context)


@login_required
def c_bantuan_kubt(request):
    awal = request.GET.get('awal')
    akhir = request.GET.get('akhir')
    bantu = bantuan_kub.objects.all().filter(
        tanggal__range=[awal, akhir])
    context = {
        'bantu': bantu
    }
    return render(request, 'laporan/c_bantuan_kub.html', context)


@login_required
def c_bantuan_kopt(request):
    awal = request.GET.get('awal')
    akhir = request.GET.get('akhir')
    bantu = bantuan_kop.objects.all().filter(
        tanggal__range=[awal, akhir])
    context = {
        'bantu': bantu
    }
    return render(request, 'laporan/c_bantuan_kop.html', context)


@login_required
def c_bantuan_kop(request):
    bantu = bantuan_kop.objects.select_related('koperasi')
    context = {
        'bantu': bantu
    }
    return render(request, 'laporan/c_bantuan_kop.html', context)


@login_required
def c_kuba(request):
    data = kub_awal.objects.all()
    context = {
        'data': data,
        'pagetitle': 'Kelompok Usaha Bersama'
    }
    return render(request, 'laporan/c_kub_awal.html', context)


@login_required
def c_kub(request):
    data = kub.objects.all()
    context = {
        'data': data,
        'pagetitle': 'Kelompok Usaha Bersama'
    }
    return render(request, 'laporan/c_kub.html', context)


@login_required
def c_koperasi(request):
    data = koperasi.objects.all()
    context = {
        'data': data
    }
    return render(request, 'laporan/c_koperasi.html', context)


@login_required
def json(request):
    data = list(kub.objects.values())
    return JsonResponse(data, safe=False)


@login_required
def json_kop(request):
    data = list(koperasi.objects.values())
    return JsonResponse(data, safe=False)


@login_required
def test(request):
    return render(request, 'coba.html')


@login_required
def simple_upload(request):
    if request.method == 'POST':
        kubsum = kubsumber()
        dataset = Dataset()
        data = request.FILES['myfile']

        imported_data = dataset.load(data.read(), format='xlsx')
        # print(imported_data)
        for data in imported_data:
            print(data[1])
            value = kub_awal(
                data[0],
                data[1],
                data[2]
            )
            value.save()

        # result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        # if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return redirect('kelompok_awal')


@login_required
def import_kub(request):
    if request.method == 'POST':
        kubsum = kubaw()
        dataset = Dataset()
        data = request.FILES['myfile']

        imported_data = dataset.load(data.read(), format='xlsx')
        # print(imported_data)
        for data in imported_data:
            print(data[1])
            value = kub(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],

            )
            value.save()

        # result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        # if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return redirect('kelompok_u')


@login_required
def import_kop(request):
    if request.method == 'POST':
        Kopsum = kopsum()
        dataset = Dataset()
        data = request.FILES['myfile']

        imported_data = dataset.load(data.read(), format='xlsx')
        # print(imported_data)
        for data in imported_data:
            print(data[1])
            value = koperasi(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
            )
            value.save()

        # result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        # if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return redirect('koperasi_t')


def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response
