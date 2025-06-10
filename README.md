In this project we learned about 
1. how to make a container using python images 
2. what is port mapping 
3. difference between making a container and running - genrally it is not important beacue it wont play any role in production as we will be working with yaml and docker compose there.

This is not a automated docker file were you can run it with a docker comapose method This is just for practice pupose to make and under how to run docker containers In this repo we will only under how to Step 1: How to build a Dockerfile Step 2: How to build an image out of it Step 3: How to build and run a contaniner out of it

So to build an Image use command as

docker build -t <name of image you want to give> . 

In the above command the term docker will activate the docker engine The term build will start making a image from the provided Dockerfile 
The term -t is called tag the name with which you want to build the image and then the name of image you want to give
'.' represent the context of the file ie from where to pick the dockerfile , the dot represent the pick the docker file from the current file or also you can provide a path

docker run -d --name <name_of_container> -p <port-mapping eg-> 50:8000> <image-name>
  
In the above command the term docker will activate the docker engine The command run will develop a container and start running it 
The command --name is called name the container with which you want to build and if you dont provide the name docker will itself genrate a random one and then the name of image you want to run the container on.
-p is used for port mapping means since docker is an isolates system so to connect your computer or to access the container it is more like a door, a gateway to enter.
Now how to enter the number before the : is your computer exit door(port) and the number after : is your container entry port 
It is advice to keep both the number same for better communication and ease

docker logs <container-name>

This command will give you access to read the docker container action within it will give a sneek peek to get into the container 