# ZooKeeper Consul Docker

ZooKeeper coordinated using Consul…

## Building

```sh
docker build --tag=lxcid/zookeeper-consul .
docker push lxcid/zookeeper-consul
```

## Why Python?

We could write zkGenServers.py as a Java program but Java isn't the nicest language to write DevOps scripts in.
We could also write in languages like Go/Swift/Rust that compile down to a nice binary that doesn't need much dependency.
We'll leave this for future exercise.

## How-to restart?

Currently you need to manual restart the container to load configurations changes…

```sh
# Consul-template should be running as PID 1
kill -HUP 1
```
