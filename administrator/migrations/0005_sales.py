# Generated by Django 3.1 on 2020-09-08 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrator', '0004_auto_20200906_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField(auto_now_add=True)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Selling Price')),
                ('qty_sold', models.IntegerField(verbose_name='Quantity Sold')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.drug')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]