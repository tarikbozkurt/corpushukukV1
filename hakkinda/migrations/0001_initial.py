# Generated by Django 4.0.4 on 2022-05-10 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hakkinda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hakkinda_title', models.CharField(blank=True, max_length=50)),
                ('hakkinda_text', models.TextField(blank=True)),
                ('hakkinda_created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]