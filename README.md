# 205InstagramStreaming

-----------

## Description 

This project was made for CST 205: Multimedia Design and Programming, a class offered by the Computer Science Department of California State University, Monterey Bay.
This is the first realease (project 02), the final project can be found on this [repository](https://github.com/JonOikawa/205GlobalEvents)

The Team
-[Dario Molina] (https://www.linkedin.com/in/dario-molina?authType=NAME_SEARCH&authToken=sgHB&locale=pt_BR&trk=tyah&trkInfo=clickedVertical%3Amynetwork%2CclickedEntityId%3A444010483%2CauthType%3ANAME_SEARCH%2Cidx%3A1-1-1%2CtarId%3A1476842226114%2Ctas%3Adario%20mo) - Sentiment analysis, location detection, initial FaceBook work, second part of Twitter work
-[Jon Oikawa] (https://github.com/JonOikawa) - Initial Twitter work, integration of Twitter/Instagram, UI/UX, hosting, translating of Python to JavaScript
-[Igor Racca] (https://www.linkedin.com/in/igor-racca-87467a10a?trk=nav_responsive_tab_profile) - Sentiment analysis, location detection, all of Instagram work

-----------

**Instagram API**

https://www.instagram.com/developer/

**Tag Endpoints** 

https://www.instagram.com/developer/endpoints/tags/

**Location Endpoints**

https://www.instagram.com/developer/endpoints/locations/
(not implemented yet)

-----------

## Installation 

First make sure that you have installed: 

1.  [Node.js] (https://nodejs.org/en/download/) <br> 
2.  [Express.js] (https://expressjs.com/) <br> Assuming you've already installed Node.js, type: `npm install mongoose`
3.  [MongoDB] (https://www.mongodb.com/download-center#community) <br> 
4.  [Mongoose] (https://www.npmjs.com/package/mongoose) <br> Assuming you've already installed Node.js, type: `npm install mongoose` 

## Running the program

If you want to see the result in the terminal, you need to use this command on windows terminal to set the encoding to UTF-8:

- chcp 65001

Run it from command line with the following command:

- py instagram_streaming.py TRACK_TERM

It is currently set to run the stream while using the given TRACK_TERM. Certain keys have been selected to look for within the returned data structure. For best readability, pipe the results to a text file with a command similar to:

- py instagram_streaming.py trump > trump.txt

Use CTRL+C to exit.

## Current Issues
Attempting to print out emojis throws an error as there is no encoding for them the charmap of UTF-8.
