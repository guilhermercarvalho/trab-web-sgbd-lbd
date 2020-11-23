# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

# class Address(models.Model):
#     UF_STATES = (
#         ('AC', 'Acre'),
#         ('AL', 'Alagoas'),
#         ('AP', 'Amapá'),
#         ('AM', 'Amazonas'),
#         ('BA', 'Bahia'),
#         ('CE', 'Ceará'),
#         ('DF', 'Distrito Federal'),
#         ('ES', 'Espírito Santo'),
#         ('GO', 'Goiás'),
#         ('MA', 'Maranhão'),
#         ('MT', 'Mato Grosso'),
#         ('MS', 'Mato Grosso do Sul'),
#         ('MG', 'Minas Gerais'),
#         ('PA', 'Pará'),
#         ('PB', 'Paraíba'),
#         ('PR', 'Paraná'),
#         ('PE', 'Pernambuco'),
#         ('PI', 'Piauí'),
#         ('RJ', 'Rio de Janeiro'),
#         ('RN', 'Rio Grande do Norte'),
#         ('RS', 'Rio Grande do Sul'),
#         ('RO', 'Rondônia'),
#         ('RR', 'Roraima'),
#         ('SC', 'Santa Catarina'),
#         ('SP', 'São Paulo'),
#         ('SE', 'Sergipe'),
#         ('TO', 'Tocantins')
#     )

#     id_addr = models.AutoField(primary_key=True)
#     street = models.CharField("Rua", max_length=255)
#     st_number = models.IntegerField("Número")
#     nbhd = models.CharField("Bairro", max_length=255)
#     state = models.CharField("Estado", max_length=2, choices=UF_STATES)
#     complement = models.CharField("Complemento", max_length=255, blank=True)
#     cep = models.CharField("CEP", max_length=8)

#     def __str__(self):
#         return f"{self.street}, {self.st_number}"


class Employee(models.Model):
    matr = models.AutoField("Matrícula", primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cpf_ee = models.CharField("CPF funcionário", max_length=11, unique=True)
    f_name = models.CharField("Nome", max_length=255)
    l_name = models.CharField("Sobrenome", max_length=255)
    birth_date = models.DateField("Data de nascimento")
    address = models.CharField("Endereço", max_length=255)
    email = models.EmailField("Email")
    phone_number = models.CharField("Telefone", max_length=11)
    position = models.CharField("Cargo", max_length=255)
    salary = models.FloatField("Salário")

    def __str__(self):
        return f"{self.matr} {self.cpf_ee} {self.f_name}"

    def get_absolute_url(self):
        return reverse('work:employee_edit', kwargs={'matr': self.matr})

class Client(models.Model):
    id_cli = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cpf_cli = models.CharField("CPF cliente", max_length=11, unique=True)
    f_name = models.CharField("Nome", max_length=255)
    l_name = models.CharField("Sobrenome", max_length=255)
    birth_date = models.DateField("Data de nascimento")
    address = models.CharField("Endereço", max_length=255)
    email = models.EmailField("Email")
    phone_number = models.CharField("Telefone", max_length=11, unique=True)
    qty_ser = models.IntegerField("Quantidade de serviços Solicitados", default=0)

    def __str__(self):
        return f"{self.id_cli} {self.cpf_cli} {self.f_name}"

class Service(models.Model):
    id_ser = models.AutoField(primary_key=True)
    type = models.CharField("Tipo de serviço", max_length=255)

    def __str__(self):
        return f"{self.id_ser} {self.type}"

class Item(models.Model):
    ItemCategory = models.TextChoices('ItemCategory', 'ACESSÓRIOS CALÇADOS ROUPAS CAMA MESA BANHO DIVERSOS')
    ItemColor = models.TextChoices('ItemColor', 'ESCURO CLARO')

    id_item = models.AutoField(primary_key=True)
    category = models.CharField("Categoria", max_length=10, choices=ItemCategory.choices)
    piece = models.CharField("Peça", max_length=255)
    color = models.CharField("Cor", max_length=6, choices=ItemColor.choices)
    qty_piece = models.IntegerField("Quantidade de peças")
    u_value = models.FloatField("Valor unitário")
    obs = models.CharField("Observação", max_length=255, blank=True)

    def __str__(self):
        return f"{self.id_item} {self.category} {self.piece}"

class Service_Order(models.Model):
    num_so = models.AutoField(primary_key=True)
    id_ser = models.ForeignKey('Service', null=True, on_delete=models.SET_NULL, verbose_name="ID Serviço")
    id_cli = models.ForeignKey('Client', null=True, on_delete=models.SET_NULL, verbose_name="ID Cliente")
    matr_ee = models.ForeignKey('Employee', null=True, on_delete=models.SET_NULL, verbose_name="Matrícula Funcionário")
    exe_date = models.DateTimeField("Data de Execução", default=timezone.now)
    total_value = models.FloatField("Valor Total")

    def __str__(self):
        return f"{self.num_so}, {self.id_ser.__str__()}, {self.id_cli.__str__()}, {self.matr_ee.__str__()}"


class Client_Service(models.Model):
    id_ser = models.ForeignKey('Service', on_delete=models.CASCADE)
    id_cli = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.id_ser.__str__()}, {self.id_cli.__str__()}"


class Service_Item(models.Model):
    id_ser = models.ForeignKey('Service', on_delete=models.CASCADE)
    id_item = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.id_ser.__str__()}, {self.id_item.__str__()}"