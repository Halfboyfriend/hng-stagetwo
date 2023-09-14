# hng-stagetwo


## https://hng-stagetwo-1f2d786746f2.herokuapp.com/api

# Flask App Rest API with Sqlalchemy db

This is a simple Flask app Rest API that interacts with a Sqlalchemy database using the Flask-Sqlalchemy. It allows you to create, retrieve, update, and delete 'person' resources.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [UML Diagram](#uml-diagram)
- [Live Link](#Link)

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Node.js](https://python.org/) (pip)

## Installation

1 . Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Halfboyfriend/hng-stagetwo.git
   ```

2 . Change into the project directory:

   ```bash
   cd hng-stagetwo
   ```

3 . Install the required npm packages:

   ```bash
  pip install -r requirements.txt
   ```


## Usage

To start the API server, run the following command:

```bash
python main.py
```


Now visit the Base URL: http://127.0.0.1:5000/ or whatever port is showed by your server.


## API Endpoints

The API provides the following endpoints:

- `POST /api` - Create a new person
- `GET /api/:{id}` - Fetch details of a person by ID or name
- `PUT /api/:{id}` - Modify details of an existing person by ID or name
- `DELETE /api/:{id}` - Remove a person by ID or name


## Usage

### Add a new person

**Endpoint:** `POST /api`

**Request:**

```http
POST /api
Content-Type: application/json

{
  "name": "John Doe",
  "age": 22,
  "email": "john@gmail.com"
}
```

**Response:**

```http
Status: 200 OK
Content-Type: application/json

{
  "name": "John Doe",
  "id": 11,
   "age": 22,
  "email": "john@gmail.com"
}
```

### Fetching details of a person

**Endpoint:** `GET /api/{id}`

**Request:**

```http
GET /api/{id}
```

**Response:**

```http
Status: 200 OK
Content-Type: application/json

{
  "name": "John Doe",
  "id": (specified id),
   "age": 22,
  "email": "john@gmail.com"
}
```

### Updating details of a person

**Endpoint:** `PUT /api/{id}`

**Request:**

```http
PUT /api/{id}
Content-Type: application/json

{
  "name": "John Doe",
  "id": 11,
   "age": 22,
  "email": "john@gmail.com"
}
```

**Response:**

```http
Status: 200 OK
Content-Type: application/json

{
  "name": "Jane Doe",
  "_id": "6503015360aa24dfa1c4670a",
  "__v": 0
}
```

### Deleting a person

**Endpoint:** `DELETE /api/{id}`

**Request:**

```http
DELETE /api/{id}
```

**Response:**

```http
Status: 200 OK
Content-Type: application/json

{
    "message": "Person deleted successfully"
}
```

## Documentation

Detailed documentation of the API can be at [README.md](README.md)

## Error Handling

In case of an error, the API returns the following response:

```http
Status: {Error Code}
Content-Type: application/json

{
    'message': 'Person doesnt exist'
}
```

## Testing
- This api was tested using python script 
[test.py](test.py)
- This api was tested with Postman and the collection of tests can be found here:

    [![Run in Postman](https://run.pstmn.io/button.svg)](static/api.png)

## UML Diagram
![UML Diagram](static/uml-diagram.png)

## Link

![Live URL](https://hng-stagetwo-1f2d786746f2.herokuapp.com/api)
