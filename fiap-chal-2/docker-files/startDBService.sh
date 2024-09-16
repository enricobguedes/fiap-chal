#!/bin/bash


# Instalar DB
yes y | sudo apt install mysql-server
# Configurar banco
sudo apt-get update
sed -i "s/bind-address            = 127.0.0.1/bind-address            = 0.0.0.0/g" /etc/mysql/mysql.conf.d/mysqld.cnf
sudo service mysql restart

#Criar banco e user do banco
echo -e '\n' | mysql -u root < /createDB.sql 
echo -e '\n' | mysql -u root < /databaseMngmt.sql