# Generated by Django 4.0.3 on 2022-04-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodgroup',
            name='blood_group',
            field=models.CharField(max_length=100),
        ),
    ]