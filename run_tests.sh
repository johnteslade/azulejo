#!/bin/sh

py.test -v --cov=azulejo --cov-report=term-missing azulejo/ azulejo/geometry.py
