#!/bin/sh

i=0
while read -r f; do
    i=$((i + 1))
	[ -d "$f" ] && continue
	printf "\n=== %d. %s ===\n" "$i" "${f##*/}"
	awk '
		/pr = \[/ { flag=1; next }
		/^\]/     { flag=0 } flag
	' "$f"
	grep -oP '^cl0 = \K.*' "$f"
done
