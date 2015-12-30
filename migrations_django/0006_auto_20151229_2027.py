# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_flickr_gallery', '0005_auto_20151013_1009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories', 'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='flickralbum',
            options={'ordering': ['title'], 'verbose_name_plural': 'albums', 'verbose_name': 'album'},
        ),
        migrations.AlterField(
            model_name='category',
            name='creation_date',
            field=models.DateTimeField(verbose_name='creation date', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='name', max_length=60),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='categories',
            field=models.ManyToManyField(to='django_flickr_gallery.Category', related_name='albums', blank=True, verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='creation_date',
            field=models.DateTimeField(verbose_name='creation date', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='description',
            field=models.TextField(null=True, blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='flickr_album_id',
            field=models.CharField(help_text='Select a flickr album.', verbose_name='flickr album', max_length=100),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='featured'),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='last_sync',
            field=models.DateTimeField(help_text='Date of last sync with flickr.', verbose_name='last sync'),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', help_text='Sites where the album will be published.', verbose_name='sites', related_name='albums'),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='slug',
            field=models.SlugField(help_text="Used to build the album's URL.", unique=True, max_length=130),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='status',
            field=models.IntegerField(choices=[(0, 'Hidden'), (1, 'Published')], verbose_name='status', default=1),
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='title',
            field=models.CharField(verbose_name='title', max_length=130),
        ),
    ]
