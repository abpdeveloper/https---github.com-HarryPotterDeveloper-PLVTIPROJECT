# Generated by Django 3.0.9 on 2020-09-17 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0017_auto_20200917_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='productdetails',
            name='StarRating',
        ),
    ]
