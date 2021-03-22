# Generated by Django 3.1 on 2021-03-04 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='realtors/%Y/%m/%d')),
                ('description', models.TextField()),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]