# Generated by Django 3.0.2 on 2020-01-26 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='tags',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Tags'),
            preserve_default=False,
        ),
    ]
