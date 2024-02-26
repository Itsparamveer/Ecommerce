# Generated by Django 5.0.2 on 2024-02-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_options_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('waitingapproval', 'Waitingapproval'), ('active', 'Active'), ('delected', 'Delected')], default='active', max_length=50),
        ),
    ]
