# Generated by Django 4.1.2 on 2022-11-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_studentextra_1_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra_1',
            name='profile_picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
