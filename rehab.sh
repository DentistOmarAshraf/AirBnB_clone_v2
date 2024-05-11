#!/usr/bin/env bash

sed -i '/location \/hbnb_static {/,/}/d' /etc/nginx/sites-available/default
