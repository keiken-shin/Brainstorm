# Generated by Django 2.2.7 on 2020-04-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storm', '0005_idea_idea_creator_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impact', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Improvement_Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Judgeselection',
        ),
    ]
