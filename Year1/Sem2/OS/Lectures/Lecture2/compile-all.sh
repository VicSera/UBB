#!/bin/bash

for F in *; do
	if file $F | grep -q "C source"; then
		gcc -Wall -g -o `echo $F | sed "s/\..*//"` $F
	fi
done
