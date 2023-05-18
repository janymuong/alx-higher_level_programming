## `SQL` - More queries

> this builds upon the directory: [SQL Introduction](../0x0D-SQL_introduction)  
> covers: How to `CEATE` a `MySQL user` and Grant Permissions(`Privileges`) to **user**, MySQL `constraints`, SQL `subqueries`, SQL `joins`

---
### Database Dumps
> **Note:**  
> as a `root` user; create the destination DB in your MySQL server before dumping  
> $ echo "CREATE DATABASE db_name;" | mysql

- `hbtn_0d_tvshows_rate`:  
```bash
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql" -s | msql hbtn_0d_tvshows_rate
```

- `hbtn_0d_tvshows`:  
```bash
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | msql hbtn_0d_tvshows_rate
```
