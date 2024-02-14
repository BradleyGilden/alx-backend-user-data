#!/usr/bin/env bash

curl "http://0.0.0.0:5000"
curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
curl "http://0.0.0.0:5000" --cookie "_my_session_id=C is fun"
curl "http://0.0.0.0:5000" --cookie "_my_session_id_fake"
