#!/bin/sh
coverage run --branch --include="*feincms_banners*" ./manage.py test testapp
coverage html
