
#! /bin/bash
salt1="soMe3FK2J+YFAMzUjwpfpA"
salt2="6dcKXY3x/JRZbyj9RDB/Lw"
i=0
cat "$@" | while read -r line; do

printf %s "$salt1$line$salt2" | md5sum | cut -f1 -d' ' >>hashes.txt
done
echo "DONE"

