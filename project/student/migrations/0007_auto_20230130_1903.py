# Generated by Django 3.0.5 on 2023-01-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20230130_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_pfp',
            field=models.ImageField(default='Default_pfp.png', upload_to='media'),
        ),
    ]