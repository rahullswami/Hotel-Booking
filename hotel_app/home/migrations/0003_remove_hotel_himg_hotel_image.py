# Generated by Django 5.1.4 on 2024-12-06 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_hotelbooking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='himg',
        ),
        migrations.CreateModel(
            name='Hotel_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='paper')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_images', to='home.hotel')),
            ],
        ),
    ]
