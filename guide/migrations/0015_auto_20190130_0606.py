# Generated by Django 2.1.5 on 2019-01-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0014_remove_userservices_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userservices',
            name='short_description',
            field=models.CharField(help_text='Short description of your service(2 to 3 sentences)', max_length=150),
        ),
    ]