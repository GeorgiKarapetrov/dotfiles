#!/bin/bash

SRC="$HOME/dotfiles"
DEST="$HOME"

#mkdir -p $DEST 

#symlink all files (and folders), exluding important existing folders (Documents and .config)
#this will delete existing folders
for f in $(ls -a $SRC/); do
	if [[ ( ! $f =~ Documents|.config|.git*|README.md|install.sh|.|.. ) && ( -e $f ) ]]; then
		if [[ -d $f ]]; then
			sudo rm -rf $DEST/$f/
		elif [[ -f $f ]]; then
			sudo rm $DEST/$f
		fi
		sudo ln -sf "$SRC/$f" "$DEST/$f"
		#echo $SRC/$f
		#echo $DEST/$f
	fi
done

#override ~/.config
for f in $(ls -a $SRC/.config/); do
	sudo rm -rf $DEST/.config/$f/
	sudo ln -sf "$SRC/.config/$f" "$DEST/.config/$f"
	#echo $SRC/.config/$f
	#echo $DEST/.config/
done

echo ''
echo "Don't forget to import tixati setting, firefox bookmarks"
echo "and to check Documents/programming"


### recusively symlink each file in the file tree

## 1 - recreate SRC directory tree as DEST
#find $SRC -type d |while read PATHNAME; do 
#    sudo mkdir -p "$DEST${PATHNAME#$SRC}" ; 
#done

## 2 - create a a symlink under $DEST for each file under $SRC
#find $SRC -type f |while read PATHNAME; do 
#        NEW="$DEST${PATHNAME#$SRC}" ; 
#        echo "$NEW" ; 
#        sudo ln -sf "$PATHNAME" "$NEW" ; 
#done

