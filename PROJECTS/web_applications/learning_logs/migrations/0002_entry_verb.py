# Generated by Django 3.2.6 on 2021-08-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='verb',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
