-- Criação da tabela
CREATE TABLE `Reservas`
(
 `id_reserva`      int NOT NULL AUTO_INCREMENT ,
 `status_reserva`  varchar(10) NULL ,
 `nm_titular`      varchar(50) NULL ,
 `cpf_titular`     varchar(11) NOT NULL ,
 `nr_pessoas`      smallint NULL ,
 `tp_quarto`       varchar(1) NULL ,
 `diarias`         smallint NULL ,
 `valor_reserva` int NOT NULL ,

PRIMARY KEY (`id_reserva`)
);

-- Insert de dados
-- Dados gerados aleatoriamente
insert into Reservas (
    status_reserva,
    nm_titular,
    cpf_titular,
    nr_pessoas,
    tp_quarto,
    diarias,
    valor_reserva)
values (
    'Reservado',
    'Joao',
    '25474241296',
    2,
    'P',
    3,
    5500);

insert into Reservas (
    status_reserva,
    nm_titular,
    cpf_titular,
    nr_pessoas,
    tp_quarto,
    diarias,
    valor_reserva)
values (
    'Reservado',
    'Lucas',
    '97845176771',
    2,
    'D',
    3,
    5500);

insert into Reservas (
    status_reserva,
    nm_titular,
    cpf_titular,
    nr_pessoas,
    tp_quarto,
    diarias,
    valor_reserva)
values (
    'Ativo',
    'Lucas',
    '97845176771',
    3,
    'D',
    6,
    6700);

insert into Reservas (
    status_reserva,
    nm_titular,
    cpf_titular,
    nr_pessoas,
    tp_quarto,
    diarias,
    valor_reserva)
values (
    'Ativo',
    'Joana',
    '21549380007',
    1,
    'S',
    1,
    500);

insert into Reservas (
    status_reserva,
    nm_titular,
    cpf_titular,
    nr_pessoas,
    tp_quarto,
    diarias,
    valor_reserva)
values (
    'Ativo',
    'Fernando',
    '57271630630',
    4,
    'P',
    4,
    3500);

insert into Reservas (
    status_reserva,
    nm_titular,
    cpf_titular,
    nr_pessoas,
    tp_quarto,
    diarias,
    valor_reserva)
values (
    'Finalizado',
    'Leonardo',
    '32766603344',
    2,
    'P',
    3,
    2500);

insert into Reservas (
    status_reserva,
    nm_titular,
    cpf_titular,
    nr_pessoas,
    tp_quarto,
    diarias,
    valor_reserva)
values (
    'Finalizado',
    'Maria',
    '10078662846',
    4,
    'P',
    5,
    7500);
