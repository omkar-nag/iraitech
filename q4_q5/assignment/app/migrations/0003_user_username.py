# Generated by Django 2.2.12 on 2021-12-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211208_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='username', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
