CREATE USER 'fiapadmin'@'%' IDENTIFIED BY 'fiapadmin';
GRANT ALL PRIVILEGES ON *.* TO 'fiapadmin'@'%';
FLUSH PRIVILEGES;