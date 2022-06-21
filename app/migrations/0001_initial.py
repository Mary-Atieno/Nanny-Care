# Generated by Django 4.0.5 on 2022-06-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nanny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='default.jpeg', upload_to='profilepic/')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('experience', models.CharField(blank=True, max_length=50)),
                ('rates', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
