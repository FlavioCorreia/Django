# Generated by Django 3.1.4 on 2020-12-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0003_remove_person_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos'),
        ),
    ]
