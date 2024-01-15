# Generated by Django 4.2.6 on 2024-01-15 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='image')),
                ('bio', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('ph', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.PositiveIntegerField()),
                ('activity', models.CharField(max_length=200)),
                ('supporter', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post', models.ImageField(null=True, upload_to='post')),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('like', models.ManyToManyField(related_name='likedpost', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='userpost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('like', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
