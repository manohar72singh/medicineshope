# Generated by Django 3.1.5 on 2021-01-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicineitem', '0002_auto_20210116_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.IntegerField()),
            ],
        ),
    ]
