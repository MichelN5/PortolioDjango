# Generated by Django 3.2.2 on 2023-01-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0004_rename_projectimages_projectimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='source_code',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='website',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
