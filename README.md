### Prerequisites

You need to install Docker on your system. You can install Docker by going to this url
https://docs.docker.com/install/

### Installing

You need to clone this repo to any path at your local machine

```
git clone https://github.com/moryachok/elasticstack-lab.git
```

Now run docker-compose in order to build the stack. On first build it may take some time to get all the required images.

```
cd elasticstack-lab/
docker-compose up
```

You can optionally run docker-compose in detached mode

```
docker-compose up -d
```

After build process finishes you will be able to enter Kibana dashboard and see there some sample data

## Enter Kibana

Now open your browser and navigate to http://127.0.0.1:5601
You should see fresh Kibana dashboard.
It will ask you to configure your first index.


