# Generated by Django 3.0.9 on 2020-11-10 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0038_insideslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparticle',
            name='ATotal',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='جمع کل'),
        ),
    ]
