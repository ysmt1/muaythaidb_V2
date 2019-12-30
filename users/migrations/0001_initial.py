# Generated by Django 2.2.5 on 2019-11-09 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mtdb', '0002_auto_20191109_1102'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='TBA')),
                ('location', models.CharField(blank=True, max_length=200)),
                ('experience', models.CharField(blank=True, max_length=200)),
                ('fighter', models.CharField(blank=True, max_length=200)),
                ('checkin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mtdb.Gym')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
