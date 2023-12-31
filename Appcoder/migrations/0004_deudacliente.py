# Generated by Django 4.2.5 on 2023-09-17 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0003_socio'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeudaCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_vencimiento', models.DateField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagada', 'Pagada')], max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appcoder.cliente')),
            ],
        ),
    ]
