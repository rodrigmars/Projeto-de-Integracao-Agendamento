# Generated by Django 5.0.4 on 2024-04-28 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pacientes", "0009_alter_paciente_data_de_nascimento_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="paciente",
            name="cartao_sus",
        ),
    ]
