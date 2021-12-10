# Generated by Django 2.2 on 2021-12-10 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0019_barril_ingreso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fechaEntrega',
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='numeroRemito',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
