# Generated by Django 2.2.5 on 2020-10-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_merge_20201013_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
