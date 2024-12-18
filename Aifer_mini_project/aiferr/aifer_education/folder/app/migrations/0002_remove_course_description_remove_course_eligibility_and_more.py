# Generated by Django 5.1.3 on 2024-11-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.RemoveField(
            model_name='course',
            name='eligibility',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.AddField(
            model_name='course',
            name='required_education',
            field=models.CharField(default='under graduate', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='education',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'),
                                            ('Female', 'Female')],
                                   max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='place',
            field=models.CharField(max_length=100),
        ),
    ]
