# Generated by Django 3.2.12 on 2023-02-13 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0006_auto_20230213_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='fav',
            field=models.ManyToManyField(to='mainbdd.Magasin'),
        ),
    ]
