# Generated by Django 4.1.5 on 2023-03-10 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangyDjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditems',
            name='item_image',
            field=models.CharField(default='https://www.shutterstock.com/shutterstock/photos/1328667779/display_1500/stock-vector-restaurant-placeholder-line-icon-linear-style-sign-for-mobile-concept-and-web-design-cafe-map-1328667779.jpg', max_length=500),
        ),
    ]
