import json

#first feature
tweets = open('./tweet_input/tweets.txt', 'r')
# ft = open('./tweet_output/ft1.txt', 'w')
# num_of_unicode = 0

# for line in tweets:
# 	tweet_obj = json.loads(line)
# 	text = tweet_obj['text']
# 	timestamp = tweet_obj['created_at']
# 	unicode_removed = text.encode('ascii','ignore')
# 	if unicode_removed != text:
# 		num_of_unicode += 1
# 	ft.write(unicode_removed + "  (timestamp: " + timestamp + ") \n")

# ft.write("\n" + str(num_of_unicode) + " tweets contained unicode. \n" )

# ft.close()

#second feature
ft2 = open('./tweet_output/ft2.txt', 'w')
graph = {}

def attachNode(graph, tag, hashtags):
	if tag not in graph:
		graph[tag] = []

	for other_tag in hashtags:
		if other_tag != tag and other_tag not in graph[tag]:
			graph[tag].append(other_tag)

def calculateDegrees(graph):
	tot_connections = 0
	for node, connections in graph.iteritems():
		tot_connections += len(connections)

	return tot_connections/len(graph)

for line in tweets:
	tweet_obj = json.loads(line)
	hashtags = tweet_obj['entities']['hashtags']
	# print tweet_obj['text']
	# print tweet_obj['entities']['hashtags']
	if len(hashtags) > 1:
		for tag in hashtags:
			attachNode(graph, tag['text'], hashtags)
	degrees = calculateDegrees(graph)
	ft2.write(str(degrees) + "\n")



