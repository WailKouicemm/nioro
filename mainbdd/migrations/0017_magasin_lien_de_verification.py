# Generated by Django 3.2.12 on 2023-02-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0016_alter_magasin_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='magasin',
            name='lien_de_verification',
            field=models.CharField(default='', max_length=200),
        ),
    ]