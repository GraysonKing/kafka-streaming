# kafka-streaming
Using kafka and docker to stream data.


Installing Docker EE on a Virtual Machine
Setup Repository

Steps from (https://docs.docker.com/install/linux/docker-ee/ubuntu/#set-up-the-repository)

Check for Updates to the system:

sudo apt-get update

Install packages allow apt to use repository over HTTPS:

```
sudo apt-get install \
    	apt-transport-https \
    	ca-certificates \
    	curl \
    	software-properties-common
```

Add a Docker Enterprise Edition URL into your environment:

```
DOCKER_EE_URL="<DOCKER-EE-URL>"
```

ADD a Docker Enterprise Edition Version to your environment

```
DOCKER_EE_VERSION=stable-17.06
```
Add Docker’s official GPG key using the docker EE repository URL

```
curl -fsSL "${DOCKER_EE_URL}/ubuntu/gpg" | sudo apt-key add -
```

Verify you now have a key with the fingerprint DD91 1E99 5A64 A202 E859 07D6 BC14 F10B 6D08 5F96

```
sudo apt-key fingerprint 6D085F96
```

Set up the Stable repository

```
sudo add-apt-repository \
   	"deb [arch=amd64] $DOCKER_EE_URL/ubuntu \
  	 $(lsb_release -cs) \
stable-17.06"
```

When running this command I got an error message “Failed to exec method /usr/lib/apt/methods/”: 



Open to edit: /etc/apt/sources.list

Navigate to near the bottom of the file “deb [arch=amd64] ://storebits.docker.com/ee/trial/sub-ff6f6fa4-ddc4-4b17-b8e8-0182c70bb670/ubuntu bionic stable-17.06”

And change it to “deb [arch=amd64] https://storebits.docker.com/ee/trial/sub-ff6f6fa4-ddc4-4b17-b8e8-0182c70bb670/ubuntu bionic stable-17.06”

Install Docker EE

Check for Updates

sudo apt-get update

Install Docker EE

sudo apt-get install docker-ee

Installing Kafka GitHub
Go to Github to copy the url for the repo:

https://github.com/GraysonKing/kafka-streaming

Go into Terminal and clone the repo

Git clone https://github.com/GraysonKing/kafka-streaming.git

Installing Kafka on Digital Ocean (preinstalled with Docker CE)

Create the nodes 

```
	for i in 1 2 3; do docker-machine create --driver digitalocean \
	--digitalocean-image  ubuntu-16-04-x64 \
	--digitalocean-access-token $DOTOKEN node-$i; done
```
Make one of these node the swarm leader, and get the others to join the swarm then run these commands on all of the nodes that are in the swarm:

```
sudo ufw allow 22/tcp && sudo ufw allow 2376/tcp && sudo ufw allow 2377/tcp && sudo ufw allow 7946/tcp && sudo ufw allow 7946/udp && sudo ufw allow 4789/udp && sudo ufw allow 2181/tcp && sudo ufw allow 2181/udp &&  sudo ufw allow 9092/tcp && sudo ufw allow 9092/udp && sudo ufw allow 8080/tcp && sudo ufw allow 8080/udp && sudo ufw allow 9094/udp && sudo ufw allow 9094/tcp
```

Enable and reload ufw, and restart the docker service.

```
sudo ufw enable && sudo ufw reload && systemctl restart docker
```

Build Docker

Navigate into the kafka-streaming folder
Build Kafka
docker build -t kafka .
Run Docker with kafka build
docker run -d kafka
Test the connection with curl
curl http://142.93.241.247:8080/


Creating DO nodes:
	for i in 1 2 3; do docker-machine create --driver digitalocean \
	--digitalocean-image  ubuntu-16-04-x64 \
	--digitalocean-access-token $DOTOKEN node-$i; done
