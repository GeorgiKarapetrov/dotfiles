#!/bin/bash

ORPHANS=`deborphan`
if [ ! -z "$ORPHANS" ]; then
    dpkg --remove $ORPHANS
fi

PURGES=`dpkg --list | grep ^rc | awk '{ print $2; }'`
if [ ! -z "$PURGES" ]; then
    dpkg --purge $PURGES
fi
