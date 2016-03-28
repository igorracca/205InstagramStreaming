# 205InstagramStreaming

# Instagram API

https://www.instagram.com/developer/

**Tag Endpoints** 

https://www.instagram.com/developer/endpoints/tags/

**Location Endpoints**

https://www.instagram.com/developer/endpoints/locations/
(not implemented yet)

# Running the program

**If you want to see the result in the terminal, you need to use this command on windows terminal to set the encoding to UTF-8:**

chcp 65001


Run it from command line with the following command:

py instagram_streaming.py TRACK_TERM


It is currently set to run the stream while using the given TRACK_TERM. Certain keys have been selected to look for within the returned data structure. For best readability, pipe the results to a text file with a command similar to:

py instagram_streaming.py trump > trump.txt

Use CTRL+C to exit.

# Current Issues
Attempting to print out emojis throws an error as there is no encoding for them the charmap of UTF-8.
