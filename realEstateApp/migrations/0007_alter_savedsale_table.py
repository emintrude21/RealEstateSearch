# Generated by Django 5.0.3 on 2024-04-22 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realEstateApp', '0006_agent_comment_post_savedsale'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='savedsale',
            table='saved_sales',
        ),
    ]
