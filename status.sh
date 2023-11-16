#!/bin/sh

theorem() {
	i=0
	while read -r f; do
		i=$((i + 1))
		[ -d "$f" ] && continue
		printf "\n=== %d. %s ===\n" "$i" "${f##*/}"
		awk '
			/pr = \[/ { flag=1; next }
			/^\]/     { flag=0 } flag
		' "$f"
		grepdef cl0 "$f"
	done
}

parse() {
	f="$1"
	[ -d "$f" ] && return
	echo "title = " "${f##*/}"
	awk '
		BEGIN { pr_count=1 }
		/pr = \[/ { flag=1; next }
		/^\]/     { flag=0 } flag {
			gsub(/^[[:blank:]]+/, "");
			gsub(/,$/, "");
			printf "pr%d = %s\n", pr_count, $0
			++pr_count;
		}
	' "$f"
	grepdef 'cl' "$f"
	grepdef 'if' "$f"
	grepdef 'st' "$f"
}

grepdef() {
	grep -s '^[[:space:]]*'"$1"'.*=' "$2"
}

case $1 in
	cat)
		shift
		if [ -z "$1" ]; then
			theorem
		else
			echo "$1" | theorem
		fi
		;;
	ls)
		shift
		find "$1" -type f | theorem
		;;
	p)
		shift
		parse "$1"
		;;
	*)
		cat << EOF
Barhana helper script
./status.sh ls <DIRECTORY>
./status.sh cat <THEOREM_FILE.py>
EOF
		;;
esac
