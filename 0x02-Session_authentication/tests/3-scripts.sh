#!/usr/bin/env bash

curl "http://0.0.0.0:5000/api/v1/status"
curl "http://0.0.0.0:5000/api/v1/auth_session/login" # not found but not "blocked" by an authentication system
curl "http://0.0.0.0:5000/api/v1/users/me"
curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh" # Won't work because the environment variable AUTH_TYPE is equal to "session_auth"
curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76" # Won't work because no user is linked to this Session ID
