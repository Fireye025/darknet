#!/bin/bash
while read p;do
	python3 joinImage.py "$p" 
done <file.list


