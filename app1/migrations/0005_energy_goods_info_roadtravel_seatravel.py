# Generated by Django 4.1.4 on 2023-06-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_airtravel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('attributes', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('attributes', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('attributes', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roadtravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('attributes', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seatravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('attributes', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
    ]
