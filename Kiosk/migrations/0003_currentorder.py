# Generated by Django 2.2.4 on 2019-08-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kiosk', '0002_food_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item_id', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
