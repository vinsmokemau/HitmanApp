# Generated by Django 3.1.5 on 2021-01-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('target', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('Assigned', 'Assigned'), ('Completed', 'Completed'), ('Failed', 'Failed')], default='Assigned', max_length=50)),
            ],
            options={
                'verbose_name': 'Hit',
                'verbose_name_plural': 'Hits',
            },
        ),
    ]