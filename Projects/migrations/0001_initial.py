# Generated by Django 3.2.2 on 2022-10-12 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(max_length=255)),
                ('ProjectPic', models.ImageField(upload_to='')),
            ],
        ),
    ]