# Generated by Django 3.1 on 2024-05-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_alter_hr_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
