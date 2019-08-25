#!/bin/bash

echo "Record lossless audio for further processing."
echo "Created file name always starts with temp_YYYYMMDD_HHMMSS."
echo "Syntax:"
echo "myrec-novideo [optional file description]"
echo "Optional file description is appended to the file name, with spaces replaced by underscores."
echo
echo


### User settings - adjust values to suit your system

# I used to have the name of my webcam mic here, but that stopped working after a system update. "default" was the only fix I found. If you have more than one microphone connected, you may need to tell Pulseaudio which mic you want to be the default, I think pavucontrol is the utility for it.
# If you want to try supplying a name here, run pacmd, then within it the command list-sources will give you a list of possible microphones. Use the name field value without angle brackets.
microphone_audio_device="default"

# Run pacmd, within it the command list-sinks will give you a list of devices to choose from. Use the name field value without angle brackets.
speakers_audio_device="alsa_output.pci-0000_00_1b.0.analog-stereo.monitor"

# Include the trailing slash after target directory name.
# Expect a large file!
target_directory="/target/directory/name/"

### End of user settings



record_command="ffmpeg -f pulse -thread_queue_size 512k -i $speakers_audio_device -f pulse -thread_queue_size 512k -i $microphone_audio_device -map 0 -map 1 -codec:a copy -codec:a copy"
temporary_file_prefix="temp_"

# The IFS (Internal Field Separator) system variable stores the character that separates command line arguments.
# We can use it to replace spaces with underscores.
temp=$IFS
IFS='_'
description="$*"
IFS=$temp

if [ $# -eq 0 ]; then
  $record_command $target_directory$temporary_file_prefix`date +%Y%m%d_%H%M%S`.mkv
else
  $record_command $target_directory$temporary_file_prefix`date +%Y%m%d_%H%M%S`_$description.mkv
fi
