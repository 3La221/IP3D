# Generated by Django 5.1 on 2024-09-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_category_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
