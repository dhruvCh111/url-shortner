# Generated by Django 2.2.7 on 2019-12-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateField(verbose_name='Created')),
                ('deadline', models.DateField(verbose_name='Deadline')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
