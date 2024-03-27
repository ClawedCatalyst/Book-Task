# Book-Task

## Endpoints:

### 1) POST `/api/books/`
<img width="1009" alt="image" src="https://github.com/ClawedCatalyst/Book-Task/assets/97229491/72b079c9-b41f-43e8-8109-76ead634ad3f">

### 2) GET `/api/books/`
<img width="999" alt="image" src="https://github.com/ClawedCatalyst/Book-Task/assets/97229491/421f9373-e37c-4ce3-8b8d-cd6a0ebe84f7">

#### 2.1) Pagination in  GET `/api/books/`
<img width="1012" alt="image" src="https://github.com/ClawedCatalyst/Book-Task/assets/97229491/63fd9f79-e36d-4452-970f-3c605c6a661b">
<img width="1011" alt="image" src="https://github.com/ClawedCatalyst/Book-Task/assets/97229491/646c62ee-5d0e-4cc6-a719-84603ebd0f47">

### 3) GET `/api/books/<isbn>`
<img width="993" alt="image" src="https://github.com/ClawedCatalyst/Book-Task/assets/97229491/c311bfe2-e309-42f2-926b-bc1fc7762b61">

### 4) PATCH `api/books/<isbn>`
<img width="1015" alt="image" src="https://github.com/ClawedCatalyst/Book-Task/assets/97229491/f1880222-d0dd-4a1e-9a4f-65a3e527d80f">

### 5) DELETE `api/books/<isbn>`
<img width="1016" alt="image" src="https://github.com/ClawedCatalyst/Book-Task/assets/97229491/4124712e-62b8-4e58-b8f7-ff448f527538">

# SETUP

1. Clone the repository:

```CMD
git clone https://github.com/ClawedCatalyst/Book-Task.git
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Install, Create and activate a virtual environment:

```CMD
pip install virtualenv
virtualenv venv
```

Activate the virtual environment

```CMD
source venv/bin/activate
```

3. Install the dependencies:

```CMD
pip install -r requirements.txt
```

4. Run the migrate command

```CMD
python manage.py migrate
```

5. Run the backend server on localhost:

```CMD
python manage.py runserver
```

You can access the endpoints from your web browser following this url

```url
http://127.0.0.1:8000
```

6. You can create a superuser executing the following commands

```CMD
python manage.py createsuperuer
```

A prompt will appear asking for username followed by password.
To access the django admin panel follow this link and login through superuser credentials

```url
http://127.0.0.1:8000/admin/
```

Run test's

```CMD
python manage.py test
```







