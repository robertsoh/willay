# Generated by Django 2.0.5 on 2018-05-05 04:41

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
                'default_related_name': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Point')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='claims/claim/photo/%Y/%m/%d/', verbose_name='Photo')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='claims.Category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claims', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Claim',
                'verbose_name_plural': 'Claims',
                'ordering': ('-date',),
                'default_related_name': 'claims',
            },
        ),
    ]
