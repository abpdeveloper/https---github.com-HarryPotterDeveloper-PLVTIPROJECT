# Generated by Django 3.0.9 on 2020-11-04 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0030_auto_20201105_0451'),
    ]

    operations = [
        migrations.CreateModel(
            name='productscategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100, verbose_name='نام دسته بندی')),
                ('cparentid', models.IntegerField(blank=True, default=0, null=True, verbose_name='نام سطح بالادست')),
                ('cdesc', models.TextField(blank=True, max_length=100, null=True, verbose_name='شرح دسته بندی')),
                ('Create_Date', models.DateTimeField(auto_now=True)),
                ('Update_Date', models.DateTimeField(auto_now_add=True)),
                ('Create_Uid', models.IntegerField(blank=True, default=0, null=True, verbose_name='کاربر ایجاد کننده')),
                ('Update_Uid', models.IntegerField(blank=True, default=0, null=True, verbose_name='کاربر ویرایش کننده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'db_table': 'productcategory',
                'ordering': ['id'],
                'permissions': (('can_read_private_section', 'administrator'), ('SubAdmin', 'SubAdmin'), ('user_watcher', 'User')),
            },
        ),
        migrations.AddField(
            model_name='products',
            name='cname1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cname4', to='WebSite.productscategory', verbose_name='نام دسته بندی1'),
        ),
        migrations.AddField(
            model_name='products',
            name='cname2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cname5', to='WebSite.productscategory', verbose_name='نام دسته بندی2'),
        ),
        migrations.AddField(
            model_name='products',
            name='cname3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cname6', to='WebSite.productscategory', verbose_name='نام دسته بندی3'),
        ),
        migrations.AddField(
            model_name='productsgroups',
            name='cname1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cname1', to='WebSite.productscategory', verbose_name='نام دسته بندی1'),
        ),
        migrations.AddField(
            model_name='productsgroups',
            name='cname2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cname2', to='WebSite.productscategory', verbose_name='نام دسته بندی2'),
        ),
        migrations.AddField(
            model_name='productsgroups',
            name='cname3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cname3', to='WebSite.productscategory', verbose_name='نام دسته بندی3'),
        ),
    ]
