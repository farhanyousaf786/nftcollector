# Generated by Django 4.1 on 2022-09-04 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_chain'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='chain',
            field=models.ManyToManyField(to='main_app.chain'),
        ),
    ]
