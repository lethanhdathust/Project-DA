When your image hosts server software , it listens on one or several ports. Ex, an HTTP server generally listens on the TCP port 80

- You can make this explicit using an EXPOSE instruction:

```
EXPOSE 80
```

Using this instruction is purely for documentation purposes. It will NOT open a port to the outside world when a container is created from that image. Anyone who creates a container will need to explicitly bind that port to an actual port of the host machine using the -p switch of the docker run command. In case you forgot, this is what we saw in the Listening for Incoming Network Connections section.