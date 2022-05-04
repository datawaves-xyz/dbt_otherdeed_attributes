#!/bin/bash

for i in 0 1 2 3 4 5 6 7 8 9
do
    python collect_lands.py "$((i*10000))" "$(((i+1)*10000))" &
done