# Generated by Django 4.0.5 on 2022-06-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_nanny_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nanny',
            name='company',
        ),
        migrations.AddField(
            model_name='nanny',
            name='company',
            field=models.ManyToManyField(default='Some String', to='app.company'),
        ),
    ]
