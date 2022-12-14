# Generated by Django 4.1 on 2022-08-31 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Periodo', models.CharField(choices=[('I', 'Inteiro'), ('M', 'Meio Periodo'), ('A', 'all time 24x7')], default='I', max_length=1)),
                ('Cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.cargo')),
                ('Funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.funcionario')),
            ],
        ),
    ]
