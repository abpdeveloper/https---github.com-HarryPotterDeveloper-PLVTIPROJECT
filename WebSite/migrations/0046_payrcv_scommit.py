# Generated by Django 3.0.9 on 2020-12-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0045_check_payrcv_payrcvcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='payrcv',
            name='SCommit',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام مشتری'),
        ),
    ]