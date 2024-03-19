# Generated by Django 3.0.5 on 2020-09-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
                ('facebook', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'صفحات اجتماعی',
            },
        ),
    ]