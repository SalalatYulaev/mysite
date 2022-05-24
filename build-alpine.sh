#!/bin/bash
git pull
cd alpine
docker build -t alpine-test .