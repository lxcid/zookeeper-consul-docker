#! /usr/bin/env python

import argparse
import json
import os
import re
import requests

def myid(node):
    if 'ServiceTags' not in node:
        return None
    r = re.compile('^myid=(\d+)$')
    res = list(filter(r.match, node['ServiceTags']))
    if len(res) == 0:
        return None
    return r.search(res[0]).group(1)

def has_myid(node):
    return not myid(node) is None

def is_valid_zookeeper(zookeeper):
    return (
        'ID' in zookeeper
        and
        'Address' in zookeeper
        and
        'ClientPort' in zookeeper
        and
        'ServerPort' in zookeeper
        and
        'ElectionPort' in zookeeper
    )

parser = argparse.ArgumentParser(description='Generates ZooKeeper\'s servers configuration by querying Consul.')
parser.add_argument('myid', help='myid')

args = parser.parse_args()

consul_http_addr = os.getenv('CONSUL_HTTP_ADDR', 'consul:8500')
r = requests.get(f"http://{consul_http_addr}/v1/catalog/service/zookeeper-2181")
res = r.json()
if len(res) == 0:
    print('[]')
    exit(0)

zookeepers = {}

for node in filter(has_myid, res):
    id = myid(node)
    zookeepers[id] = {
        'ID': id,
        'Address': '0.0.0.0' if id == args.myid else node['ServiceAddress'],
        'ClientPort': os.getenv('ZOO_PORT', '2181') if id == args.myid else node['ServicePort'],
    }

r = requests.get(f"http://{consul_http_addr}/v1/catalog/service/zookeeper-2888")
res = r.json()
for node in filter(has_myid, res):
    id = myid(node)
    if id not in zookeepers:
        continue
    zookeepers[id]['ServerPort'] = '2888' if id == args.myid else node['ServicePort']

r = requests.get(f"http://{consul_http_addr}/v1/catalog/service/zookeeper-3888")
res = r.json()
for node in filter(has_myid, res):
    id = myid(node)
    if id not in zookeepers:
        continue
    zookeepers[id]['ElectionPort'] = '3888' if id == args.myid else node['ServicePort']

valid_zookeepers = list(filter(is_valid_zookeeper, zookeepers.values()))

print(json.dumps(valid_zookeepers))
exit(0)
