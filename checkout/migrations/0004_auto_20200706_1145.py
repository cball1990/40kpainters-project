# Generated by Django 3.0.8 on 2020-07-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200702_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('paid', 'Paid'), ('painted', 'Painting Complete'), ('basing', 'Basing Complete'), ('finishing', 'Final Touches'), ('complete', 'Waiting To Be Shipped'), ('shipped', 'Shipped')], default='ordered', max_length=30),
        ),
    ]