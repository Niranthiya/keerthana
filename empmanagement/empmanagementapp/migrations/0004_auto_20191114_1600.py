# Generated by Django 2.0.3 on 2019-11-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empmanagementapp', '0003_auto_20191113_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdetails',
            name='code_no',
            field=models.IntegerField(default=False),
        ),
    ]
