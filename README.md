# hng-stagetwo
## https://hng-stagetwo-agp4b7p37-halfboyfriend.vercel.app/

# Flask App Rest API with Sqlalchemy db

This is a simple Flask app Rest API that interacts with a Sqlalchemy database using the Flask-Sqlalchemy. It allows you to create, retrieve, update, and delete 'person' resources.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Documentation](#documentation)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [UML Diagram](#uml-diagram)
- [License](#license)

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Node.js](https://nodejs.org/) (with npm)
- [A MongoDB server](https://www.mongodb.com/) (running locally or accessible via a URI)

## Installation

1 . Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Felixdiamond/HNGx_Stage_Two.git
   ```

2 . Change into the project directory:

   ```bash
   cd HNGx_Stage_Two
   ```

3 . Install the required npm packages:

   ```bash
   npm install
   ```

## Configuration

1 . Create a `.env` file in the root directory of the project and add the following environment variables:

   ```env
   PORT=MY_PORT
   CONNECTION_STRING=CONN_STRING
   ```

   Make sure to replace `CONN_STRING` with the connection URI gotten from mongodb. The `PORT` variable is optional and will run at `3000` by default.

## Usage

To start the API server, run the following command:

```bash
npm start
```

To start in developer mode, run:

```bash
npm run dev
```

The server will start on the port specified in your `.env` file (default: 3000). You should see a message in the console indicating that the server is running.


Now visit the Base URL: http://localhost:3000 or whatever port is showed by your server.


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
  "name": "John Doe"
}
```

**Response:**

```http
Status: 200 OK
Content-Type: application/json

{
  "name": "John Doe",
  "_id": "6503015360aa24dfa1c4670a",
  "__v": 0
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
  "_id": "6503015360aa24dfa1c4670a",
  "__v": 0
}
```

### Updating details of a person

**Endpoint:** `PUT /api/{id}`

**Request:**

```http
PUT /api/{id}
Content-Type: application/json

{
  "name": "Jane Doe"
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
    "message": "John Doe David removed successfully"
}
```

## Documentation

Detailed documentation of the API can be at [DOCUMENTATION.md](DOCUMENTATION.md)

## Error Handling

In case of an error, the API returns the following response:

```http
Status: {Error Code}
Content-Type: application/json

{
    "error": "Error Message"
}
```

## Testing
- This api was tested with Postman and the collection of tests can be found here:

    [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/27281373-704cd9f0-8cf5-49cc-9f85-f3e4acb17e45?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D27281373-704cd9f0-8cf5-49cc-9f85-f3e4acb17e45%26entityType%3Dcollection%26workspaceId%3Dfab1b95b-6d58-4b2e-ad4b-d0c0aad72f83)

## UML Diagram
![UML Diagram](static/uml-diagram.png)

