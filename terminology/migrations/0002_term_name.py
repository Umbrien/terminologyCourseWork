# Generated by Django 3.1.7 on 2021-04-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminology', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='name',
            field=models.CharField(default=None, max_length=512, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
