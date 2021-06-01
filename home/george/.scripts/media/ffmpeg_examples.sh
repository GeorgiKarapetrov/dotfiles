#!/bin/bash

ffmpeg \
	-f x11grab \
	-s "$(xdpyinfo | grep dimensions | awk '{print $2;}')" \
	-i "$DISPLAY" \
 	-c:v x265 -qp 0 -r 30 \
	"$HOME/video-$(date '+%y%m%d-%H%M-%S').mkv"

ffmpeg -ss 00:00:40.300 -i z1.mp4 -vframes 1 -q:v 2 out.jpg

ffmpeg -i test.mp4 -ss 00:00:01.300 -async 1 -to 00:00:52 z.mp4

ffmpeg -f pulse -i default <name>.wav

ffmpeg -f pulse -i default -async 1 -codec:a libmp3lame -qscale:a 2 name.mp3

fmpeg -i SoundTrack.mp3 -ss 00:03:48 -t 00:04:28 02-\#34.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 03-Working\'G.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 04-San\ Francisko.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 05-Lifestyles.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 06-Jay\'s\ hole.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 07-Wrong.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 08-G.O.Light.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 09-Brightest\ Light.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 10-Women\ bleed.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 11-Trippin\' colors.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 12-Orient\ mucho.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 13-Horror\ IV.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 14-Smokin\'G.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 15-Prepodavam.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 -t 00:03:48 16-Brother\ Sun.mp3 && \
fmpeg -i SoundTrack.mp3 -ss 00:00:00 17-Where\ we\'re\ from.mp3 && \

ffmpeg -i Input -c:v libx265 -an -b:v 4M -maxrate 4M -bufsize 2M output.mkv
ffmpeg -i Input -c:v libx265 -crf 28 out.mkv