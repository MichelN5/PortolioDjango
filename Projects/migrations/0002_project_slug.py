# Generated by Django 3.2.2 on 2022-10-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.CharField(default='A', max_length=255),
            preserve_default=False,
        ),
    ]