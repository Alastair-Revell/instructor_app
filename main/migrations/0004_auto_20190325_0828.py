# Generated by Django 2.1.7 on 2019-03-25 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190324_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_category', models.CharField(max_length=200)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Catergories',
            },
        ),
        migrations.CreateModel(
            name='InstructorSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_series', models.CharField(max_length=200)),
                ('series_summaries', models.CharField(max_length=200)),
                ('instructor_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.InstructorCategory', verbose_name='Catergory')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.AlterModelOptions(
            name='instructors',
            options={'verbose_name_plural': 'Instructors'},
        ),
        migrations.AddField(
            model_name='instructors',
            name='instructor_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='instructors',
            name='instructor_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.InstructorSeries', verbose_name='Series'),
        ),
    ]
