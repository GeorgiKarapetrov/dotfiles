#!/usr/bin/bash
sudo create_ap wlp13s0 enp14s0 pc 1234567899 && expect "[sudo"
send -- "1a"

