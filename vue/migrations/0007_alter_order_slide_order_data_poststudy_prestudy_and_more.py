# Generated by Django 5.0.1 on 2024-01-29 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue', '0006_remove_experiment_slug_experiment_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='slide_order',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
                ('slide_number', models.CharField(max_length=200)),
                ('tcp_est', models.CharField(max_length=200)),
                ('confidence_score', models.CharField(max_length=200)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vue.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='PostStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
                ('UEQ_answers', models.CharField(max_length=100)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vue.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='PreStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('experience', models.CharField(max_length=100)),
                ('interest_in_tech', models.CharField(max_length=100)),
                ('adoption_of_new_tech', models.CharField(max_length=100)),
                ('familiarity_with_AI', models.CharField(max_length=100)),
                ('experiment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vue.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
                ('tcp_est', models.CharField(max_length=200)),
                ('confidence_score', models.CharField(max_length=200)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vue.experiment')),
            ],
        ),
    ]
