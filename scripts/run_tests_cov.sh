#!/bin/bash

cd ..
coverage run -m pytest
coverage report
