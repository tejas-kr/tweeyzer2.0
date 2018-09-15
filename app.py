import tweepy
from textblob import TextBlob
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = "matkarohack"


@app.route('/')
def index():
	return render_template('tweets.html')

@app.route('/tweets', methods=['GET'])
def tweets():
	subject = request.args.get('subject')
	# count = request.form['count']

				###########################################

	consumer_key = 'pkYGwYHQIahocFIhItwvbWepu'
	consumer_secret = 'reyuBcw0xYdJS9FdFnf6hiPckEtTacL8kFI1VQJV1eBPWsKQGn'
	access_token = '775384841185554432-Lt4cvgf2jWV36kwnQ4yBHPp6FH9hsXI'
	access_token_secret = 'WeFAYRKFvSonhmt8RHhDR8SnnKuH9BynFp9Eeer0oW9MH'
	
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
	except:
		return render_template("authentication_error.html")
	finally:
		api = tweepy.API(auth)

	def get_senti(txt):
		textBlob = TextBlob(txt)
		if textBlob.sentiment.polarity > 0:
			return 'positive'
		elif textBlob.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def get_tweets(subject):
		tweets = []
		try:
			fetched_tweets = api.search(q = subject, lang='en')
			for tweet in fetched_tweets:
				parsed_tweet = {}
				parsed_tweet['text'] = tweet.text
				parsed_tweet['sentiment'] = get_senti(tweet.text)
				if tweet.retweet_count > 50:
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
			return tweets
		except:
			return render_template('not_found.html')
	
	tweets = get_tweets(subject)
	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

	num_ptweets = (len(ptweets)/len(tweets)) * 100
	num_neutweets = (len(neutweets)/len(tweets)) * 100
	num_ntweets = (len(ntweets)/len(tweets)) * 100

	ret_dict = {
		"subject": subject,
		"ptweets": ptweets, 
		"neutweets": neutweets, 
		"ntweets": ntweets, 
		"num_ptweets": round(num_ptweets, 2), 
		"num_neutweets": round(num_neutweets, 2), 
		"num_ntweets": round(num_ntweets, 2)
	}

	return jsonify(ret_dict)

	# return render_template('tweets.html', subject=subject, ptweets=ptweets, neutweets=neutweets, ntweets=ntweets, num_ptweets=round(num_ptweets, 2), num_neutweets=round(num_neutweets, 2), num_ntweets=round(num_ntweets, 2))

if __name__ == '__main__':
	app.run(debug = True)