# Generated by Django 3.1.5 on 2021-01-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicineRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medi_Name', models.CharField(max_length=40)),
                ('medi_Mfg', models.DateTimeField()),
                ('medi_Batch', models.CharField(max_length=40)),
                ('medi_Exp', models.DateTimeField()),
                ('medi_Comp', models.CharField(max_length=40)),
                ('medi_Mrp', models.IntegerField()),
            ],
        ),
    ]