# Generated by Django 3.2.12 on 2023-02-16 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0018_alter_magasin_lien_de_verification'),
    ]

    operations = [
        migrations.AddField(
            model_name='magasin',
            name='valid',
            field=models.BooleanField(default=False),
        ),
    ]
