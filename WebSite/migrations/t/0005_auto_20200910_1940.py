# Generated by Django 3.0.9 on 2020-09-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0004_salecontactus_centerimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='whoweare',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='ما که هستیم'),
        ),
    ]
