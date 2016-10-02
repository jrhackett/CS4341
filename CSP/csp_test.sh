#!/bin/bash

clear

for i in `seq 1 25`;
do
	python main.py tests/input$i.txt > outputs/output$i.txt && echo "success for $i" || echo "\tfailure for $i"
done
