# Generated by Django 3.0.9 on 2020-09-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0024_auto_20200927_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spfactor',
            name='Discount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='spfactor',
            name='Expense',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='spfactor',
            name='Total',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='نام'),
        ),
    ]