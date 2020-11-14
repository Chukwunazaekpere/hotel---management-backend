# Generated by Django 3.1.2 on 2020-11-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0009_occupant_checked_in'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OccupantPaymentDetails',
            new_name='PaymentDetails',
        ),
        migrations.AlterField(
            model_name='occupant',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='occupant',
            name='phone',
            field=models.CharField(error_messages={'unique': 'This phone field must contain only numbers of eleven characters.'}, max_length=11, unique=True),
        ),
    ]