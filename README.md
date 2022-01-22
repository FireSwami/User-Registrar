# User Registrar

User Registrar (UR) - a small web-based interface designed to record attendees 
at various meetings. UR remembers the first and last name of the visitor.
Also you can leave phone number if you wish.
It is not possible to register for the same surname twice.


### Installation

Use ***SETUP*** instructions.


### Usage

Use **[localhost](http://127.0.0.1:8000/)**, 
**[Admin Panel](http://127.0.0.1:8000/admin/)**,
to start registration.
Also you can use 
**[web-site](http://...)**
to do same work.



### Requirements
+ Python version> = 3.9.0
+ Framework - Django> = 3.2.8
+ Database - SQLite

### Addons


+ The project has **[Django Admin Panel](http://127.0.0.1:8000/admin/)**
  for the convenience of filling and maintaining the database
  (you must create and use own username, password; use ***SETUP*** instructions.)


+ Sorting and formatting by ***black*** 
  to improve the code quality. If you need install it try:
  
    >#### pip install -r dev.txt