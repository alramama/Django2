# Generated by Django 4.0.5 on 2022-07-18 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_bid_boq_bids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid_boq',
            name='bids',
        ),
    ]
