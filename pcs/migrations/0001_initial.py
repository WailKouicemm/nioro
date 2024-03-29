# Generated by Django 3.2.12 on 2023-02-28 22:22

from django.db import migrations, models
import django.db.models.deletion
import pcs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PcName', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('couleur', models.CharField(max_length=50)),
                ('prix', models.FloatField()),
                ('poid', models.FloatField()),
                ('pouce', models.FloatField()),
                ('tactile', models.BooleanField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pcs', to='pcs.model')),
            ],
        ),
        migrations.CreateModel(
            name='Processeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Number', models.CharField(max_length=20)),
                ('vitesse', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gb', models.IntegerField()),
                ('Type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stokage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gb', models.CharField(max_length=20)),
                ('Type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SousModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SousmodelName', models.CharField(max_length=20)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sousModels', to='pcs.model')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='posts/default.jpg', upload_to=pcs.models.upload_to)),
                ('pub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='pcs.pc')),
            ],
        ),
        migrations.AddField(
            model_name='pc',
            name='processeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pcs', to='pcs.processeur'),
        ),
        migrations.AddField(
            model_name='pc',
            name='ram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pcs', to='pcs.stokage'),
        ),
    ]
