# Generated by Django 4.1 on 2022-09-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_cmsslider_cms_css'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]