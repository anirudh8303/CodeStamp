# Generated by Django 3.1.3 on 2020-11-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0005_auto_20201123_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('phar_id', models.AutoField(primary_key=True, serialize=False)),
                ('phar_name', models.CharField(default='', max_length=100)),
                ('phar_ownerName', models.CharField(default='', max_length=150)),
                ('phar_idProof', models.ImageField(default='', upload_to='fit/pharmacy')),
                ('phar_StoreImage', models.ImageField(default='', upload_to='fit/pharmacy')),
                ('phar_phone', models.IntegerField()),
                ('phar_address', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
