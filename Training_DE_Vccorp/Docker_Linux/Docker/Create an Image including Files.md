
- Suppose i have a file named index.html like this: 
- ![](Pasted%20image%2020231211143035.png)
- I want to create an image that includes a web server that includes a web serves the above page over HTTP. NGINX is a good candidate. I could keep using the debian base image and add instructions to my Dockerfile that install NGINX, but it is easier to base my work on images that are already configured and tested . 
- The Docker contain an NGINX image where NGINX has already been installed with a configuration that serves files found in the */usr/share/nginx/html directory.*
- I  create the following Dockerfile file in the same folder as the HTML file

```
FROM nginx:1.15 COPY index.html /usr/share/nginx/html
```

- COPY instruction, its first parameter is the file to be copied from the build context and its second parameter is the destination directory inside the image.
- The build context is basically the directory you provide ,to the docker build command. Its contents are available for COPY instructions to use, but only during the image build process. That means it's available only for the instructions in the Dockerfile file, and files from it won't be a part of the build image or containers that u will spawn from that image unless u use the COPY instructions.

- You may have noticed that this time the Dockerfile file contains no CMD instruction. Remember that the CMD instruction states which executable should be run when a container is created from my image, so it’s weird that I don’t include a CMD instruction that runs an NGINX server. The reason why I didn’t include a CMD instruction is because the base nginx:1.15 image already contains a CMD instruction to run the NGINX server. This is part of my image and I don’t need to include my own CMD instruction as long as I don’t want to run another executable on container startup. 
- Back to creating our HTTP server image, I open a command line inside the folder where my index.html and Dockerfile files are, and run the following commands:
```
docker build -t webserver . 
docker run --rm -it -p 8082:80 webserver
```


- When running my container, I added the –rm and -it switches simply for demo purposes.
- In reality, that server container would be long-running, so I’d run it without those switches. 
- Here’s why I used the switches: 
- The -it switch allows me to stop the container using Ctrl-C from the command-line 
- The –rm switch ensures that the container is deleted once it has stopped
`--rm`: This flag automatically removes the container when it stops running. This helps to clean up after the container exits.

`-it`: These flags are two separate options combined:

- `-i`: This flag stands for "interactive." It keeps STDIN open even if not attached, allowing you to interact with the container.
- `-t`: This flag allocates a pseudo-TTY (terminal). It provides an interface for interacting with the container.