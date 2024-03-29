# Generated by Django 3.1.5 on 2021-01-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicineitem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_Name', models.CharField(max_length=50)),
                ('cus_Email', models.CharField(max_length=100)),
                ('cus_Mob', models.IntegerField()),
                ('cus_Gen', models.CharField(max_length=10)),
                ('cus_Adds', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='medicinerec',
            name='medi_Exp',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='medicinerec',
            name='medi_Mfg',
            field=models.DateField(),
        ),
    ]
