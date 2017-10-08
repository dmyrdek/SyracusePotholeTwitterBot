import tweepy, time, sys, json, urllib2, datetime, inflect

CONSUMER_KEY = 'q5JuzVFycsjKRw1OV4d0qtzT1'
CONSUMER_SECRET = '807W1eDYIVnQ1Jukh2yRTB91zE2HKeA1HjQVqXmHoXIG2KhN1K'
ACCESS_KEY = '916738528054214656-f26w6MCh50w0HcPjyFq0ZuluXxhNohu'
ACCESS_SECRET = 'ylDau4XgwJ71ugirq87f3RvoifocsAPVPcNHeNRFgJqSQ'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class Node:
    def __init__(self,initaddress,initdistrict):
        self.address = initaddress
        self.district = initdistrict
        self.next = None
        self.prev = None
        self.count = 1

class LinkedList:
    def __init__( self ) :
		self.head = None

    def getNext(self):
        return self.head.next
        
    def search(self, tempAddress):
		x = self.head
		if x != None :
			while x.next != None :
				if ( x.address == tempAddress ) :
					return x				
				x = x.next
			if ( x.address == tempAddress ) :
				return x
		return None
		
    def add(self, newAddress, newDistrict):
        if self.search(newAddress) == None:
            node = Node( newAddress, newDistrict)
            if self.head == None:	
                self.head = node
            else:
	            node.next = self.head
	            node.next.prev = node						
	            self.head = node
        else:
                self.search(newAddress).count += 1


data = json.load(urllib2.urlopen('https://services6.arcgis.com/bdPqSfflsdgFRVVM/arcgis/rest/services/Potholes_filled/FeatureServer/0/query?where=1%3D1&outFields=date_fixed,address,TNT_NAME&returnGeometry=false&orderByFields=date_fixed%20DESC&outSR=4326&f=json'))

#Creates linked list
list = LinkedList()

#Yesterday's Unix Time
yesterday = datetime.date.today() - datetime.timedelta(1)
unix_time_yesterday= yesterday.strftime("%s")

#Unix Time from Multiple Days Ago
oneMonthAgo = datetime.date.today() - datetime.timedelta(12)
oneDayAgo = datetime.date.today() - datetime.timedelta(11)
unix_month_ago = oneMonthAgo.strftime("%s")
unix_day_ago = oneDayAgo.strftime("%s")

#Obtain Individual Pothole Data
for pothole in data["features"]:
    date = pothole["attributes"]["date_fixed"]
    date = date/1000
    #Only do Potholes Fixed in Previous Day
    if date > int(unix_month_ago):
        if date < int(unix_day_ago):
            date = time.strftime('%Y-%m-%d', time.localtime(date))
            district = pothole["attributes"]["TNT_NAME"]
            address = pothole["attributes"]["address"]
            address = address.rstrip()
            list.add(address, district)

#Tweet Potholes Filled at Each Address        
temp = list
while temp.getNext() != None:
    d = inflect.engine()
    num = d.number_to_words(int(temp.head.count))
    num = str(num)
    num = num.title()
    
    #Tweet Based on District and Number of Potholes
    if temp.head.count == 1:
        if temp.head.district == "Downtown":
            api.update_status(status = num + " pothole was fixed this morning at " + temp.head.address.title() + " in #" + temp.head.district + "Syracuse") 
        elif temp.head.district == "Eastwood":
            api.update_status(status = num + " pothole was fixed this morning at " + temp.head.address.title() + " in #" + temp.head.district + "OfSyracuse") 
        else:
            api.update_status(status = num + " pothole was fixed this morning at " + temp.head.address.title() + " in the #" + temp.head.district + "OfSyracuse")
    else:
        if temp.head.district == "Downtown":
            api.update_status(status = num + " potholes were fixed this morning at " + temp.head.address.title() + " in #" + temp.head.district + "Syracuse") 
        elif temp.head.district == "Eastwood":
            api.update_status(status = num + " potholes were fixed this morning at " + temp.head.address.title() + " in #" + temp.head.district + "OfSyracuse") 
        else:
            api.update_status(status = num + " potholes were fixed this morning at " + temp.head.address.title() + " in the #" + temp.head.district + "OfSyracuse")
    
    #Get Next Location
    temp.head = temp.getNext()
    
    #Wait One Minute to Tweet About the Next Location
    time.sleep(60)