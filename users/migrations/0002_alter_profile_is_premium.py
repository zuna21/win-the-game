# Generated by Django 4.1 on 2022-08-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_premium',
            field=models.CharField(blank=True, choices=[('NP', 'Not premium user'), ('OP', 'Only premium user'), ('PP', 'Premium plus user')], default='NP', max_length=2, null=True),
        ),
    ]
