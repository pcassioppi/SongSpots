# Generated by Django 3.1.6 on 2021-02-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20210208_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
