#!/bin/sh
# syntax: setperm.s destdir
#
if [ -z $1 ] ; then echo "Requires single argument: <directoryname>" ; exit 1 ;                                       fi

destdir=$1

dirmode=0770
filemode=0744

YN=no

printf "\nThis will RECURSIVELY change the permissions for this entire branch:\n                                      "
printf "\t$destdir\n"
printf "\tDirectories chmod = $dirmode\tFiles chmod = $filemode\n"
printf "Are you sure want to do this [$YN]? "

read YN

case $YN in
        [yY]|[yY][eE][sS])
        # change permissions on files and directories.
        find $destdir -type f -print0 | xargs -0 chmod $filemode $i
        find $destdir -type d -print0 | xargs -0 chmod $dirmode $ii ;;

        *) echo "Better safe than sorry I always say." ;;
esac
