use test;
drop table if exists users;
create table users(
	id int(11) unsigned primary key auto_increment,
	name varchar(100) not null,
	address text not null
)