# Generated by Django 2.1.2 on 2018-10-18 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, unique=True)),
                ('enumValues', models.CharField(blank=True, default='', max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('enum', 'enum'), ('text', 'text'), ('date', 'date'), ('number', 'number')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Field_Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risks.Field')),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Risk_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('field', models.ManyToManyField(to='risks.Field')),
            ],
        ),
        migrations.AddField(
            model_name='risk',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risks.Risk_Type'),
        ),
        migrations.AddField(
            model_name='field_risk',
            name='risk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risks.Risk'),
        ),
    ]
