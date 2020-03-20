#!/bin/bash

rsync -av --exclude=.git --exclude=venv --exclude=data . ec1:/db/corona-au/
