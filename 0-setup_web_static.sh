#!/usr/bin/env bash
# Script to preapre nginx to serve web static

if ! command -v nginx >/dev/null 2>&1
then
	echo "Okey"
	apt update -y
	apt install nginx -y
fi

if [[ -d "/data/web_static/releases/test/" ]];then
	mkdir -p '/data/web_static/releses/test'

if [[ -d "/data/web_static/shared" ]];then
	mkdir -p '/data/web_static/shared'

Html='<html>
  <head>
  </head>
  <body>
    Holberton School
   </body>
</html>'

echo ${Html} >/data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/

to_rep='server_name _;'
rep='\tlocation /hbnb_static {
		alias /data/web_static/current/;
		default_type text/html;
	}'

sed -i "s|${to_rep}|${to_rep}${rep}|" /etc/nginx/sites-avalibale/default
service nginx restart