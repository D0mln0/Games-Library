# Games-Library
Visit the site:
https://games-library-qdwk.onrender.com

```
Login: SFG
Password: utGGtGsT5nTMJ66
```

Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata dump.json
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />


1. You can turn on "Remember me" button, if you want to stay logged in after leaving the website
Data base structure:
![img.png](photo/img.png)

Login page:
![img_1.png](photo/img_1.png)

Register page:
![img_2.png](photo/img_2.png)

Home page:
![img_3.png](photo/img_3.png)

Small footer:
![img_14.png](photo/img_14.png)

Page with game list:
![img_4.png](photo/img_4.png)

Game detail page:
![img_5.png](photo/img_5.png)

Game delete page:
![img_6.png](photo/img_6.png)

Game update page:
![img_7.png](photo/img_7.png)

Publisher list page:
![img_8.png](photo/img_8.png)

Publisher details:
![img_9.png](photo/img_9.png)

Publisher update:
![img_10.png](photo/img_10.png)

Players list page:
![img_11.png](photo/img_11.png)

Player detail page:
![img_12.png](photo/img_12.png)

Player update page:
![img_13.png](photo/img_13.png)