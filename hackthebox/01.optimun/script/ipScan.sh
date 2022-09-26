#!/bin/bash

for i in  $(seq 1 255); do 
	timeout	1 bash -c "ping -c 1 10.10.10.$i" 2>/dev/null && echo -e "10.10.10.$i - Active" &
done; wait
