# Generated by Django 3.1 on 2020-09-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_drug_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
