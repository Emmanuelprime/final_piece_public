# Generated by Django 4.1.2 on 2022-11-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_teacherextra_1_teacher_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherextra_1',
            name='teacher_type',
            field=models.CharField(choices=[('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time')], max_length=10),
        ),
    ]