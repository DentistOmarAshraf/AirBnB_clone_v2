#!/usr/bin/env bash
# Script to preapre nginx to serve web static

if ! command -v nginx >/dev/null 2>&1
then
	echo "Okey"
	apt update -y
	apt install nginx -y
fi

if [[ ! -d "/data/web_static/releases/test/" ]];then
	mkdir -p '/data/web_static/releses/test'
fi

if [[ ! -d "/data/web_static/shared" ]];then
	mkdir -p '/data/web_static/shared'
fi

Html='<html>
  <head>
  </head>
  <body>
    Holberton School
   </body>
</html>'

touch /data/web_static/releases/test/index.html
echo ${Html} >/data/web_static/releases/test/index.html

if [ ! -d "/data/web_static/current" ]
then
	ln -s /data/web_static/releases/test /data/web_static/current
fi

chown -R ubuntu:ubuntu /data/

to_rep='server_name _;'
rep="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tdefault_type text/html;\n\t}"

sed -i "s|${to_rep}|${to_rep}${rep}|" /etc/nginx/sites-available/default

service nginx restart
