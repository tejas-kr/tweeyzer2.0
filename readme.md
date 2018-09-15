# Tweelyzer 2.0
Tweelyzer was a web app I made for my 3rd sem college project. It was used for analysing twitter sentiments about a certain topic.
#### Working of Tweelyzer 1.0
- the user enters some topic in a form
- the page reloads in tradition form submit fashion
- and finally the output is shown in newly rendered view.

# New Features in Tweelyzer 2.0!

#### what's improved
- improved ui 
- it's now a single page app (spa)
- data is sent and get via ajax requests.


#### what's added
- [a rest api](#Rest-API)
- you can resuse this api in your own applications...

## Rest API
 using it is damn simple

```
curl https://your-own-uri/tweets?subject=your-subject
```

###### you will get a json containing the following properties:
- neutweets - list of neutral tweets about that topic
- ptweets - list of positive tweets about that topic
- ntweets - list of nagetive tweets about that topic
- num_ntweets - number of nagetive tweets about that topic
- num_ntweets - number of nagetive tweets about that topic
- num_ntweets - number of nagetive tweets about that topic

## Requirements
- python 3
- tweepy - with a twitter api auth key and account
- textblob
- flask
- jquery (not for api)
- bootstarp (not for api)