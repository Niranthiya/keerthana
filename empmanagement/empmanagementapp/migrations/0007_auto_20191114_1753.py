# Generated by Django 2.0.3 on 2019-11-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empmanagementapp', '0006_auto_20191114_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdetails',
            name='code_no',
            field=models.CharField(max_length=5),
        ),
    ]