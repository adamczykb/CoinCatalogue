# Generated by Django 3.0.7 on 2020-06-23 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200623_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Katalog',
            fields=[
                ('ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=70, null=True, verbose_name='Nazwa katalogu')),
            ],
        ),
        migrations.AddField(
            model_name='moneta',
            name='cenaz',
            field=models.IntegerField(null=True, verbose_name='Cena zapłacona w zł'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='cena',
            field=models.IntegerField(null=True, verbose_name='Cena katalogowa w €'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='nazwa',
            field=models.CharField(max_length=70, null=True, verbose_name='Nazwa monety'),
        ),
        migrations.AddField(
            model_name='moneta',
            name='katalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Katalog', verbose_name='Do jakiego katalogu należy'),
        ),
    ]