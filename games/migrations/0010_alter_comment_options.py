# Generated by Django 4.1 on 2022-08-09 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_alter_reply_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
    ]