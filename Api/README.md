# Contents:

-  ### [About the project](#about)
-  ### [Getting Started](#start)
-  ### [API Endpoints](#api)
  
## <a name="about">About the project</a>

Welcome to the Book Management API documentation! This project provides a robust CRUD (Create, Read, Update, Delete) API for efficiently managing a collection of books. The implementation leverages advanced technologies, including the Python programming language, Django Rest Framework, Django framework, and a database for seamless data management.



## <a name="start">Getting Started</a>
### Prerequisites
Before diving into the project, ensure that you have the following prerequisites installed on your system:
    
    Python (version 3.12.0 or higher)

### Installation

**1.Clone the repository to your local machine:**


    git clone https://github.com/antonmolchanov18/BooksAPI.git

**2.Navigate to the project directory:**

    cd booksapi/api

**3.Create venv:**

    python -m venv venv

**4.Activate venv:**

    .\venv\Scripts\activate

**5.Install project dependencies:**

    pip install -r requirements

**6.Navigate to the project directory:**

    cd bookapi

**6.Make migrations:**
     
    python manage.py makemigrations  

**7.Migrate the database:**

    python manage.py migrate

**8.Create a superuser:**

    python manage.py createsuperuser

**9.Run the development server:**
    
    python manage.py runserver



## <a name="api">API Endpoints</a>
For effective testing of Book Management API functionality, it is recommended to use Postman, a powerful API development and testing tool. In this section, we'll provide some examples and instructions for using Postman to interact with the API.

**You can also use the provided interface of the Rest framework ( ^ ω ^)**

PK (Primary Key) and its Role in API Endpoints

In the context of API endpoints, the term "PK" refers to the Primary Key, which is a unique identifier assigned to each record in a database table. In relational databases, including those commonly used with APIs, the primary key is crucial for uniquely identifying and accessing individual records.
## Authorization

URL for Authorization:
http://127.0.0.1:8000/api/drf-auth/login/

Method: POST

Description: Access secure resources, enter your credentials, and receive an authorization token.


## 1. Retrieve All Books
Endpoint: http://127.0.0.1:8000/api/books/

Method: GET

Description: Retrieve a list of all books in the collection.


## 2. Create a New Book
Endpoint: http://127.0.0.1:8000/api/books/

Method: POST

Description: Add a new book to the collection.


## 3. Retrieve a Specific Book

Endpoint: http://127.0.0.1:8000/api/books/<int:pk>/

Method: GET

Description: Retrieve details for a specific book identified by {book_id}.


## 4. Update a Book

Endpoint: http://127.0.0.1:8000/api/books/<int:pk>/

Method: PUT

Description: Update the details of a specific book identified by {book_id}.


## 5. Delete a Book

Endpoint: http://127.0.0.1:8000/api/booksdelete/<int:pk>/

Method: DELETE

Description: Remove a specific book from the collection.



