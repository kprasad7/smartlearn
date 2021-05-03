# Generated by Django 2.2.10 on 2021-05-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('idd', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('student_class', models.CharField(choices=[('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('ten', 'ten')], default='10', max_length=10)),
                ('subject', models.CharField(max_length=10)),
                ('topic', models.CharField(max_length=100)),
                ('subtopic', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='questions_img')),
                ('question', models.CharField(max_length=600)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
                ('answer', models.CharField(choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4')], max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
