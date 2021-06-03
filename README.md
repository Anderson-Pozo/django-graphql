# Django Graphql example
This is a simple example of an API using Django Graphql with Docker

## 📑 Prerequisites

- Docker
- Code editor

## ⚙ Installing
1. Clone the repository
    ```sh
   https://github.com/Anderson-Pozo/django-graphql.git
   ```
2. Create .env file
    ```sh
    DB_HOST= dbpostgres
    POSTGRES_PORT=5432
    POSTGRES_DB=db
    POSTGRES_USER=user_postgres
    POSTGRES_PASSWORD=password
    ``` 
3. In root directory run the command
    ```sh
    docker-compose up -d
    ```
4. Check if containers are running
    ```sh
   docker ps
   ```

## ✔ Test API
To test the API you can use Postman or any application
that Graphql supports

- Get all actors
```sh
query {
    actors {
        id
        name
        nationality
        age
    }
}
```
- Create actor
```sh
    mutation{
    createActor(input: 
    {name: "Antonio Banderas", 
    nationality: "Mexican", 
    age: "32"})
    {
        actor{
            id
            name
            nationality
            age
        }
    }
}
```
[Download the collection of API requests]()
## ⚙ Built with

* [Django](https://docs.djangoproject.com/en/3.2/)
* [Docker](https://docs.docker.com/)
* [Postgres](https://www.postgresql.org/docs/)
* [Graphql - Graphene](https://docs.graphene-python.org/projects/django/en/latest/)

## 👦 Author

* **Anderson Pozo**