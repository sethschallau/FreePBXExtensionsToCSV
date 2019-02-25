A quick and dirty 'script' to pull from a freePBX config file for extensions
This took the essential stuff for new extensions in other PBX systems.
Written before I knew what REGEX was, and how to implement it for something like this.

py2 and 3 versions because newer freePBX servers ran 3, but the majority ran 2.

This was a very quick "proof of concept" piece that was/is implemented further by full time developers.
 

From my original info on what I wrote:
"File must be run in the / directory.
It pulls from the sip_additional.conf file that FreePBX stores its extension information in.
Outputs a .csv file that can be used with the QuBe bulk configuration upload."
