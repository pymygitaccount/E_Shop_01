# Generated by Django 3.0 on 2022-03-09 04:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20220307_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quqantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime(2022, 3, 9, 9, 44, 50, 404131))),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Customer')),
            ],
        ),
    ]