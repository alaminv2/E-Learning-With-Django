# Generated by Django 2.2.3 on 2020-10-20 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_course', '0003_auto_20201019_0825'),
        ('app_quiz', '0002_answer_is_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_catagory', to='app_course.Catagory'),
        ),
    ]
