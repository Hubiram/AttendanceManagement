# Generated by Django 5.0.3 on 2024-04-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_remove_subject_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(related_name='subjects', to='attendance.student'),
        ),
    ]
