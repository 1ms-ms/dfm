CREATE TABLE note (
    id int NOT NULL AUTO_INCREMENT,
    content varchar(255) NOT NULL,
    PRIMARY KEY(id));

GRANT ALL PRIVILEGES  ON testdb.* TO 'testuser'@'localhost' IDENTIFIED BY 'testpass' WITH GRANT OPTION;

GRANT ALL PRIVILEGES ON *.* TO 'testuser'@'localhost' WITH GRANT OPTION;

GRANT ALL PRIVILEGES  ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass' WITH GRANT OPTION;

GRANT ALL PRIVILEGES ON *.* TO 'testuser'@'%' WITH GRANT OPTION;
