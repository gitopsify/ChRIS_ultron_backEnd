# Generated by Django 2.1.4 on 2019-02-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugininstances', '0006_plugininstance_pipeline_inst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boolparameter',
            name='value',
            field=models.BooleanField(),
        ),
    ]
