# Generated by Django 3.1 on 2020-09-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_drug'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8, verbose_name='Unit Price'),
            preserve_default=False,
        ),
    ]