#!/bin/bash

ffmpeg -i SoundTrack.mp3 -y -t 00:03:48 01-Blue\ Cartoon.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:03:49 -t 00:04:28 02-\#34.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:08:18 -t 00:05:23 03-Working\'G.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:13:44 -t 00:03:22 04-San\ Francisko.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:17:07 -t 00:03:59 05-Lifestyles.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:21:07 -t 00:03:44 06-Jay\'s\ hole.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:24:52 -t 00:06:22 07-Wrong.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:31:19 -t 00:03:44 08-G.O.Light.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:35:04 -t 00:04:44 09-Brightest\ Light.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:39:50 -t 00:05:39 10-Women\ bleed.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:45:33 -t 00:05:50 11-Trippin\' colors.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:51:24 -t 00:05:50 12-Orient\ mucho.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 00:55:23 -t 00:05:15 13-Horror\ IV.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 01:00:42 -t 00:04:30 14-Smokin\'G.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 01:05:13 -t 00:04:10 15-Prepodavam.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 01:09:25 -t 00:03:10 16-Brother\ Sun.mp3 &
ffmpeg -i SoundTrack.mp3 -y -ss 01:12:35 -t 00:01:30 17-Where\ we\'re\ from.mp3

exit 0