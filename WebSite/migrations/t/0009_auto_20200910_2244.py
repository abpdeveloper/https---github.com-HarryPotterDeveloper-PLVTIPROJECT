# Generated by Django 3.0.9 on 2020-09-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0008_customers_spfactor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetails',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='productdetails',
            name='like',
        ),
        migrations.AddField(
            model_name='productdetails',
            name='StarRating',
            field=models.IntegerField(default=0, verbose_name='امتیاز ستاره ای'),
        ),
    ]
