# Generated by Django 5.0 on 2024-04-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_auto_20240331_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]