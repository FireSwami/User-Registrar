1. Clone project on GitHub: **[publik rep. on GiTHub](https://github.com/FireSwami/Park)**
2. Install virtual environment in your sources root directory:

    >#### python -m venv venv

3. Activate virtual environment in your sources root directory:<br>
   on Windows:

    >#### venv\scripts\activate
    
    on macOS & Ubuntu:

    >#### source venv/bin/activate

4. Install libs in your sources root directory:

    >#### pip install -r requirements.txt

5. Create DB:

    >#### python manage.py migrate

7. Creat superuser if you need: 

    >#### python manage.py createsuperuser

8. Start server (you mast have password keies ***.env*** file 
   in sources root directory): 

    >#### python manage.py runserver

8. If you need start server in docker container,
   create container with docker and run it:
    
    >#### docker-compose build
   
    >#### docker compose exec web python manage.py migrate --noinput

    >#### docker-compose up
   
9. Open **[localhost](http://127.0.0.1:8000/)** 
    (for default) and start to visitor's registration.
     - *Also you can use **[Django Admin Panel](http://127.0.0.1:8000/admin/)** 
   in order to correct something.*
     - *Also you can use **[web-site](http://...)** for visitor's rigistration.*
