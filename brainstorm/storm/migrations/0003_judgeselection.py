# Generated by Django 2.2.6 on 2020-04-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storm', '0002_auto_20200401_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judgeselection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_status', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]