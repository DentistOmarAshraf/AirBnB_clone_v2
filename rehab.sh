#!/usr/bin/env bash

rep="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tdefault_type text/html;\n\t}"
del=""
sed -i "s|${rep}|${del}|" /etc/nginx/sites-available/default 
