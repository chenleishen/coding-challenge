import json

#second feature
tweets = open('./tweet_input/tweets.txt', 'r')
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

ft2.close()