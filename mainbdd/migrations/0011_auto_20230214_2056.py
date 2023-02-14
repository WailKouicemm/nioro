# Generated by Django 3.2.12 on 2023-02-14 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0010_photos_publication_service_servisenondispo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magasin',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainbdd.categorie'),
        ),
        migrations.AlterField(
            model_name='magasin',
            name='parton',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainbdd.utilisateur'),
        ),
    ]
