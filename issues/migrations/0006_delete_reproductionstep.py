# Generated by Django 5.0.6 on 2024-07-24 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_reproductionstep'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReproductionStep',
        ),
    ]