# Generated by Django 4.1 on 2022-08-08 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Filme",
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
                ("titulo", models.CharField(max_length=100)),
                ("thumb", models.ImageField(upload_to="thumb_filmes")),
                ("descricao", models.TextField()),
                (
                    "categoria",
                    models.CharField(
                        choices=[
                            ("ANALISES", "Análises"),
                            ("PROGRAMACAO", "Programação"),
                            ("APRESENTACAO", "Apresentação"),
                            ("OUTROS", "Outros"),
                        ],
                        max_length=15,
                    ),
                ),
                ("visualizacoes", models.IntegerField(default=0)),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
