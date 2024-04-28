from tkinter import Widget
from django import forms
from .utils import AGENDAMENTO_FIXO_CHOICES, GENERO_CHOICES
from .models import Paciente
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    RegexValidator,
)


class PacienteForm(forms.ModelForm):

    # nome = forms.CharField(
    #     validators=[
    #         MinLengthValidator(
    #             3, "Limite mínimo de 3 caracteres permitido para campo Nome"
    #         ),
    #         MaxLengthValidator(
    #             30,
    #             message="Limite máximo de 30 caracteres permitido para campo Nome",
    #         ),
    #         RegexValidator(
    #             regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
    #             message="Informe apenas texto para campo Nome",
    #         ),
    #     ],
    #     required=False,
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "olá papai",
    #             "name": "nome",
    #             "id": "nome",
    #             "class": "",
    #         }
    #     ),
    # )

    nome = forms.CharField(
        label="Nome",
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"name": "nome", "id": "nome", "autocomplete": "off"}
        ),
    )

    # data_de_nascimento = forms.DateField(
    #     label="Data de Nascimento",
    #     input_formats=("%m/%d/%Y"),
    #     required=False,
    #     widget=forms.DateInput(
    #         attrs={
    #             "type": "date",
    #             "name": "dataNascimento",
    #             "id": "dataNascimento",
    #             "autocomplete": "off",
    #         }
    #     ),
    # )
    data_de_nascimento = forms.DateField(
        label="Data de Nascimento",
        required=False,
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={
                "type": "date",
                "name": "dataNascimento",
                "id": "dataNascimento",
                "autocomplete": "off",
            },
        ),
    )
    genero = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=GENERO_CHOICES,
    )

    cartao_sus = forms.IntegerField(
        label="Cartão SUS",
        required=False,
        widget=forms.NumberInput(
            attrs={
                "name": "cartaoSUS",
                "id": "cartaoSUS",
                "placeholder": "000000000000000",
                "autocomplete": "off",
            }
        ),
    )

    agendamento_fixo = forms.ChoiceField(
        label="Agendamento Fixo",
        required=False,
        choices=AGENDAMENTO_FIXO_CHOICES,
        widget=forms.RadioSelect(),
        initial=2,
    )

    telefone = forms.CharField(
        label="Telefone",
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "name": "telefone",
                "id": "telefone",
                "placeholder": "+55(00) 00000-0000",
                "autocomplete": "off",
            }
        ),
    )

    rua = forms.CharField(
        label="Rua",
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={"name": "rua", "id": "rua", "autocomplete": "off"}
        ),
    )

    numero = forms.IntegerField(
        label="Número",
        required=False,
        widget=forms.NumberInput(attrs={"name": "numero", "id": "numero"}),
    )

    complemento = forms.CharField(
        label="Complemento",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={"name": "complemento", "id": "complemento", "autocomplete": "off"}
        ),
    )

    ponto_referencia = forms.CharField(
        label="Ponto de Referência",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "name": "pontoReferencia",
                "id": "pontoReferencia",
                "autocomplete": "off",
            }
        ),
    )

    # nome = (
    #     forms.CharField(
    #         validators=[
    #             MinLengthValidator(
    #                 3, "Limite mínimo de 3 caracteres permitido para campo Nome"
    #             ),
    #             MaxLengthValidator(
    #                 30,
    #                 message="Limite máximo de 30 caracteres permitido para campo Nome",
    #             ),
    #             RegexValidator(
    #                 regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
    #                 message="Informe apenas texto para campo Nome",
    #             ),
    #         ],
    #         max_length=30,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "* Nome",
    #                 "class": "form-text-input",
    #                 "name": "nome",
    #                 "id": "nome",
    #             }
    #         ),
    #     ),
    # )

    # sobre_nome = (
    #     forms.CharField(
    #         validators=[
    #             MinLengthValidator(3, "Limite mínimo de 3 caracteres"),
    #             MaxLengthValidator(
    #                 60,
    #                 message="Limite máximo de 30 caracteres",
    #             ),
    #             RegexValidator(
    #                 regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
    #                 message="Formato texto inválido",
    #             ),
    #         ],
    #         max_length=60,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "* Sobre nome",
    #                 "class": "form-text-input",
    #                 "name": "sobreNome",
    #                 "id": "sobreNome",
    #             }
    #         ),
    #     ),
    # )

    # # '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2024-01-15', '01/15/2024', '01/15/24'
    # data_de_nascimento = (
    #     forms.DateField(
    #         required=True,
    #         widget=forms.DateInput(
    #             format="%m/%d/%Y",
    #             attrs={
    #                 "type": "date",
    #                 "placeholder": "* dd/mm/yyyy",
    #                 "class": "form-text-input",
    #                 "name": "dataNascimento",
    #                 "id": "dataNascimento",
    #             },
    #         ),
    #         error_messages={"invalid": "Formato data inválido"},
    #     ),
    # )

    # genero = forms.ChoiceField(choices=GENERO_CHOICES, widget=forms.RadioSelect())

    # cartao_sus = forms.CharField()

    # telefone = (
    #     forms.CharField(
    #         validators=[
    #             RegexValidator(
    #                 regex=r"(\([0-9]{2}\))\s([9]{1})?([0-9]{4})-([0-9]{4})",
    #                 message="Formato inválido",
    #             ),
    #         ],
    #         max_length=15,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "type": "tel",
    #                 "placeholder": "* (99) 9999-9999",
    #                 "class": "form-text-input",
    #                 "name": "telefone",
    #                 "id": "telefone",
    #             }
    #         ),
    #     ),
    # )

    # rua = (
    #     forms.CharField(
    #         validators=[
    #             MinLengthValidator(5, "Limite mínimo de 5 caracteres"),
    #             MaxLengthValidator(
    #                 80,
    #                 message="Limite máximo de 80 caracteres",
    #             ),
    #             RegexValidator(
    #                 regex=r"^([a-zA-Zà-úÀ-Ú0-9]|-|_|.|º|\s)+$",
    #                 message="Formato texto inválido",
    #             ),
    #         ],
    #         max_length=60,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "* Sobre nome",
    #                 "class": "form-text-input",
    #                 "name": "sobreNome",
    #                 "id": "sobreNome",
    #             }
    #         ),
    #     ),
    # )

    # numero = (
    #     forms.IntegerField(
    #         required=True,
    #         widget=forms.NumberInput(
    #             attrs={
    #                 "placeholder": "* Número",
    #                 "class": "form-text-input",
    #                 "name": "sobreNome",
    #                 "id": "sobreNome",
    #             }
    #         ),
    #         error_messages={"invalid": "Campo necessário"},
    #     ),
    # )

    # complemento = (
    #     forms.CharField(
    #         validators=[
    #             MinLengthValidator(5, "Limite mínimo de 5 caracteres"),
    #             MaxLengthValidator(
    #                 60,
    #                 message="Limite máximo de 60 caracteres",
    #             ),
    #             RegexValidator(
    #                 regex=r"[^A-Za-z0-9\\s]+",
    #                 message="Formato texto inválido",
    #             ),
    #         ],
    #         max_length=60,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "Sobre nome",
    #                 "class": "form-text-input",
    #                 "name": "sobreNome",
    #                 "id": "sobreNome",
    #             }
    #         ),
    #     ),
    # )

    # ponto_referencia = (
    #     forms.CharField(
    #         validators=[
    #             RegexValidator(
    #                 regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
    #                 message="Formato texto inválido",
    #             ),
    #         ],
    #         max_length=15,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "",
    #                 "class": "form-text-input",
    #                 "name": "pontoReferencia",
    #                 "id": "pontoReferencia",
    #             }
    #         ),
    #     ),
    # )

    # def clean(self):

    #     super(PacienteForm, self).clean()

    # nome = forms.CharField(
    #     validators=[
    #         # MinLengthValidator(
    #         #     3, "Limite mínimo de 3 caracteres permitido para campo Nome"
    #         # ),
    #         MaxLengthValidator(
    #             30,
    #             message="Limite máximo de 30 caracteres permitido para campo Nome",
    #         ),
    #         RegexValidator(
    #             regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
    #             message="Informe apenas texto para campo Nome",
    #         ),
    #     ],
    #     error_messages={"required": "Campo necessário"},
    # )

    class Meta:

        model = Paciente

        fields = "__all__"
        # fields = [
        #     "nome",
        #     "data_de_nascimento",
        #     "genero",
        #     "cartao_sus",
        #     "agendamento_fixo",
        #     "telefone",
        #     "rua",
        #     "numero",
        #     "complemento",
        #     "ponto_referencia",
        # ]

        exclude = ["status", "data_criacao", "data_alteracao"]

        # fieldsets = [("genero", {"fields": ["name", "Genero"], "legend": "Gênero"})]

        # fields = {
        #     "nome": forms.CharField(
        #         validators=[
        #             MinLengthValidator(
        #                 3, "Limite mínimo de 3 caracteres permitido para campo Nome"
        #             ),
        #             MaxLengthValidator(
        #                 30,
        #                 message="Limite máximo de 30 caracteres permitido para campo Nome",
        #             ),
        #             RegexValidator(
        #                 regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
        #                 message="Informe apenas texto para campo Nome",
        #             ),
        #         ],
        #         max_length=100,
        #         help_text="100 characters max.",
        #     )
        # }

        # widgets = {
        #     "nome": forms.TextInput(
        #         attrs={"id": "nome", "name": "nome", "autocomplete": "off"}
        #     ),
        #     "data_de_nascimento": forms.DateInput(
        #         format=("%m/%d/%Y"),
        #         attrs={
        #             "type": "date",
        #             "id": "dataNascimento",
        #             "name": "dataNascimento",
        #             "autocomplete": "off",
        #         },
        #     ),
        #     "genero": forms.RadioSelect(
        #         attrs={"selected": ""},
        #         choices=[],
        #     ),
        #     "cartao_sus": forms.TextInput(
        #         attrs={"id": "cartaoSUS", "name": "cartaoSUS", "autocomplete": "off"}
        #     ),
        #     "agendamento_fixo": forms.RadioSelect(
        #         attrs={
        #             "id": "agendamento_fixo",
        #             "name": "cartaoSUS",
        #             "autocomplete": "off",
        #         },
        #         choices=[],
        #     ),
        #     "telefone": forms.TextInput(
        #         attrs={"id": "telefone", "name": "telefone", "autocomplete": "off"}
        #     ),
        #     "rua": forms.TextInput(
        #         attrs={"id": "rua", "name": "rua", "autocomplete": "off"}
        #     ),
        #     "numero": forms.NumberInput(
        #         attrs={"id": "numero", "name": "numero", "autocomplete": "off"}
        #     ),
        #     "complemento": forms.TextInput(
        #         attrs={
        #             "id": "complemento",
        #             "name": "complemento",
        #             "autocomplete": "off",
        #         }
        #     ),
        #     "ponto_referencia": forms.TextInput(
        #         attrs={
        #             "id": "pontoReferencia",
        #             "name": "pontoReferencia",
        #             "autocomplete": "off",
        #         }
        #     ),
        # }

    # def clean_nome(self):

    #     nome = self.cleaned_data.get("nome")

    #     if not nome:
    #         raise forms.ValidationError("Campo necessário")

    #     return nome

    def clean(self):

        cleaned_data = super().clean()

        nome = cleaned_data.get("nome")

        if not nome:
            raise forms.ValidationError("Campo necessário")