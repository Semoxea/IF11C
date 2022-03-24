---
layout: default
title: "ITS-Praxis - Routing"
permalink: /ITSPraxis/Routing
---

### Netzplan

|Gerät/Schnittstelle|IP-Adresse|Netzmaske|Gateway|
|--|--|--|--|
|PC-Verkauf|192.168.1.1|/24|192.168.1.251|
|Router-en1_0, Eth|192.168.0.251|/24|Provider|
|Router-en1_1, Eth|192.168.1.251|/24|Provider|
|PC-Werkstatt|192.168.0.1|/24|192.168.0.251|

### Routingtabelle

|Ziel-IP-Adresse|Netzmaske|Gateway|Schnittstelle|Metrik|
|--|--|--|--|--|
|192.168.1.0|/24|192.168.1.251|eth_1|0|
|192.168.0.0|/24|192.168.0.251|eth_0|0|
