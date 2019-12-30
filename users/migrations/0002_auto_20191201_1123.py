# Generated by Django 2.2.5 on 2019-12-01 17:23

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/default.png', upload_to=users.models.profile_img_path),
        ),
    ]
