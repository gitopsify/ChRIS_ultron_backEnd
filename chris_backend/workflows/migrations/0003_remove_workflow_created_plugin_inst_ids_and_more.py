# Generated by Django 4.0 on 2022-10-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0002_alter_workflow_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflow',
            name='created_plugin_inst_ids',
        ),
        migrations.AddField(
            model_name='workflow',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
