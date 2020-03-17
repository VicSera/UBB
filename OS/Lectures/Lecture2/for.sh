#!/bin/bash

#for A in a b c d e; do
#	echo $A
#done

for F in `find ../..`; do
	test -f $F && wc -l $F
done
