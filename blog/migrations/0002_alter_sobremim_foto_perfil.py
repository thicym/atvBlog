# Generated by Django 5.1 on 2024-08-28 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobremim',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='myblog/static/img/thicy.jpeg'),
        ),
    ]
