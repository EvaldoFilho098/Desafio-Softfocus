# Generated by Django 4.1 on 2022-08-30 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proagro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tillage',
            name='productor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tillages', to='proagro.productor'),
        ),
    ]
