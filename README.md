# Task Management System

### Run the following commands to get started:

```
git clone https://github.com/MaulikZalavadiya/scaletech_task.git User_Role_Management
python3 -m venv venv
```
#### Activate the virtual environment

Mac OS / Windows
```source env/bin/activate```

Linux
```.\env\Scripts\activate```

```
cd User_Role_Management
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

# Overview

This project is a Django-based User and Role management system that includes the following features:

* CRUD operations for Users and Roles.
* Role-based access control.
* User signup and login APIs.
* Management of access modules for roles.
* Bulk user updates and efficient search functionality.
<a name="Features"></a>
## [Features](#Features)
* **Role Module:** Allows managing user roles with a list of access modules.
    * **Fields:** roleName, accessModules, createdAt, active.
* **User Module:** Manages user details and assigns roles.
    * **Fields:** firstName, lastName, email, password, role.
* **Access Module Management:**
    * Add and remove access modules.
    * Ensure unique access module values.
    * Check if a user has access to a specific module.
* **Bulk User Updates:** Update multiple users with the same or different data in a single call.
* **Search:** Search users based on first or last name.

<a name="Requirements"></a>
## [Requirements](#Requirements)

* Python 3.8+
* Django 4.0+
* Django REST Framework
* Django REST Framework Token Authentication

<a name="table-of-contents"></a>
## [Table of Contents](#table-of-contents)

In order to achieve all of these results, it is necessary to send the **_Authorization: Token_** with each link.

#### Note: Folder screenshots contains images for all operations.

* [Authentication](#auth)
  * Signup ```http://127.0.0.1:8000/user/sigup```
  * Login ```http://127.0.0.1:8000/user/login```
  * Logout ```http://127.0.0.1:8000/user/logout```
  
* User [CRUD Operations](#crud)
  * All User ```http://127.0.0.1:8000/user/users/```
  * Create User ```http://127.0.0.1:8000/user/users/```
  * Retrieve specific User ```http://127.0.0.1:8000/user/users/id/```
  * Update User ```http://127.0.0.1:8000/user/users/id/```
  * Delete User ```http://127.0.0.1:8000/user/users/id/```

* Role [CRUD Operations](#crud)
  * All Role ```http://127.0.0.1:8000/user/roles/```
  * Create Role ```http://127.0.0.1:8000/user/roles/```
  * Retrieve specific Role ```http://127.0.0.1:8000/user/roles/id/```
  * Update Role ```http://127.0.0.1:8000/user/roles/id/```
  * Delete Role ```http://127.0.0.1:8000/user/roles/id/```

* [Filter Tasks](#filter)
  * Search Users ```http://127.0.0.1:8000/user/users/?search=ma```

* [Bulk Update](#update)
  * Bulk update Users ```http://127.0.0.1:8000/user/users/bulk_update/```


* [Module Check](#modulecheck)
  * Module Check ```http://127.0.0.1:8000/user/users/check_access/?module=user```

* [Multiple User Update](#multipleuserupdate)
  * Module Check ```http://127.0.0.1:8000/user/users/user_update/```

  


[Raseedi]: http://www.raseedi.co/


<a name="auth"></a>
<a name="crud"></a>
<a name="filter"></a>
<a name="update"></a>
<a name="modulecheck"></a>
<a name="multipleuserupdate"></a>