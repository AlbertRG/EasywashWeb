# Generated by Django 3.2.12 on 2023-09-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpages', '0004_alter_inventory_expirated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('type_service', models.CharField(max_length=100)),
                ('plate_code', models.CharField(max_length=7, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]