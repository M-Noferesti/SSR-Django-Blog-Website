# Generated by Django 3.0.5 on 2020-09-16 09:49

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Categories/%Y/%m/%d')),
                ('image_alt', models.CharField(blank=True, max_length=100, null=True)),
                ('post_count', models.IntegerField(default=0)),
                ('subcategories_count', models.IntegerField(default=0)),
                ('timestamp', django_jalali.db.models.jDateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'دسته بندی های اصلی',
            },
        ),
    ]
