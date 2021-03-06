# Generated by Django 3.0.9 on 2020-11-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0037_auto_20201108_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='insideslider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide', models.ImageField(upload_to='', verbose_name='انتخاب عکس')),
                ('Create_Date', models.DateTimeField(auto_now=True, null=True)),
                ('Update_Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Create_Uid', models.IntegerField(blank=True, default=0, null=True, verbose_name='کاربر ایجاد کننده')),
                ('Update_Uid', models.IntegerField(blank=True, default=0, null=True, verbose_name='کاربر ویرایش کننده')),
            ],
            options={
                'verbose_name': 'اسلایدر ',
                'verbose_name_plural': 'اسلایدر ها',
                'db_table': 'insideslider',
                'permissions': (('can_read_private_section', 'administrator'), ('SubAdmin', 'SubAdmin'), ('user_watcher', 'User')),
            },
        ),
    ]
