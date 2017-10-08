import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET KEY'
ACCESS_KEY = 'YOUR ACCESS KEY'
ACCESS_SECRET = 'YOUR ACCESS SECRET KEY'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#landon sucks <-- true (cedric) <-- not true (brian)



# twitter account: CusePotholes
# password : cusepothole
# swag #popular #followforfollow #followersarelife #briancantholdalchol #fuckyou

#twitter bot info
# Consumer Key (API Key)	q5JuzVFycsjKRw1OV4d0qtzT1
# Consumer Secret (API Secret)	807W1eDYIVnQ1Jukh2yRTB91zE2HKeA1HjQVqXmHoXIG2KhN1K
#Access Token	916738528054214656-f26w6MCh50w0HcPjyFq0ZuluXxhNohu
#Access Token Secret	ylDau4XgwJ71ugirq87f3RvoifocsAPVPcNHeNRFgJqSQ


#Owner	CusePotholes
#Owner ID	916738528054214656