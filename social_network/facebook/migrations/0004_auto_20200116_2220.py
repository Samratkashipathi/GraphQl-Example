# Generated by Django 2.2.6 on 2020-01-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_auto_20200116_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='current_location',
        ),
        migrations.AddField(
            model_name='customuser',
            name='friends',
            field=models.ManyToManyField(related_name='_customuser_friends_+', to='facebook.CustomUser'),
        ),
        migrations.RemoveField(
            model_name='photos',
            name='likes',
        ),
        migrations.AddField(
            model_name='photos',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='facebook.CustomUser'),
        ),
        migrations.RemoveField(
            model_name='videos',
            name='likes',
        ),
        migrations.AddField(
            model_name='videos',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='facebook.CustomUser'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]