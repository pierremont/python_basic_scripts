#! /bin/python

testfile = "e:/petrus/VAS/howto_technology/devops/python/testfile2.txt"

import re
import sys

file = open(testfile, "r")
ignore_error = "voiceglue httpcache: failure from exec of \"voiceglue_tts_gen -t A serious error has occured.  Exiting. /home/radcom/mediaserver/asterisk/var/lib/asterisk/sounds/voiceglue/tts/nKspH8NWoqCQHdnUbRbm-0c3qQUwqMXJ5_A_serious_error_has_occured___Ex.wav en\": No such file or directory"

for line in file:
     if re.search(ignore_error, line):
         print line,
         #file.close()
         #file = open(testfile, "w")
         #file.write("")
         #file.close()