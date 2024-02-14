#!/usr/bin/env bash

curl "http://0.0.0.0:5000/"
curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
curl "http://0.0.0.0:5000/" --cookie "_my_session_id=7da6ddf4-7815-4f1d-8539-94b20f132f00"
