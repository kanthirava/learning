# Generated by Django 2.2.6 on 2019-10-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bankdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=30)),
                ('bank_branch', models.CharField(max_length=30)),
                ('bank_branchcode', models.CharField(max_length=30)),
                ('bank_ifsc', models.CharField(max_length=30)),
            ],
        ),
    ]
