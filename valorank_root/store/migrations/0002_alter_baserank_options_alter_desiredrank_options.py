# Generated by Django 4.1.3 on 2022-12-01 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baserank',
            options={'verbose_name': 'Ранг, с которого нужен буст', 'verbose_name_plural': 'Ранги, с которых нужен буст'},
        ),
        migrations.AlterModelOptions(
            name='desiredrank',
            options={'verbose_name': 'Ранг, до которого нужен буст', 'verbose_name_plural': 'Ранги, до которых нужен буст'},
        ),
    ]