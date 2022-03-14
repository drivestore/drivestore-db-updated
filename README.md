# drivestore-db-updated

#Building 

Docker build . -t devdb


#Running 
docker run  -p 8080:8080  -p 5432:5432 --env PUSH_KEY=DRIVESTORE_KEY  -e POSTGRES_DB=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres devdb