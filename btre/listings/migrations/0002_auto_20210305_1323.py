# Generated by Django 3.1 on 2021-03-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
