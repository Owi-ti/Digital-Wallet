# Generated by Django 4.0.6 on 2022-08-31 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_remove_transaction_date_and_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30, null=True)),
                ('symbol', models.CharField(max_length=5, null=True)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
