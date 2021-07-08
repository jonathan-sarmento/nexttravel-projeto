create table cidades(
	id serial primary key,
	estado varchar(3) not null,
	nome varchar(50) not null,
	imagem_url varchar(255),
	alimentacao text,
	hospedagem text
);

create table pontos_turisticos(
	id serial primary key,
	nome varchar(50) not null,
	descricao text,
	id_cidade int references cidades(id) not null
);

create table imagens_url(
	id serial primary key,
	url varchar(255),
	id_ponto_turistico int references pontos_turisticos(id)	not null
);


-- Inserindo campos

insert into cidades(estado, nome, imagem_url, alimentacao, hospedagem) 
values ('RJ',
		'Rio de Janeiro',
		'https://www.soniaferreiraimoveisrj.com.br/modulos/bairros/202004252129503601.jpg',
		'Almoçamos no restaurante Siqueira Grill, fica na Rua Siqueira Campos, 16 - Loja B - Copacabana.Excelente buffet, com uma grande variedade, tem de tudo que você imaginar, churrasco, sushi, frutos do mar e o ambiente super agradável.',
		'Ficamos no Orla Copacabana Hotel. Apenas elogios, simplesmente amei o hotel, muito limpo e bem aromatizado, o café da manhã é maravilhoso, o quarto lindo e aconchegante, a cama confortável e grande, funcionários esbanjando simpatia e educação, muito bem localizado, a piscina com uma vista espetacular, espero voltar em breve.'
		);

insert into pontos_turisticos(nome, descricao, id_cidade) 
values (
		'Praia de Copacabana',
		'A praia é lindíssima, muitas pessoas praticando espostes, varios quiosques, além de vendedores ambulantes.O calçadão, feito com pedras portuguesas pretas e brancas, é outro símbolo do local. Confesso que pra caminhar na areia tem que ter disposição, não sei explicar mas é diferente das demais praias que visitei, foi cansativo e maravilhoso ao mesmo tempo. Foi um passeio maravilhoso. Uma dica é preparar o bolso caso queira passar o dia.',
		12
		);

insert into imagens_url(url, id_ponto_turistico) 
values (
		'https://www.livima.com.br/blog/wp-content/uploads/2017/10/1469063274-Copacabana_beach.jpg',
		12
);


insert into cidades(estado, nome, imagem_url, alimentacao, hospedagem) 
values ('MG',
		'Poços de Caldas',
		'http://blog.ibrturismo.com.br/wp-content/uploads/2016/03/10503481_729292023778887_2110779090_o.jpg',
		'Não me lembro no nome do restaurante que almoçamos, mas apesar de ser uma cidade turítica, as refeições tem um preço justo.',
		'Me hospedei na Pousada Girassol. As refeições são muito boas, funcionários atencioso, alpendre da entrada com redes de descanso e bancos de madeira. Área comum do hotel em geral muito boa trazendo paz e tranquilidade, exceto quando passa carros na pista. Gostamos principalmente da atenção dos funcionários. O que deixou a desejar foi o estado de conservação'
		);

insert into pontos_turisticos(nome, descricao, id_cidade) 
values (
		'Recanto Japonês',
		'A cidade já é um ponto turítico, as ruas, os jardins abertos, a arquitetura. Fui pelas termas, águas de origem vulcânica, sai revitalizada da imersão. Visitei o recanto Japonês que é lindíssimo. O que mais me encantou e me faz querer voltar é o prazer de estar próxima a natureza, nos recantos podemos alimentar os macacos, é extraordinario. Poços de Caldas é uma cidade maravilhosa, voltarei muitas e muitas vezes.',
		13
		);

insert into imagens_url(url, id_ponto_turistico) 
values (
		'https://i.pinimg.com/originals/6c/9e/3b/6c9e3b2fe1852a598daedc6ef60c433a.jpg',
		13
);
	
select * from imagens_url;
SELECT * FROM pontos_turisticos;
select * from cidades;



