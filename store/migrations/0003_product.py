# Generated by Django 3.2 on 2022-08-28 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_auto_20220828_1219'),
        ('store', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('images', models.ImageField(upload_to='photos/products')),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
