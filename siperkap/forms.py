from siperkap.models import kub, kub_awal
from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *


class kelompok_a(forms.ModelForm):
    class Meta:
        model = kub_awal
        fields = ['nama_kelompok', 'alamat']


class kelompok(forms.ModelForm):
    class Meta:
        model = kub
        fields = ['nama_kub', 'no_registrasi', 'alamat',
                  'nama_ketua', 'jumlah_anggota', 'status']


class Formkoperasi(forms.ModelForm):
    class Meta:
        model = koperasi
        fields = ['nama_koperasi', 'alamat',
                  'no_hp', 'ketua', 'jumlah_anggota']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_superuser']


class Form_ubah_pass(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password']


class Form_bantuan_kop(forms.ModelForm):
    class Meta:
        model = bantuan_kop
        fields = ['dak', 'kkp']
