# Generated by Django 4.1.2 on 2022-11-07 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_alter_teacherextra_1_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherextra_1',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='teacherextra_1',
            name='teacher_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]