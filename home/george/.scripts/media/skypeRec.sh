#!/bin/bash

echo "Record lossless audio and lossless video for further processing."
echo "Created file name always starts with temp_YYYYMMDD_HHMMSS."
echo "Syntax:"
echo "myrec [optional file description]"
echo "Optional file description is appended to the file name, with spaces replaced by underscores."
echo
echo

### User settings - adjust values to suit your system and needs

# I used to have the name of my webcam mic here, but that stopped working after a system update. "default" was the only fix I found. If you have more than one microphone connected, you may need to tell Pulseaudio which mic you want to be the default, I think pavucontrol is the utility for it.
# If you want to try supplying a name here, run pacmd, then within it the command list-sources will give you a list of possible microphones. Use the name field value without angle brackets.
microphone_audio_device="default"

# Run pacmd, within it the command list-sinks will give you a list of devices to choose from. Use the name field value without angle brackets.
speakers_audio_device="alsa_output.pci-0000_00_1b.0.analog-stereo.monitor"

# Select frame size.
# Some standard frame sizes for reference:
# wvga 852x480
# wxga 1366x768
# wsxga 1600x1024
# wuxga 1920x1200
# woxga 2560x1600
# wqsxga 3200x2048
# wquxga 3840x2400
# whsxga 6400x4096
# whuxga 7680x4800
frame_size="wxga"

# Framerate in frames per second
framerate="30"

# Indicate which screen the video should be recorded from and an optional offset.
# For example:
# :0.0+10,20
# where 0.0 is display.screen number of your X11 server, same as the DISPLAY environment variable. 10 is the x-offset and 20 the y-offset of the frame, measured from the top left corner of the screen to the top left corner of the frame.
frame_position=":0.0"

# Include the trailing slash after target directory name.
# Expect a very large file!
target_directory="~/Desktop/"

### End of user settings



record_command="ffmpeg -f pulse -thread_queue_size 512k -i $speakers_audio_device -f pulse -thread_queue_size 512k -i $microphone_audio_device -f x11grab -s $frame_size -r $framerate -thread_queue_size 512k -i $frame_position -map 0 -map 1 -map 2 -codec:a copy -codec:v libx264 -qp 0 -preset ultrafast"
temporary_file_prefix="sky_"

# The IFS (Internal Field Separator) system variable stores the character that separates command line arguments.
# We can use it to replace spaces with underscores.
temp=$IFS
IFS='_'
description="$*"
IFS=$temp

if [ $# -eq 0 ]; then
  $record_command $target_directory$temporary_file_prefix`date +%Y%m%d_%H-%Mh`.mkv
else
  $record_command $target_directory$temporary_file_prefix`date +%Y%m%d_%H-%Mh`_$description.mkv
fi
