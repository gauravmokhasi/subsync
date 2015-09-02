subsync
=======

Subsync is a super-easy way to help sync the timing between videos and their .srt files.

Written in Python, subsync works when there is a fixed delay throughout the video. All the user has to do is figure out the delay once and then use subsync to fix it forever. Contrast this to the normal scenario in which the user has to press G or H to figure out and fix the delay each time he opens the video.

Instructions of use:
- Have Python 2.7 installed on your computer.
- Place subsync.py in the same directory as the .srt file.
- Run subsync.py and type out the name of the file whose timing you want to fix.
- Enter the value of delay (can be negative as well).
- Hit enter. The existing file gets overwritten with the fixed timing.
