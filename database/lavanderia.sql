CREATE SCHEMA IF NOT EXISTS lavanderia;

SET search_path TO lavanderia;

CREATE TABLE IF NOT EXISTS pessoa(
    cpf VARCHAR(11) NOT NULL,
    nome VARCHAR(255),
    sobrenome VARCHAR(255),
    data_nasc DATE,
    id_endereco INTEGER NOT NULL,
    telefone VARCHAR(11),
    email VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS endereco(
    id_endereco INTEGER NOT NULL,
    rua VARCHAR(255),
    numero INTEGER,
    bairro VARCHAR(255),
    estado VARCHAR(2),
    complemento VARCHAR(255),
    cep VARCHAR(8)
);

CREATE TABLE IF NOT EXISTS funcionario(
    matr INTEGER NOT NULL,
    cpf_funcionario VARCHAR(11) NOT NULL,
    cargo VARCHAR(255),
    salario REAL
);

CREATE TABLE IF NOT EXISTS cliente(
    id_cliente INTEGER NOT NULL,
    cpf_cliente VARCHAR(255) NOT NULL,
    qnt_servico INTEGER
);

CREATE TABLE IF NOT EXISTS cliente_servico(
    id_servico INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS ordem_servico(
    num_os INTEGER NOT NULL,
    id_servico INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    matr_funcionario INTEGER NOT NULL,
    data_servico TIMESTAMP,
    valor_total REAL   
);

CREATE TABLE IF NOT EXISTS servico(
    id_servico INTEGER NOT NULL,
    tipo VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS servico_item(
    id_servico INTEGER NOT NULL,
    id_item INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS item(
    id_item INTEGER NOT NULL,
    categoria VARCHAR(255),
    peca VARCHAR(255),
    cor VARCHAR(6),
    quantidade INTEGER,
    valor_uni REAL,
    observacoes VARCHAR(255),
    CONSTRAINT tom_cor CHECK (cor IN ('escuro', 'claro'))
);

-- Constrains de endereco
ALTER TABLE endereco ADD
	CONSTRAINT pk_endereco PRIMARY KEY (id_endereco);

-- Constrains de pessoa
ALTER TABLE pessoa ADD
    CONSTRAINT pk_pessoa PRIMARY KEY (cpf);

ALTER TABLE pessoa ADD
    CONSTRAINT fk_endereco_pessoa FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco);

ALTER TABLE pessoa ADD
    CONSTRAINT uniq_telefone UNIQUE (telefone);

ALTER TABLE pessoa ADD
    CONSTRAINT uniq_email UNIQUE (email);

-- Constrains de funcionario
ALTER TABLE funcionario ADD
    CONSTRAINT pk_funcionario PRIMARY KEY (matr);

ALTER TABLE funcionario ADD
    CONSTRAINT fk_funcionario_cpf FOREIGN KEY (cpf_funcionario) REFERENCES pessoa(cpf);

-- Constrains de cliente
ALTER TABLE cliente ADD
    CONSTRAINT pk_cliente PRIMARY KEY (id_cliente);

ALTER TABLE cliente ADD
    CONSTRAINT fk_cliente_cpf FOREIGN KEY (cpf_cliente) REFERENCES pessoa(cpf);

-- Constrains de servico
ALTER TABLE servico ADD
    CONSTRAINT pk_servico PRIMARY KEY (id_servico);

-- Constrains de cliente_servico
ALTER TABLE cliente_servico ADD
    CONSTRAINT fk_cli_serv_servico FOREIGN KEY (id_servico) REFERENCES servico(id_servico);

ALTER TABLE cliente_servico ADD
    CONSTRAINT fk_cli_serv_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente);

-- Constrains de ordem_servico
ALTER TABLE ordem_servico ADD
    CONSTRAINT pk_os PRIMARY KEY (num_os);

ALTER TABLE ordem_servico ADD
    CONSTRAINT fk_os_servico FOREIGN KEY (id_servico) REFERENCES servico(id_servico);

ALTER TABLE ordem_servico ADD
    CONSTRAINT fk_os_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente);

ALTER TABLE ordem_servico ADD
    CONSTRAINT fk_os_funcionario FOREIGN KEY (matr_funcionario) REFERENCES funcionario(matr);

-- Constrains de item
ALTER TABLE item ADD
    CONSTRAINT pk_item PRIMARY KEY (id_item);

-- Constrains de servico_item
ALTER TABLE servico_item ADD
    CONSTRAINT fk_cli_serv_servico FOREIGN KEY (id_servico) REFERENCES servico(id_servico);

ALTER TABLE servico_item ADD
    CONSTRAINT fk_cli_serv_item FOREIGN KEY (id_item) REFERENCES item(id_item);
