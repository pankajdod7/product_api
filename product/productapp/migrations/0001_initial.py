# Generated by Django 3.1.4 on 2020-12-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('productcategory_id', models.AutoField(primary_key=True, serialize=False)),
                ('parentcategory_id', models.IntegerField(default=None)),
                ('productcategory_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=300)),
                ('product_price', models.FloatField()),
                ('category_id', models.TextField(default=None)),
            ],
        ),
    ]