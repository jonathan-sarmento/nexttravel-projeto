create table capitais(
	id serial primary key,
	nome varchar(50) not null,
	descricao text not null,
	imagem_url varchar(255) not null
);

create table pontos_turisticos(
	id serial primary key,
	nome varchar(50) not null,
	breve_descricao text,
	descricao text,
	id_capital int references capitais(id)
);

create table imagens_url(
	id serial primary key,
	url varchar(255),
	id_ponto_turistico int references pontos_turisticos(id)	
);


-- Inserindo capitais
insert into capitais(nome, descricao, imagem_url) values ('Manaus - Amazonas', 'Bela cidade blabla', 'https://photo980x880.mnstatic.com/1f/4c/1f4c4deac815df1ae0c9cd56cd5c1d7a.jpg');

-- Inserindo pontos turisticos
insert into pontos_turisticos(nome, breve_descricao, descricao, id_capital) values ('Teatro Amazonas', 'Muito lindo o teatro', 'Muito lindo mesmo o teatro', 1); 

select * from imagens_url;