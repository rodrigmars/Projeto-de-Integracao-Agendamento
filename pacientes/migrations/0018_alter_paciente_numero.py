# Generated by Django 5.0.4 on 2024-04-30 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pacientes", "0017_alter_paciente_agendamento_fixo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paciente",
            name="numero",
            field=models.CharField(max_length=7),
        ),
    ]
