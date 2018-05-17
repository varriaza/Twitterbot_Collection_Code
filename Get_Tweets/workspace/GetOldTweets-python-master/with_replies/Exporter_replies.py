# -*- coding: utf-8 -*-
import sys,getopt,datetime,codecs
import os
if sys.version_info[0] < 3:
	# ********* CHANGE GOT NAME HERE ********* 1/4
    import got_replies
else:
    import got3 as got

def main(argv):
	# print 
	#print("here")
	
	if len(argv) == 0:
		print('You must pass some parameters. Use \"-h\" to help.')
		return

	if len(argv) == 1 and argv[0] == '-h':
		f = open('exporter_help_text.txt', 'r')
		print f.read()
		f.close()

		return

	try:
		opts, args = getopt.getopt(argv, "", ("username=", "near=", "within=", "since=", "until=", "querysearch=", "toptweets", "maxtweets=", "output="))
		
		# print 
		#print("here2")

		# ********* CHANGE GOT NAME HERE ********* 2/4
		tweetCriteria = got_replies.manager.TweetCriteria()
		outputFileName = "output_got.csv"
		
		# print 
		#print("here3")

		for opt,arg in opts:
			if opt == '--username':
				tweetCriteria.username = arg
				outputFileName = arg + ".csv" #changed for our needs: output name is username

			elif opt == '--since':
				tweetCriteria.since = arg

			elif opt == '--until':
				tweetCriteria.until = arg

			elif opt == '--querysearch':
				tweetCriteria.querySearch = arg
				outputFileName = arg + ".csv" #changed for our needs: output name is username

			elif opt == '--toptweets':
				tweetCriteria.topTweets = True

			elif opt == '--maxtweets':
				tweetCriteria.maxTweets = int(arg)
			
			elif opt == '--near':
				tweetCriteria.near = '"' + arg + '"'
			
			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--output':
				outputFileName = arg
		
		# ********* CHANGE DATA FOLDER HERE ********* 3/4
		os.chdir("/home/ubuntu/workspace/data/replies_data/")		
		outputFile = codecs.open(outputFileName, "w+", "utf-8")

		outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink;replyTo')

		print('Searching...\n')

		def receiveBuffer(tweets):
			for t in tweets:
				outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s;%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink, t.replyTo)))
			outputFile.flush()
			print('More %d saved on file...\n' % len(tweets))
		
		# print 	
		#print("here4")	

		# ********* CHANGE GOT NAME HERE ********* 4/4
		got_replies.manager.TweetManager_replies.getTweets(tweetCriteria, receiveBuffer)
		
		# If you change the TweetManager file do the following
		# 1) change models/__init__.py to have new TweetManager file name
		# 2) change models/__init__.py to have new class name
		# 3) Make sure functions in TweetManager use new class name
		
		# print 
		#print("Here5")

	except arg:
		print('Arguments parser error, try -h' + arg)
	finally:
		outputFile.close()
		print('Done. Output file generated "%s".' % outputFileName)

if __name__ == '__main__':
	main(sys.argv[1:])
