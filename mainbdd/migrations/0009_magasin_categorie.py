# Generated by Django 3.2.12 on 2023-02-13 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0008_auto_20230213_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='magasin',
            name='categorie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainbdd.categorie'),
        ),
    ]
