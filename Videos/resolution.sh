OIFS="$IFS"
IFS=$'\n'
for file in `find $1 -type f`
do
     echo "file = $file"
     ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 $file #|grep "3840x2160"
     # read line
done
IFS="$OIFS"