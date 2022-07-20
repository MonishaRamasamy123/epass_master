# Generated by Django 4.0.5 on 2022-07-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('mode_of_transport', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(null=True)),
                ('no_of_persons', models.IntegerField(null=True)),
                ('from_address', models.CharField(max_length=1000, null=True)),
                ('to_address', models.CharField(max_length=1000, null=True)),
                ('from_city', models.CharField(max_length=20, null=True)),
                ('to_city', models.CharField(max_length=20, null=True)),
                ('from_state', models.CharField(max_length=20, null=True)),
                ('to_state', models.CharField(max_length=20, null=True)),
                ('from_zip', models.IntegerField(null=True)),
                ('to_zip', models.IntegerField(null=True)),
                ('reason', models.CharField(max_length=2000, null=True)),
                ('covid_status', models.CharField(max_length=3, null=True)),
                ('aadhar_img', models.ImageField(null=True, upload_to='images/')),
                ('submitted_date', models.DateTimeField(null=True)),
                ('approved_date', models.DateTimeField(null=True)),
                ('approval_status', models.CharField(max_length=20, null=True)),
                ('reject_reason', models.CharField(default='', max_length=2000, null=True)),
                ('from_count', models.IntegerField(default=0)),
                ('to_count', models.IntegerField(default=0)),
            ],
        ),
    ]