from django.contrib.auth.models import Permission, User
from django.db import models
from django.db.models import Model
from django.db.models.aggregates import Max
import datetime


class kub_awal(models.Model):
    nama_kelompok = models.CharField(max_length=200)
    alamat = models.CharField(max_length=200)
    id_kub = models.CharField(max_length=50)


class kub(models.Model):
    nama_kub = models.CharField(max_length=200, null=True, blank=True)
    no_registrasi = models.CharField(max_length=100, null=True, blank=True)
    alamat = models.CharField(max_length=100, null=True, blank=True)
    nama_ketua = models.CharField(max_length=100, null=True, blank=True)
    jumlah_anggota = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)


class koperasi(models.Model):
    nama_koperasi = models.CharField(max_length=100, null=True, blank=True)
    alamat = models.CharField(max_length=200, null=True, blank=True)
    no_hp = models.CharField(max_length=100, null=True, blank=True)
    ketua = models.CharField(max_length=100, null=True, blank=True)
    jumlah_anggota = models.CharField(max_length=50, null=True, blank=True)


def current_year():
    return datetime.date.today().year


class bantuan_kop(models.Model):
    dak = models.CharField(max_length=200, null=True, blank=True)
    kkp = models.CharField(max_length=200, null=True, blank=True)
    apbd = models.CharField(max_length=200, null=True, blank=True)
    tanggal = models.DateField(auto_now_add=True)
    koperasi = models.ForeignKey(koperasi, models.CASCADE, null=True)


class bantuan_kub(models.Model):
    dak = models.CharField(max_length=200, null=True, blank=True)
    kkp = models.CharField(max_length=200, null=True, blank=True)
    apbd = models.CharField(max_length=200, null=True, blank=True)
    tanggal = models.DateField(auto_now_add=True)
    kub = models.ForeignKey(kub, models.CASCADE, null=True)
