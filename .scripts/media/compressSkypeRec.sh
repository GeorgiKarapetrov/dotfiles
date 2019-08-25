#!/bin/bash

echo "Compress files recorded with myrec or myrec-novideo."
echo "For files to be processed they need to reside in the storage directory and start with temp_"
echo "The two audio tracks (mic and speakers) are mixed together into one new stream, but they are also available as separate tracks in the final file."

# Mixing is because players I know cannot play two audio tracks from the same file simultaneously.
# The mic also captures sounds produced by the speakers. It has two effects:
# 1. You can use this single track to hear both yourself (the mic) and whatever came out of your speakers. Personally I did not like the degraded quality of recorded speaker sounds, hence the direct recording off the sound card and mixing that with the mic track.
# 2. Speaker sounds recorded by the mic are slightly delayed when compared to the direct recording off the sound card. The mixed track is thus hard to listen to.
# I do have echo cancellation module loaded in Pulseaudio, perhaps there is something wrong with my configuration?

### User settings

# Indicate storage directory without the trailing slash
storage_directory="/storage/directory/name"

### End of user settings

# Any temp_ file may contain 3 streams (audio, audio, video) indexed as (0, 1, 2), or just 2 streams (audio, audio) indexed as (0, 1).
# A file temp2_ contains just one stream: both audio streams from temp_ mixed.
# The step with temp2_ is necessary as the mixing option (-filter_complex) is a global option (i.e. not stream-specific). Attempts at doing it all in one go prevent the separate tracks from being copied into the final file.

for f in $storage_directory/temp_*
do
  if [ -e ${f/temp_/} ]
  then
    # Do not overwrite an existing final file. Prevents unnecessary work when the script is run regularly as a cron job.
    echo "$f: A final file (without temp_) already exists. Skipping. If you want to reencode, please delete the final file manually."
  else
    # Variable g will contain the name of the second temporary file with both audio streams mixed into one.
    g=${f/temp_/temp2_}

    # Mixing mic and sound card tracks into one stream
    ffmpeg -i "$f" -map 0:0 -map 0:1 -filter_complex amix=inputs=2:duration=longest:dropout_transition=2 -codec:a libvorbis -n "$g"

    # Create the final file: copy the mixed audio stream from temp2_, add and compress both separate audio streams from temp_, compress at high quality the video stream from temp_.
    # The question mark in -map 0:2? tells ffmpeg to ignore the error if this stream (video) is missing. Allows this same script to be used for audio-only recordings.
    ffmpeg -i "$f" -i "$g" -map 1:0 -map 0:0 -map 0:1 -map 0:2? -codec:a:0 copy -codec:a:1 libvorbis -codec:a:2 libvorbis -codec:v libx264 -qp 18 -preset slow -threads 0 -n "${g/temp2_/}"

    # Delete temp2_
    rm "$g"
  fi
done
