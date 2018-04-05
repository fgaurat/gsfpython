# Formation Python
## URL documentation : https://docs.python.org/3/tutorial/interpreter.html


## XML
https://docs.python.org/fr/3.6/library/xml.etree.elementtree.html

##argparse
https://docs.python.org/3/library/argparse.html

##Logging
https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

##Server
http://ns349423.ip-94-23-40.eu:8080/
##admin mysql
http://ns349423.ip-94-23-40.eu:8080/adminer.php

user:admin
passw:mypass


##SQL
```
CREATE TABLE tododb.todos (
	id INT NOT NULL AUTO_INCREMENT,
	`action` varchar(100) NULL,
	dueDate varchar(100) NULL,
	CONSTRAINT todos_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci ;
```
---------------------------------------------------------------------------

```
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 1', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 2', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 3', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 1', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 2', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 3', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 1', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 2', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 3', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 1', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 2', '1522245898');
INSERT INTO tododb.todos(`action`, dueDate) VALUES('Action 3', '1522245898');
```