# Generated by Django 3.2.2 on 2022-10-18 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0002_project_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='')),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_image', to='Projects.project')),
            ],
        ),
    ]
