# Generated by Django 3.2.12 on 2023-02-20 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0027_service_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='mainbdd.categorie'),
        ),
    ]
