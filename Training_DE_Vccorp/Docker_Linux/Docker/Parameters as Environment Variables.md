
- In real life , a container's input and outputs are likely to vary according to the container's environment. For instance, if you run a web application,it is likely to connect to a db and listen for incoming requests on a given DNS. The db connection details and DNS will have different values on a development machine, on the test server and the production server
### Reading a Value #
- Whatever the technology you use inside your container, you can access environment variables. For instance, if you set a name environment variable, you may access it with:

![](Pasted%20image%2020231211151759.png)


### Providing a value

- In order to provide an environment variable’s value at runtime, you simply use the -e name=value parameter on the docker run command.

- A special use case is when the system that runs the container has the name environment variable defined, and you want to reuse it, then you can simply use the -e name parameter without specifying a value.

#### Default Value

- You may also want to define a default value for an environment variable, in case it isn’t provided when a container is created; this may be done in the Dockerfile file, using the ENV instruction. For instance, the following makes sure that if the name variable isn’t provided to the docker run command, it has a default value of Dockie:
```
ENV name=Dockie
```
#### Sample Usage

```
#!/bin/sh 
echo "Pinging $host..." 
ping -c 5 $host
```

```
FROM debian:8 
ENV host=www.google.com
COPY ping.sh . 
CMD ["sh", "ping.sh"]
```

Note that my Dockerfile file includes an ENV instruction that specifies that the host variable will be www.google.com in case it isn’t provided. I create my image from that Dockerfile file by running a docker build command
```
docker build -t pinger .
```


Next, I run two containers based on that image: 

```
docker run --rm pinger
docker run --rm -e host=www.bing.com pinger

```

- We don’t provide the first container with any value for the host environment variable in order for it to default to the www.google.com value specified in the Dockerfile file. The second container is provided the www.bing.com value. Here’s the output from these two containers (shortened for brevity):

![](Pasted%20image%2020231211153156.png)