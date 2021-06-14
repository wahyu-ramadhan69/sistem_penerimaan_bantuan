# Generated by Django 2.2.19 on 2021-05-30 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siperkap', '0002_auto_20210530_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kub',
            name='no_regitrasi',
        ),
        migrations.AddField(
            model_name='kub',
            name='no_registrasi',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]