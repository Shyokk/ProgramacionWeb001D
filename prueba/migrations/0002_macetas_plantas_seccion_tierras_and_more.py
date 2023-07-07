# Generated by Django 4.2.2 on 2023-06-30 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Macetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Plantas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tierras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.seccion')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='marca',
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.AddField(
            model_name='plantas',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.seccion'),
        ),
        migrations.AddField(
            model_name='macetas',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.seccion'),
        ),
    ]