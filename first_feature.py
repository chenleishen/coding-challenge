import json

#first feature
tweets = open('./tweet_input/tweets.txt', 'r')
ft = open('./tweet_output/ft1.txt', 'w')
num_of_unicode = 0

for line in tweets:
	tweet_obj = json.loads(line)
	text = tweet_obj['text']
	timestamp = tweet_obj['created_at']
	unicode_removed = text.encode('ascii','ignore')
	if unicode_removed != text:
		num_of_unicode += 1
	ft.write(unicode_removed + "  (timestamp: " + timestamp + ") \n")

ft.write("\n" + str(num_of_unicode) + " tweets contained unicode. \n" )

ft.close()



