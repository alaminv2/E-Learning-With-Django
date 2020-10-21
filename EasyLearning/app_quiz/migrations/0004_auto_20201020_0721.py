# Generated by Django 2.2.3 on 2020-10-20 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_quiz', '0003_quiz_catagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentanswer',
            name='question',
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_answers', to='app_quiz.Student'),
        ),
    ]