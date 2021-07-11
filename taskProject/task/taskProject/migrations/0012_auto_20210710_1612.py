# Generated by Django 3.1.2 on 2021-07-10 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskProject', '0011_tarefa_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='categoria',
            field=models.ForeignKey(choices=[(25, 'Matemáticaa'), (26, 'Literatura'), (29, 'Aula de Música')], on_delete=django.db.models.deletion.CASCADE, to='taskProject.categoria'),
        ),
    ]
