# Generated by Django 3.1.2 on 2021-06-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskProject', '0007_auto_20210612_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='concluida',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='data_conclusao',
            field=models.DateField(null=True),
        ),
    ]
