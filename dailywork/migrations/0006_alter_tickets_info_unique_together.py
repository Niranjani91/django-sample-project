# Generated by Django 4.1.3 on 2023-02-05 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailywork', '0005_tickets_info'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tickets_info',
            unique_together={('username', 'ticket_title', 'ticket_status')},
        ),
    ]