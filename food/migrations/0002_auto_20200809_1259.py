# Generated by Django 2.2 on 2020-08-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
