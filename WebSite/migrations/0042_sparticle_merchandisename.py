# Generated by Django 3.0.9 on 2020-11-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0041_auto_20201111_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparticle',
            name='Merchandisename',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام کالا'),
        ),
    ]