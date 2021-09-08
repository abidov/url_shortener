# Generated by Django 3.1.13 on 2021-09-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(editable=False, verbose_name='Real URL')),
                ('shortened_url_id', models.CharField(editable=False, max_length=8, unique=True, verbose_name='Shortened URL ID')),
                ('count', models.PositiveIntegerField(verbose_name='Click count')),
            ],
        ),
    ]
