#!/bin/sh

awk -F: '{ split($5,a," "); if(a[1]) print a[1] }' /etc/passwd | sort | uniq -c | sort -k1n
