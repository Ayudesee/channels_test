# Generated by Django 4.0.6 on 2022-08-02 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tack', '0001_initial'),
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='tack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tack.tack'),
        ),
    ]
