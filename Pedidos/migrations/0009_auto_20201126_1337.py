# Generated by Django 2.2 on 2020-11-26 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0008_auto_20201126_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='Pedido',
            new_name='pedido',
        ),
    ]
