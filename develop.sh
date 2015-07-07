#!/bin/bash

rm -rf ~/pelican/output &&pelican content --relative-urls --ignore-cache
