# Generated by Django 5.1 on 2024-08-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_description_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='isFeatured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='isVideo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/images/'),
        ),
    ]
