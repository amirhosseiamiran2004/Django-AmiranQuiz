# Generated by Django 4.1.3 on 2022-11-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=120)),
                ('number_of_question', models.IntegerField()),
                ('time', models.IntegerField(help_text='duration of the quiz minuts')),
                ('required_sorce_to_pass', models.IntegerField(help_text='requird sourse to pass')),
                ('dificluty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('Hard', 'Hard')], max_length=6)),
            ],
        ),
    ]
