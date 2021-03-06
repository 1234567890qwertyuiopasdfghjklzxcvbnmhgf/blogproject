# Generated by Django 3.1.3 on 2021-01-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('postdate', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('hobby', '趣味'), ('study', '学習'), ('other', 'その他')], max_length=50)),
            ],
        ),
    ]
