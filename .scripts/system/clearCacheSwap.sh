#!/bin/bash

#Clear PageCache only
# sync; echo 1 > /proc/sys/vm/drop_caches

#Clear dentries and inodes.
# sync; echo 2 > /proc/sys/vm/drop_caches

#Clear Both. Note, we are using "echo 3", but it is not recommended in production instead use "echo 1"
sync; echo 3 > /proc/sys/vm/drop_caches && swapoff -a && swapon -a
