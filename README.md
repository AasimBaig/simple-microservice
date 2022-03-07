## Simple Backend Microservice

---

To run :

1. Install Docker
2. Inside cmd `docker-compose build`
3. `docker-compose up`

---

Test queries on `localhost:8000`
or `0.0.0.0:8000`

```
query{
    allcheck
}

query{
  allCollections{
    title
    verified
    image
    snippets
  }
}
```
