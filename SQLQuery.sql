CREATE DATABASE users
go

USE users
go

CREATE Table Customer(
Id int identity primary key,
fullname varchar(100),
phone varchar (20),
)
go

INSERT INTO Customer VALUES ('Henry','57301299999')
select * from Customer

CREATE TABLE Orders(
OrderId int identity primary key,
OrderNumber varchar(100),
Product varchar(100),
CustomerId int foreign key references Customer(Id)
)
go

use master
alter database users set single_user with rollback immediate

drop database users