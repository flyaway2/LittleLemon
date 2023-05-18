# Little Lemon Restaurant API
![Coursera](https://img.shields.io/badge/Coursera-%230056D2.svg?style=for-the-badge&logo=Coursera&logoColor=white)
A restful API that exposes a restaurant menu items with ability to add and update dishes along displaying the menu list also it provides booking tables 
to authenticated  users, you can register and login as a user through token based authentication.
## URLS Available:
-GET: restaurant/menu: returns a list of menu items available
-restaurant/menu/<int:pk>:
  -GET: return item with the specified id
  -PUT: update item with the specified id
  -DELETE: delete item with the specified id
 -restaurant/booking/tables:
  -GET:return a list of booked tables
  -POST: booking a table
 -POST: auth/users/: create a new user
 -POST: auth/token/login: generate a token for a user
