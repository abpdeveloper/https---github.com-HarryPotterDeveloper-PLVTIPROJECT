# Generated by Django 3.0.9 on 2020-10-10 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0027_auto_20200927_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dgroup_name', models.CharField(max_length=200, verbose_name='نام زیر گروه')),
                ('dgroup_desc', models.TextField(blank=True, max_length=4000, null=True, verbose_name='توضیح زیر گروه')),
                ('Create_Date', models.DateTimeField(auto_now=True)),
                ('Update_Date', models.DateTimeField(auto_now_add=True)),
                ('Create_Uid', models.IntegerField(default=0, verbose_name='کاربر ایجاد کننده')),
                ('Update_Uid', models.IntegerField(default=0, verbose_name='کاربر ویرایش کننده')),
                ('group_paren_id', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.PROTECT, to='WebSite.productsgroups', verbose_name='کد گروه پدر')),
            ],
            options={
                'verbose_name': 'زیر گروه',
                'verbose_name_plural': 'زیر گروه ها',
                'db_table': 'Group_Detail',
                'ordering': ['id'],
                'permissions': (('can_read_private_section', 'administrator'), ('SubAdmin', 'SubAdmin'), ('user_watcher', 'User')),
            },
        ),
    ]
