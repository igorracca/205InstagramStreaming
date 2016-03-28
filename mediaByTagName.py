#
# Use this command on windows terminal to set the encoding to UTF-8:
# chcp 65001

import urllib.request
import json
import sys

tagname = sys.argv[1]
print("Tag name: " + tagname)

# open the output file in append mode
file = open('jsonOutput', 'a')

# Search for tags by name. It shows and counts similar tags. 'search?q={tag-name}'
# next_url = "https://api.instagram.com/v1/tags/search?q=" + tagname + "

# &access_token=145161542.1fb234f.afe13baad0e2403ea0a650b7aeacfe6b"

# Get a list of recently tagged media. 'tags/{tag-name}'
next_url = "https://api.instagram.com/v1/tags/" + tagname + "/media/recent?access_token=145161542.1fb234f.afe13baad0e2403ea0a650b7aeacfe6b"

while(1):
	response = urllib.request.urlopen(next_url)
	content = response.read()
	data = json.loads(content.decode("utf-8"))
	# get the next url request
	next_url = data['pagination']['next_url']
	# print(next_url)

	for i in range(0, 19):
		# get the type of the media to help to access json file
		mediaType = data['data'][i]['type'] + "s"
		# get the caption if its not null
		if data['data'][i].get('caption'):
			caption = str(data['data'][i]['caption']['text'])
		else:
			caption = "None"
		# get the location if its not null
		if data['data'][i].get('location'):
			location = "\n" 
			location += "\tName " + data['data'][i]['location']['name'] + " \n"
			location +=	"\tLocation_id " + str(data['data'][i]['location']['id']) + "\n"
			location +=	"\tLatitude " + str(data['data'][i]['location']['latitude']) + "\n"
			location +=	"\tLongitude " + str(data['data'][i]['location']['longitude']) + "\n"
		else:
			location = "None"
		# get the tags if its not null
		if len(data['data'][i]['tags']) > 0:
			tags = "\n"
			for tag in (data['data'][i]['tags']):		
				tags += "\t" + tag + "\n"
		else:
			tags = "None"
		# get the likes if its not null
		if data['data'][i]['likes']['count'] > 0:
			likes = "\n"
			for user in (data['data'][i]['likes']['data']):		
				likes += "\tUsername :" + user['username'] + "\n"
				likes += "\tProfile Picture: " + user['profile_picture'] + "\n"
		else:
			likes = "None"
		# get the comments if its not null
		if data['data'][i]['comments']['count'] > 0:
			comments = "\n"
			for user in (data['data'][i]['comments']['data']):		
				comments += "\tUsername :" + user['from']['username'] + "\n"
				comments += "\tProfile Picture: " + user['from']['profile_picture'] + "\n"
				comments += "\tComment: " + user['text'] + "\n"
		else:
			comments = "None"

		output = "\n" 
		output += "Link: " + data['data'][i]['link'] + "\n"
		output += "Username: " + data['data'][i]['user']['username'] + "\n"
		output += "Full Name: " + data['data'][i]['user']['full_name'] + "\n"
		output += "Profile_picture: " + data['data'][i]['user']['profile_picture'] + "\n"
		output += "Media Type: " + data['data'][i]['type'] + "\n"
		output += "Media Url: " + data['data'][i][mediaType]['standard_resolution']['url'] + "\n"
		output += "Caption: " + caption + "\n"
		output += "Location: " + location + "\n"
		output += "Tags: " +  tags + "\n"
		output += "Likes: " + likes + "\n"
		output += "Comments: " + comments + "\n"

		print(output)

		# append media json in the output file
		# file.write(json.dumps(output))
		# file.write("\n\n")

file.close(output)