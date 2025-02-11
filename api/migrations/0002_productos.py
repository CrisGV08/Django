# Generated by Django 5.1.2 on 2024-11-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_producto', models.URLField(max_length=255)),
                ('producto', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'productos',
            },
        ),
    ]
