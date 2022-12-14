# Generated by Django 4.1 on 2022-08-24 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_fiscal', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('valor_compra', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'COMPRAS',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Forncedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'FORNECEDOR',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'MATERIAL',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='PREÇO')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='QUANTIDADE')),
                ('subtotal', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orcamento.compra')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orcamento.material')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'PRODUTOS',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orcamento.forncedor'),
        ),
    ]
