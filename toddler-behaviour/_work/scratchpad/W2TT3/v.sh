grep -v '^MATCHES' $1 | grep -v '^$' | sed 's/^OPENING: //' | awk '/^ID/{split($0,a," ");printf "\n%s ",a[2];next}{printf "%s ",$0}' | sed 's/TITLE: /| /'
