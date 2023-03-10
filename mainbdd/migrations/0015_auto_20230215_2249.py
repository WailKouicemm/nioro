# Generated by Django 3.2.12 on 2023-02-15 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0014_remove_magasin_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='vu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='horeur',
            name='jour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horeurs', to='mainbdd.jour'),
        ),
        migrations.AlterField(
            model_name='horeur',
            name='magasin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horeurs', to='mainbdd.magasin'),
        ),
        migrations.AlterField(
            model_name='service',
            name='magasin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='mainbdd.magasin'),
        ),
    ]