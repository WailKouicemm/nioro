# Generated by Django 3.2.12 on 2023-02-16 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0022_auto_20230216_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horeur',
            name='jour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horeurs', to='mainbdd.jour'),
        ),
    ]