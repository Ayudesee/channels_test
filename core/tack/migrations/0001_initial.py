# Generated by Django 4.0.6 on 2022-08-02 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('name', models.CharField(max_length=16)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.group')),
            ],
        ),
    ]
