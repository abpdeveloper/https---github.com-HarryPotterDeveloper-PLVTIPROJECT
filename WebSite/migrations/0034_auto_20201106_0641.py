# Generated by Django 3.0.9 on 2020-11-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0033_auto_20201106_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='priceoff',
            field=models.BigIntegerField(verbose_name='قیمت محصول پس از تخفیف'),
        ),
    ]