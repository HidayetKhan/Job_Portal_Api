# Generated by Django 4.2.7 on 2023-12-16 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_userexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('field_of_study', models.CharField(max_length=50)),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
                ('grade', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
