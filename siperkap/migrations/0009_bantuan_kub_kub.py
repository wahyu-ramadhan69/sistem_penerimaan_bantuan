# Generated by Django 3.1.4 on 2021-05-31 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siperkap', '0008_remove_bantuan_kub_id_kub'),
    ]

    operations = [
        migrations.AddField(
            model_name='bantuan_kub',
            name='kub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='siperkap.kub'),
        ),
    ]