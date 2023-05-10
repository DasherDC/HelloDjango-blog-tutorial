# Generated by Django 2.2.3 on 2022-08-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220817_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
