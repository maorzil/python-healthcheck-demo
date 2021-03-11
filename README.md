# Description
This is a simple python script that performs health-check on a given service-url every 5 seconds. 

# Prerequisites

- python 3.7.7
- docker
- docker-compose

# How To Run

1. Start nginx service using the provided docker-compose.yml file using the following command:
   `docker-compose up -d`
   you can verify that the service is up and running at the following url http://localhost:8080
2. Run the health-check script using the following command:
   `python3 healthcheck.py`
3. Stop the nginx service using the following command:
   `docker-compose down`
4. See the world burn

