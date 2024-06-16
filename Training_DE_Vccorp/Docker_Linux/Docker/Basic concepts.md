#### Container

```
- A container is an isolated environment for your code. This means that a container has no knowledge of your operating system, or your files. It runs on the environment provided to you by Docker Desktop. Containers have everything that your code needs in order to run, down to a base operating system.
											Document docker
```

- A *container* is what we eventually want to run and host in Docker. You can think of it as an isolated machine, or a virtual machine
- A Container runs inside the Docker host isolated from the other containers and even the host OS. It cannot see the other containers, physical storage, or get incoming connections unless you explicitly that it can. It contain everything it needs to run : OS, packages, runtimes, files,environment variables, standard input and output


Your typical Docker server would look like this — a host for many containers:
![](Pasted%20image%2020231208172443.png)

- We can see there are two app2 containers in the same schema above is normal; this typically the case when a server hosts a release and a test version. Which means you could host both versions on the same server.

#### Images
- Any container that runs is created from an *image* . An image describes everything that is needed to create a container. It is a template for containers. You may create as many containers as needed from a single image

![](Pasted%20image%2020231208173310.png)

#### Registries
- Images are stored in a registry. In the above, the *app2* is used to create two containers
- Each container lives its own life , they both share a common root: their image from the registry