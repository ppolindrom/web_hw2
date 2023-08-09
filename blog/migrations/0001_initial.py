# Generated by Django 4.2.3 on 2023-08-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('content', models.TextField()),
                ('preview', models.ImageField(upload_to='blog_previews/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
