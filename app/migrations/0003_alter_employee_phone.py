# Generated by Django 4.1.3 on 2022-11-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_employee_email_alter_employee_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(),
        ),
    ]