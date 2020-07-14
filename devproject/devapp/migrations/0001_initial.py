# Generated by Django 3.0.8 on 2020-07-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('made_on', models.DateTimeField()),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
