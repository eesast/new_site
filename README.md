# eesast_newsite
The static page for eesast

#### lecture

* The page to show lecture files
* Front-end: Vue
* Back-end: A django project to provide indexes 
  * Index of **LECTURE_DIR** at **backend/lecture/dir/**  
  * Index of **LECTURE_DIR/subdir** at  **backend/lecture/subdir/\<str:subdir\>** 
* Test at local enviroment:
  * Run    **python manage.py runserver 127.0.0.1:8888**  at **./** (the directory where this README file locates)   
  * Get data from     **127.0.0.1:8888/backend/lecture/dir/**  or  **127.0.0.1:8888/backend/lecture/subdir/name-of-subdir** 
    * You can try this by GET from 127.0.0.1:8888/backend/lecture/dir/ in your Postman and you will know how this works
  * Usually, the **name-of-subdir** will be responsed in response of **backend/lecture/dir/ ** 

