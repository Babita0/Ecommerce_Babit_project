# Generated by Django 3.1.7 on 2021-02-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField(auto_now_add=True)),
                ('exam_name', models.CharField(max_length=50)),
                ('exam_description', models.TextField(max_length=200)),
                ('total_marks', models.FloatField(max_length=10)),
                ('pass_mark', models.FloatField(max_length=10)),
                ('exam_status', models.BooleanField()),
            ],
        ),
    ]
