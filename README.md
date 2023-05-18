# Little Lemon Restaurant API
![Coursera](https://img.shields.io/badge/Coursera-%230056D2.svg?style=for-the-badge&logo=Coursera&logoColor=white)
![Meta](https://img.shields.io/badge/Meta-0668E1?style=flat&logo=meta&logoColor=white)
![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)


A restful API that exposes a restaurant menu items with ability to add and update dishes along displaying the menu list also it provides booking tables 
to authenticated  users, you can register and login as a user through token based authentication.
## URLS Available:
- **GET**: restaurant/menu: returns a list of menu items available

- restaurant/menu/<int:pk>:

  - **GET**: return item with the specified id
  
  - **PUT**: update item with the specified id
  
  - **DELETE**: delete item with the specified id
  
 - restaurant/booking/tables:
 
   - **GET**:return a list of booked tables
  
   - **POST**: booking a table
  
 - **POST**: auth/users/: create a new user
 
 - **POST**: auth/token/login: generate a token for a user

## Installation and Running The Project:
- Installing Python if it's not already setup used Version is 3.11
-  Setting up the virtual environment using pipenv:

```jsx
pipenv install
```
- the required packages : django, djangorestframework, mysqlclient, djoser
- Running pipenv Virtual Environment:

```jsx
pipenv shell
```
- the configuration for mysql Database Connection:

```jsx
DATABASES = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',
        'USER': 'root',
        'PASSWORD': 'root@123',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
}
```
💡 Change those settings according to your local setup.
- Running the server:

```jsx
python manage runserver
```
