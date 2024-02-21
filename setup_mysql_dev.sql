-- Creating User and Grant Privilage

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS
'hbnb_dev'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';

FLUSH PRIVILEGES;
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
