The latest tag #
In my demonstrations I didn’t include a tag; therefore the default latest tag was used. For instance, the actual image name was hello:latest when I ran the following command:

```
docker build -t hello .
```

As long as you are creating simple software, running on a simple CI/CD pipeline, it can be fine to use the latest tag. In a simple scenario, you may: 1. Update the source code 
2. Build a new image with the latest tag 
3. Run a new container with the newest image
4. Kill the previous container There’s a caveat with this however: when using the docker run hello command on a distant machine (which actually means docker run hello:latest), the distant machine has no means to know that there is a newer version of the hello:latest image. You need to run the docker pull hello command on the distant machine in order for the newest version of your image to be downloaded to that machine. 

#### Why would you tag your Images
- You may want any or all of the following features:
	-  Be able to roll back to a previous version of an image if you detect a problem with the latest image
	- Run different versions in different environments . Ex : latest version => text environment ; previous version -> production environment
	- Run different versions at the same time
	- Deploy different versions to different users, and able to run whatever version on your development machine while u sp them
	- In order to apply a tag: 
	- 
```
docker build -t hello:1.0 .
```


Tags for Base Images # 
Remember your images are based on other images; this is done using the FROM instruction in your Dockerfile file. Just as you can tag your images, the base image you use can be the latest one or a tagged one. 
In my demos, I used tagged images. For instance, I based my server image on the nginx:1.15 base image. It’s quite tempting to base your images on the latest ones so that you’re always running on up-to-date software, especially since it’s so straightforward. All you need to do is omit the tag altogether or mention the latest one. You could be tempted to use the following instruction in your Dockerfile file