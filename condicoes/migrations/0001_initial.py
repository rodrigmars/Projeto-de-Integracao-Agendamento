# Generated by Django 5.0.4 on 2024-05-23 02:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pacientes", "0020_alter_paciente_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Condicao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "condicao_fisica",
                    models.IntegerField(
                        choices=[
                            (1, "Deambula"),
                            (2, "Não deambula"),
                            (3, "Acamado"),
                            (4, "Cadeirante"),
                            (5, "Traqueostomizado"),
                            (6, "Uso de Oxigênio Contínuo"),
                            (7, "Outros"),
                        ]
                    ),
                ),
                ("descricao_condicao", models.CharField(max_length=60, null=True)),
                ("acompanhante", models.IntegerField(choices=[(1, "Sim"), (2, "Não")])),
                (
                    "cuidado_especial",
                    models.IntegerField(choices=[(1, "Sim"), (2, "Não")]),
                ),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                ("data_alteracao", models.DateTimeField(auto_now=True)),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pacientes.paciente",
                    ),
                ),
            ],
            options={
                "db_table": "condicoes",
                "ordering": ["-data_criacao"],
            },
        ),
    ]