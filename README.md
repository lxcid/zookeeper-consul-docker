# ZooKeeper Consul

ZooKeeper with Consul installed…


```sh
docker build --tag=lxcid/zookeeper-consul .
docker push lxcid/zookeeper-consul
```

Currently you need to manual restart the container to load new configurations.

```sh
kill -HUP 1
```
