# Generated by Django 2.2 on 2019-07-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=25)),
                ('phone_number', models.BigIntegerField()),
                ('country_code', models.CharField(max_length=6)),
                ('contact_email', models.EmailField(max_length=254)),
                ('facebook_url', models.URLField()),
                ('twitter_url', models.URLField()),
                ('insta_url', models.URLField()),
                ('linkedin_url', models.URLField()),
            ],
            options={
                'db_table': 'vg_professional_teaml',
            },
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_img',
            field=models.ImageField(upload_to='media'),
        ),
    ]
