from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Address(models.Model):
    UF_STATES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    )

    id_addr = models.AutoField(primary_key=True)
    street = models.CharField("Rua", max_length=255)
    st_number = models.IntegerField("Número")
    nbhd = models.CharField("Bairro", max_length=255)
    state = models.CharField("Estado", max_length=2, choices=UF_STATES)
    complement = models.CharField("Complemento", max_length=255)
    cep = models.CharField("CEP", max_length=8)

    def __str__(self):
        return f"{self.street}, {self.st_number}"

class Employee(models.Model):
    matr = models.AutoField("Matrícula", primary_key=True)
    cpf_ee = models.CharField("CPF funcionário", max_length=11, unique=True)
    f_name = models.CharField("Nome", max_length=255)
    l_name = models.CharField("Sobrenome", max_length=255)
    birth_date = models.DateField("Data de nascimento")
    id_addr = models.ForeignKey('Address', null=True, verbose_name="Endereço", on_delete=models.SET_NULL)
    email = models.EmailField("Email")
    phone_number = models.CharField("Telefone", max_length=11)
    position = models.CharField("Cargo", max_length=255)
    salary = models.FloatField("Salário")

    def __str__(self):
        return f"{self.matr} {self.cpf_ee} {self.f_name}"


class Client(models.Model):
    id_cli = models.AutoField(primary_key=True)
    cpf_cli = models.CharField("CPF cliente", max_length=255, unique=True)
    f_name = models.CharField("Nome", max_length=255)
    l_name = models.CharField("Sobrenome", max_length=255)
    birth_date = models.DateField("Data de nascimento")
    id_addr = models.ForeignKey('Address', null=True, on_delete=models.SET_NULL)
    email = models.EmailField("Email")
    phone_number = models.CharField("Telefone", max_length=11, unique=True)
    qty_ser = models.IntegerField("Quantidade de serviços Solicitados")

    def __str__(self):
        return f"{self.id_cli} {self.cpf_ee} {self.f_name}"

class Service(models.Model):
    id_ser = models.AutoField(primary_key=True)
    type = models.CharField("Tipo de serviço", max_length=255)

class Item(models.Model):
    ItemCategory = models.TextChoices('ItemCategory', 'ACESSÓRIOS CALÇADOS ROUPAS CAMA MESA BANHO DIVERSOS')
    ItemColor = models.TextChoices('ItemColor', 'ESCURO CLARO')

    id_item = models.AutoField(primary_key=True)
    category = models.CharField("Categoria", max_length=10, choices=ItemCategory.choices)
    piece = models.CharField("Peça", max_length=255)
    color = models.CharField("Cor", max_length=6, choices=ItemColor.choices)
    qty_piece = models.IntegerField("Quantidade de peças")
    u_value = models.FloatField("Valor unitário")
    obs = models.CharField("Observação", max_length=255)

class Service_Order(models.Model):
    num_so = models.AutoField(primary_key=True)
    id_ser = models.ForeignKey('Service', null=True, on_delete=models.SET_NULL)
    id_cli = models.ForeignKey('Client', null=True, on_delete=models.SET_NULL)
    matr_ee = models.ForeignKey('Employee', null=True, on_delete=models.SET_NULL)
    exe_date = models.DateTimeField()
    total_value = models.FloatField()

    def __str__(self):
        return self.num_so


class Client_Service(models.Model):
    id_ser = models.ForeignKey('Service', on_delete=models.CASCADE)
    id_cli = models.ForeignKey('Client', on_delete=models.CASCADE)

class Service_Item(models.Model):
    id_ser = models.ForeignKey('Service', on_delete=models.CASCADE)
    id_item = models.ForeignKey('Item', on_delete=models.CASCADE)