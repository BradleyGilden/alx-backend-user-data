#!/usr/bin/env bash

curl "http://0.0.0.0:5000/api/v1/status"
curl "http://0.0.0.0:5000/api/v1/status/"
curl "http://0.0.0.0:5000/api/v1/users"
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
