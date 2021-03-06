# Generated by Django 3.1.3 on 2021-01-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
