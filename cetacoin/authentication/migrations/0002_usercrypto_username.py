# Generated by Django 3.1.4 on 2020-12-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercrypto',
            name='username',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
