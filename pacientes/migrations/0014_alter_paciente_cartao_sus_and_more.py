# Generated by Django 5.0.4 on 2024-04-28 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pacientes", "0013_alter_paciente_genero"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paciente",
            name="cartao_sus",
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="data_de_nascimento",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="genero",
            field=models.IntegerField(
                choices=[(1, "Feminino"), (2, "Masculino"), (3, "Outros")], null=True
            ),
        ),
    ]
