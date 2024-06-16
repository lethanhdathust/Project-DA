- Some short-lived containers -> we usually do some processing and display some output.
- However, there's a very common use for long-lived containers: server containers. Whether you want to host a web application, an API, or a database , *a container that listen for incoming network connections and is potentially long-lived*
```
It is best not to think containers as long-lived, even when they are
```

#### Running a long-lived container
- docker run command -> impractical for running long-lived containers
- To disconnect while allowing the long-lived container to continue running in the background, we use the -d or -detach switch on the docker run command
- Running a container as detached means that you immediately get your command-line back and the standard output from the container is not redirected to your command-line anymore
- Suppose *ping* command , i can use a Linux alpine for this:

```
docker run alpine ping www.docker.com
```

![](Pasted%20image%2020231211103713.png)


- Ping command doesn't end since it keeps pinging the Docker server.
- I can detach fro it using the CTRL-C shortcut, and it keeps running in the background.
- However, we can run it detach from the beginning: 

```
docker run -d alpine ping www.docker.com
```
- when we use -d , the container start but we don't see the output. Instead , the docker run command returns the ID of the container that was just created'
- ![](Pasted%20image%2020231211104231.png)
- We can interact with the running container using: *docker logs* to see its output, *docker inspect* to get detail information and *docker stop* to kill it
- We can can get a portion of the output using the -from , -until or tail switches.
- Ex: See the most recent 10 seconds of logs for running container
```
docker logs --since 10s 789b
```
- We can stop and clean up that container
```
docker stop 313
docker rm 313
docker ps -a
```

### Listening for incoming Network connections

- A containers runs in isolation , as such, it doesn't listen for incoming connections on the machine where it is running. We must explicitly open a port on the host machine and map it to a port on the container.
- Suppose i want to run the NGINX wen server. It listens for incoming HTTP requests on port 80 by default. It simply run the server, my machine does not route incoming requests to it unless i use the -p switch on the docker run command.
- The -p switch takes two parameters:
	- The incoming port u want to open on the host machine
	- The port to which it should be mapped inside the container.

- Ex: i want my machine to listen for incoming connections on port 8085 and route them to port 80 inside a container:
```
docker run -d -p 8085:80 nginx
```

