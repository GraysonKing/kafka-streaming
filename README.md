# kafka-streaming
Using kafka and docker to stream data.

## Setting up the Docker environment on Digital Ocean (preinstalled with Docker CE)

Create/Access a Digital Ocean server and create a new droplet, selecting the Docker one-click app.

Get your Digital Ocean API key and export it as a variable on the command line:

```
export DOTOKEN=your_api_key
```

Create the nodes:

```
	for i in 1 2 3; do docker-machine create --driver digitalocean \
	--digitalocean-image  ubuntu-16-04-x64 \
	--digitalocean-access-token $DOTOKEN node-$i; done
```

Make one of these nodes the swarm leader, and get the others to join the swarm then run these commands on all of the nodes that are in the swarm:

```
sudo ufw allow 22/tcp && sudo ufw allow 2376/tcp && sudo ufw allow 2377/tcp && sudo ufw allow 7946/tcp && sudo ufw allow 7946/udp && sudo ufw allow 4789/udp && sudo ufw allow 2181/tcp && sudo ufw allow 2181/udp &&  sudo ufw allow 9092/tcp && sudo ufw allow 9092/udp && sudo ufw allow 8080/tcp && sudo ufw allow 8080/udp && sudo ufw allow 9094/udp && sudo ufw allow 9094/tcp
```

Enable and reload ufw, and restart the docker service.

```
sudo ufw enable && sudo ufw reload && systemctl restart docker
```

After this go to your Digital Ocean and resize the three nodes you just created to have at least 2GB of RAM, both Kafka and Zookeeper use ~1GB in this project so this will prevent any out of memory errors.

## Setting up the containers on Docker CE

Clone this repository onto your machine:

```
git clone GraysonKing/kafka-streaming
```

Start the containers with the YAML file either with docker-compose or docker stack:

docker-compose:
```
docker-compose -f dc.yml up -d
```

docker stack:
```
docker stack deploy -c dc.yml kafkastreaming
```

Then test the containers, with curl or by opening the page in your browser. By default it will be available on port 8080

## Setting up on Docker EE

Follow this [guide](https://docs.docker.com/install/linux/docker-ee/ubuntu/#set-up-the-repository) to get Docker EE to work, then set up the containers with docker-compose or docker stack

Clone this repository onto your machine:

```
git clone GraysonKing/kafka-streaming
```

Start the containers with the YAML file either with docker-compose or docker stack:

docker-compose:
```
docker-compose -f dc.yml up -d
```

docker stack:
```
docker stack deploy -c dc.yml kafkastreaming
```
