#!/bin/sh

# NF - number of fields
# NR - line number

# BEGIN{} & END{} - executed once

#awk -F: '{ split($5,arr," "); if (length(arr)>0) print arr[1] }' /etc/passwd 

# gsub
#awk -F: '{ if(index($5,"A")==1) print $0 }' /etc/passwd

echo "arguments: $#"

for a in $@
do
	echo $a
done

cat /etc/passwd | while read l
do
	echo "line: $l"
done
