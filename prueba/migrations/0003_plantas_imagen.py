# Generated by Django 4.2.2 on 2023-07-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_macetas_plantas_seccion_tierras_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantas',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]