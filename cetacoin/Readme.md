
## CETACOIN BACKEND

<summary>Table of Contents</summary>
<ol>
<li><a href="#build-with">Build with</a></li>
<li><a href="#prerequisites ">Prerequisites </a></li>
<li><a href="#usage">Usage</a></li>
</ol>
</details>

### Build with
- Python 3.6
- Django 3.1.4

### 
Backend of cetacoin is responsible of taking care about the following list

- Login: Using  email and password attributes defined under **UserCrypto** model you can log in to the app 
- Register: Using  first_name, last_name, email and password attributes you can also register a new user 

### Prerequisites 

- `pip install django`
- `pip install djangorestframework-simplejwt`
- `pip install PyJWT`
- `pip install django-cors-headers`
- `pip install djangorestframework`
 
 ### Usage
 The app has those endpoint to use it
 
- `/api/auth/register`
- `/api/auth/login`
