# Generated by Django 2.2.5 on 2020-01-04 19:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monteseupc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacaMae',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=50, verbose_name='Produto')),
                ('processadores_suportados', models.CharField(choices=[('INTEL', 'Intel'), ('AMD', 'Amd'), ('ambos', 'Intel e AMD')], max_length=50, verbose_name='Processador Suportados')),
                ('slots', models.IntegerField(choices=[('2', '2'), ('4', '4')], verbose_name='Quantidade de Slots')),
                ('memoria_suportada', models.CharField(choices=[('4GB', '4GB'), ('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB')], max_length=10, verbose_name='Memoria suportada')),
                ('video_integrado', models.BooleanField(default=True, verbose_name='Video integrado')),
            ],
        ),
        migrations.AddField(
            model_name='monteseupc',
            name='memoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='monteseupc.Memoria', verbose_name='Memoria Ram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monteseupc',
            name='placa_de_video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monteseupc.PlacaDeVideo', verbose_name='Placa de Video'),
        ),
        migrations.AddField(
            model_name='monteseupc',
            name='qtd_de_memoria',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Quantidade de Memoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monteseupc',
            name='tamanho_da_memoria',
            field=models.CharField(choices=[('4GB', '4GB'), ('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB')], default=1, max_length=50, verbose_name='Tamanho da Memoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monteseupc',
            name='placa_mae',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='monteseupc.PlacaMae', verbose_name='Placa mae'),
            preserve_default=False,
        ),
    ]
