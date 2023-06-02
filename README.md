#This tool is for educational and legal purpose only , use it illegally at your own risk !!!.

#You will need stable and good internet connection to make the tool run accurately.

#The ownner of this script will not be responsible for any damage or illegal activities used for this script, you do that at your own risk!.

##INSTALLATION##
git clone https://github.com/White7-shark/SharkTracker.git
cd PyTracker
pip install -r requirements.txt
chmod +x pytracker.py


##USAGE##
python3 pytracker.py
choose your option to run

##OPTIONS##
1. phone number
 when using option1 to track or get information for a particular phone number , add the region or country code attach the number
for eg +14842989271 , +1 is the country code
You made an api for the full output or result of this option. The link for the api will be given to you in the output of the script

2.ip address
 when using option 2, please use a coreect or valid ip address , else it will return an error

3.coordinates
 Enter the correct latitude and longitude to geolocate the location for you perfectly or use option 1 for the prompt that will be 
 given to get the coordinates of an address  or a place(reverse geolocation)

4.geolocation
 This uses google's api to get a location from a wifi access points or a cell tower that a mobile device or an electronic can connect
 to. To use this you will be asked  to give some details of the cell tower or the wifi access point. Google's geolcation api receives https requests
 with the cell tower or wifi access point then returns latitude/longitude coordinates and a radius indicating the accuracy 
 of the result for each valid input. For more info about the geolocation with google's api visit https://developers.google.com/maps/documentation/geolocation/overview

5.location from exif
  This option extracts data called exif data from images then pin point a location from it. for example like where the  image
  was taken from, the place, the device used to take the image and others. It also gives a map from google map of the location 
  where the image was taken from. To use this option please insert image(s) in the image folder. The image folder is in the same 
  directory with the sharktracker.py or the README.md.
   

### for more info please or any question follow me on twitter:https://twitter.com/YoungSh32788105 ### or
## get info about me on https://github.com/White7-shark
    
