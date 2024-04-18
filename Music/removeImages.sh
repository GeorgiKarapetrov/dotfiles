#!/bin/bash

# find . -type f -print0 |
#     xargs -0 file --mime-type |
#     awk -F: '{if ($2 ~/image\//) print $1}'

# find . -type f -print0 |
#     xargs -0 file --mime-type |
#     awk -F: '{if ($2 ~ /video\// && $1 !~ /m4a/ && $1 !~ /wma/ ) print $1}'

find . -type f \( -iname \*jpg -o -iname \*png -o -iname \*bmp \) -delete
