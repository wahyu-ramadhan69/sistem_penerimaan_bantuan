from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('pengguna', views.pengguna, name='pengguna'),
    path('ubah_pass/<int:id>', views.ubah_pass, name='ubah_pass'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('kelompok_awal', views.kelompok_awal, name='kelompok_awal'),
    path('tambah_ka', views.tambah_ka, name='tambah_ka'),
    path('ubah_ka/<int:id>', views.ubah_ka, name='ubah_ka'),
    path('hapus_ka/<int:id>', views.hapus_ka, name='hapus_ka'),

    path('kelompok_u', views.kelompok_u, name='kelompok_u'),
    path('kelompok_u_tambah', views.kelompok_u_tambah, name='kelompok_u_tambah'),
    path('kelompok_u_hapus/<int:id>',
         views.kelompok_u_hapus, name='kelompok_u_hapus'),
    path('kelompok_u_ubah/<int:id>', views.kelompok_u_ubah, name='kelompok_u_ubah'),

    path('koperasi_t', views.koperasi_t, name='koperasi_t'),
    path('tambah_kop', views.tambah_kop, name='tambah_kop'),
    path('hapus_kop/<int:id>', views.hapus_kop, name='hapus_kop'),
    path('ubah_kop/<int:id>', views.ubah_kop, name='ubah_kop'),

    path('bantuan_kub_t', views.bantuan_kub_t, name='bantuan_kub_t'),
    path('hapus_bantuan_kub/<int:id>',
         views.hapus_bantuan_kub, name='hapus_bantuan_kub'),
    path('ubah_bantu_kub/<int:id>',
         views.ubah_bantu_kub, name='ubah_bantu_kub'),

    path('bantuan_koperasi', views.bantuan_koperasi, name='bantuan_koperasi'),
    path('ubah_bantuan_kop/<int:id>',
         views.ubah_bantuan_kop, name='ubah_bantuan_kop'),
    path('hapus_bantuan_kop/<int:id>',
         views.hapus_bantuan_kop, name='hapus_bantuan_kop'),

    path('c_bantuan_kub', views.c_bantuan_kub, name='c_bantuan_kub'),
    path('c_kuba', views.c_kuba, name='c_kuba'),
    path('c_bantuan_kop', views.c_bantuan_kop, name='c_bantuan_kop'),
    path('c_kub', views.c_kub, name='c_kub'),
    path('c_koperasi', views.c_koperasi, name='c_koperasi'),
    path('c_bantuan_kubt', views.c_bantuan_kubt, name='c_bantuan_kubt'),
    path('c_bantuan_kopt', views.c_bantuan_kopt, name='c_bantuan_kopt'),

    path('tambah_bantuan/<int:id>', views.tambah_bantuan, name='tambah_bantuan'),
    path('proses_tambah', views.proses_tambah, name='proses_tambah'),
    path('tambah_bantu', views.tambah_bantu, name='tambah_bantu'),
    path('edit_bantuan/<int:id>', views.edit_bantuan, name='edit_bantuan'),
    path('proses_edit', views.proses_edit, name='proses_edit'),
    path('proses_hapus', views.proses_hapus, name='proses_hapus'),

    path('tambah_bantuankop/<int:id>',
         views.tambah_bantuankop, name='tambah_bantuankop'),
    path('proses_tambahkop', views.proses_tambahkop, name='proses_tambahkop'),
    path('tambah_bantukop', views.tambah_bantukop, name='tambah_bantukop'),
    path('edit_bantuankop/<int:id>', views.edit_bantuankop, name='edit_bantuankop'),
    path('proses_editkop', views.proses_editkop, name='proses_editkop'),
    path('proses_hapuskop', views.proses_hapuskop, name='proses_hapuskop'),

    path('test', views.test, name='test'),
    path('json/', views.json, name='json'),
    path('json_kop/', views.json_kop, name='json_kop'),
    path('simple_upload', views.simple_upload, name='simple_upload'),
    path('import_kub', views.import_kub, name='import_kub'),
    path('import_kop', views.import_kop, name='import_kop'),
]
