#!/bin/bash
mkdir croped
find *.jpg > tmpF.txt
while read p;do
	python3 cropImage.py "$p" 
done <tmpF.txt
rm tmpF.txt
cd croped 
mkdir croped
find *.jpg > tmpF.txt
while read p; do
	python3 ../cropImage.py "$p"
done <tmpF.txt
rm tmpF.txt






