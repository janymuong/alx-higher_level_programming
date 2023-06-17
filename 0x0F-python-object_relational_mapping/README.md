# Object-Relational Mapping (ORM)  
> This project is two-parts:  
>> `MySQLdb - MySQLClient`, `SQLAlchemy` 

`Object-Relational Mapping` - ORM is a programming technique that allows programmers to work with relational databases using object-oriented programming languages. It provides a convenient and intuitive way to interact with the database by abstracting the underlying SQL queries and data access operations.

## How ORM Works
ORM maps *`database tables`* to *`object classes`* and *`table columns`* to *`object attributes`*. Thus, it allows manipulation of database records as objects, making the code easier to maintain, and less context switching between Python and raw SQL.

With an ORM, developers define models or classes that represent database tables. These models encapsulate the table structure and define relationships between tables using object-oriented concepts like inheritance and associations (e.g., one-to-one, one-to-many, many-to-many). The ORM then handles the translation between the object-oriented operations and the corresponding SQL queries required to interact with the database.

`ORM` frameworks typically provide various **features**, such as:
```bash
- Automatic generation of SQL queries
- Database schema creation and migration
- Data validation and type checking
- Transaction management
- Query optimization and caching
- Support for multiple database backends
```

## Built with:

- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/): Python Object Relational Mapper.
- [MySQLdb](): Has features to create connection objects to MySQL database management system(DBMS), and execute SQL.
- [MySQL](): dbms
- [Python]()


## Environment:

> **Note**  

> - Ubuntu 20.04  
> - SQLAlchemy==1.4.41  
> - MySQL: 8.0.33-0ubuntu0.20.04.2  
> - MySQLdb: MySQLdb.version_info(2, 1, 1, 'final', 0)
