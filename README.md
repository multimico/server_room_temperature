# server_room_temperature

This repository contains the service for measuring the room temperature and humidity of our server room. 

The service is build as a docker container that is supposed to be run on a raspberry pi with Grove Hat. 

## Launch the container

the launch command

```bash
docker-compose up
```

## start node_exporter

```bash
./node_exporter --web.listen-address="0.0.0.0:9100"
``` 
