docker build -t neonews .

docker run -d -p 8000:8000 neonews

docker logs -f <container_id>
