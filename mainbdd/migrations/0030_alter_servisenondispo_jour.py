# Generated by Django 3.2.12 on 2023-02-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0029_servisenondispo_jour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servisenondispo',
            name='jour',
            field=models.CharField(max_length=50),
        ),
    ]
