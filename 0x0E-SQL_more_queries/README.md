## `SQL` - More queries

This builds upon the directory: [SQL Introduction](../0x0D-SQL_introduction)  
Covers: How to `CEATE` a `MySQL user` and Grant Permissions(`Privileges`) to **user**, MySQL `constraints`, SQL `subqueries`, SQL `joins`

#### Run SQL statements like this:  
```bash
$ cat file_name.sql | mysql -hlocalhost -uroot -p db_name
```
as root usr you can leave out: **-h** **-u** **-p**

---
#### Database Dumps
> **Note**:  
> as a **root** user; create the destination DB in your MySQL server before dumping  
> `$ echo "CREATE DATABASE db_name;" | mysql`

- `hbtn_0d_tvshows_rate`:  
```bash
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql" -s | msql hbtn_0d_tvshows_rate
```

- `hbtn_0d_tvshows`:  
```bash
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | msql hbtn_0d_tvshows
