# Generated by Django 4.2.7 on 2023-11-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='img',
            field=models.ImageField(default='ddddd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
