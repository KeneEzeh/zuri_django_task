# Generated by Django 4.1.2 on 2022-10-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_remove_lyric_song_id_remove_song_artiste_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='song_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='artiste_id',
            field=models.IntegerField(default=0),
        ),
    ]