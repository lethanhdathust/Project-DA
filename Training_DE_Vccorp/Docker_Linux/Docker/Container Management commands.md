In this lesson, you will be introduced to some commands which can help you manage containers.

- You can get help for Docker commands from the command-line itself using the
–help switch. For instance, in order to know more about the docker run
command we used in the previous lesson, you could type:

```
docker run --help
```

You may use the following commands for container management:
- docker ps: lists the containers that are still running. Add the -a switch in
order to see containers that have stopped
- docker logs: retrieves the logs of a container, even when it has stopped

- docker inspect: gets detailed information about a running or stopped
container

- docker stop: deletes a container that is still running

- docker rm: deletes a container
In the next lesson, we will get a chance to us