# Generated by Django 4.1.2 on 2022-11-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_deskstatus_id_alter_deskstatus_desk_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deskstatus',
            name='user_id',
        ),
        migrations.AddField(
            model_name='deskstatus',
            name='user_name',
            field=models.CharField(default='adi', max_length=10),
        ),
        migrations.AlterField(
            model_name='deskstatus',
            name='desk_status',
            field=models.IntegerField(default=0),
        ),
    ]
