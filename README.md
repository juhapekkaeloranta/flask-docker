# Template for docker + flask

A helloworld flask app inside a docker container. Use this as a project template.

## Structure

The application code is in the `web` folder:

* `app.py` - application code
* `Dockerfile` - build instruction for Docker
* `requirements.txt` - dependencies for build

The project root has `docker-compose.yml` file that makes container management easier. It looks like this:

```
web:
  build: ./web
  ports:
   - "5001:5000"
  volumes:
   - ./web:/app
```

It defines a container with the name `web` and following configurations:

1. Build the container with files from the `web` folder

  ```
  build: ./web
  ```

2. Forward container port 5000 to host port 5001

  ```
  ports:
     - "5001:5000"`
  ```  

3. Set up a "live sync" (=mount) between container folder `/app` and source code folder `./web`. Changes in source code will initiate a automatical rebuild of the container. This is handy in development but should never be used in production!

```
  volumes:
   - ./web:/app
```

## Commands

Start the server:

```
docker-compose up
```

Add `-d` for detached mode.

```
docker-compose up -d
```

Attach to the container:

```
docker exec -i -t flaskdocker_web_1 bash
```