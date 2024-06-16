![](Pasted%20image%2020231211141126.png)



- A Docker image is created using the docker build command and a Dockerfile file. The Dockerfile file contains instructions on how the image should be built.
- Ex: create a basic image for a container that displays a "hello world" message when its run
- I create a file named Dockerfile that describes how my image should be built. A Dockerfile always begins with a FROM instrction because every image is based on another image.
 -> This allows you to extend images that may already be complex
 - I can use a Debian Linux Image
 ```
 FROM debian:a
```


- This is not enough. While i do get a Debian Linux basis, i am not running any command that could display "hello world". This can be achieved using the CMD instruction. The CMD instruction specifies which executable is run when a container is created using your image and provides optional arguments
- Here’s an improved Dockerfile file that creates a Debian Linux-based image and instructs it to greet our users when a container spawns:

```
FROM debian:8
CMD ["echo", "Hello world"]
```

- Note that both the program to run and its arguments are provided as a JSON array of strings. 
- In order to create an image from my Dockerfile file, I need to run the docker build command. To do this, I type the following command in my terminal in the folder where the Dockerfile file lives:

```
docker build -t hello .
```

- The -t switch is used in front of the desired image. An image can be created without a name, it would have an auto-generated unique ID, so it is an optional parameter on the docker build command.

```
Note the dot at the end of the command above. It specifies which path is used as the build context (more about that later), and where the Dockerfile is expected to be found. Should my Dockerfile have another name or live elsewhere, I can add a -f switch in order to provide the file path.
```

- The docker build command just created an image named hello. That image is stored locally on my computer, and I can run it as I would any other image:
- Docker run --rm hello As expected, the docker run command above simply prints the message:
- ![](Pasted%20image%2020231211142530.png)