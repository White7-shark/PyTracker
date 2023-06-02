from pprint import pprint

import folium
import phonenumbers


def phonetrack():
    """""Phone numbers """""
    from phonenumbers import geocoder
    try:
        Targetnum = (input("Enter target's number:"))
        tarpar = phonenumbers.parse(Targetnum)
        tarloca = geocoder.description_for_number(tarpar, "en")
        print("Target number located on", tarloca)
        print("checking if target can be dialled internationally...",
              phonenumbers.can_be_internationally_dialled(tarpar))
        print("checking if number is geographical...", phonenumbers.is_number_geographical(tarpar))
        print("checking if number is alpha...", phonenumbers.is_alpha_number(Targetnum))
        print("checking if number is possible...", phonenumbers.is_possible_number(tarpar))
        print("checking if number is valid short number...", phonenumbers.is_valid_short_number(tarpar))
        print("Region code for number is:", phonenumbers.region_code_for_number(tarpar))
        print("National significant number:", phonenumbers.national_significant_number(tarpar))
        print("Number type:", phonenumbers.number_type(tarpar))
        print("supported calling codes", phonenumbers.supported_calling_codes())
        from phonenumbers import carrier

        ser_par = phonenumbers.parse(Targetnum)
        ser_pro = carrier.name_for_number(ser_par, "en")
        service = carrier.safe_display_name(ser_par, "en")
        print("service name:", ser_pro)
        print("checking if carrier is specific...", phonenumbers.is_carrier_specific(ser_par))

        from opencage.geocoder import OpenCageGeocode

        map = input("Do you want a map for the target location, Enter Y/N:")
        umap = str.lower(map)
        if umap == "y":
            api = input("Which api do you prefer, enter 1 for google or enter 2 for opencage:")
            print()
            if api == "2":
                print(
                    "HINT: pls visit 'https://opencagedata.com' and signup for your api keys. For a better result you can \n"
                    "purchase the  priced one instead of the free-trial but any of them will worked")
                print()
                key = input("Paste your api key:")
                geocoder = OpenCageGeocode(key)
                query = str(tarloca)
                result = geocoder.geocode(query)
                print("Giving extra information about target's number...")
                print()
                pprint(result)

                lat = result[0]['geometry']['lat']
                lng = result[0]['geometry']['lng']
                maploca = folium.Map(location=[lat, lng], zoom_start=9)
                folium.Marker([lat, lng], popup=tarloca).add_to(maploca)
                maploca.save("Targetlocation.html")
                print("please the map has been saved in your current directory with the name Targetlocation.html \n "
                      "open to view the map")
            elif api == "1":
                print("HINT:please visit https://developers.google.com/maps/documentation/geocoding/overview to get or"
                      "purchase your api, google has a free trial so you can use that.")
                import requests
                import webbrowser

                # Define the API endpoint and your API key
                url = 'https://maps.googleapis.com/maps/api/geocode/json'
                api_key = input("paste your api key here:")

                # Create parameters for the API request
                params = {
                    'address': Targetnum,
                    'key': api_key
                }

                # Send a GET request to the API
                response = requests.get(url, params=params)

                # Handle the response
                if response.status_code == 200:
                    data = response.json()
                    results = data['results']

                    if results:
                        # Extract the latitude and longitude from the first result
                        location = results[0]['geometry']['location']
                        latitude = location['lat']
                        longitude = location['lng']

                        print("Latitude: ", latitude)
                        print("Longitude: ", longitude)

                        # Construct the map URL with the coordinates
                        map_url = f'https://www.google.com/maps?q={latitude},{longitude}'

                        # Open the map URL in a browser window
                        webbrowser.open_new(map_url)
                    else:
                        print("No results found for the phone number.")
                else:
                    print("Error:", response.status_code)

        else:
            exit()
    except phonenumbers.NumberParseException:
        print("Missing or invalid country or region code, perhaps might be a wrong number.")


"""""ip address"""""

import geocoder
import folium
import os


def iptrack():
    target = input("Enter target IP address (type 'me' for your own IP address): ")

    if target == 'me':
        # Track own IP address
        geo = geocoder.ip('me')
    else:
        # Track specified IP address
        geo = geocoder.ip(target)

    if geo.ok:
        lat, lng = geo.latlng

        # Create a map centered around the IP coordinates
        map = folium.Map(location=[lat, lng], zoom_start=12)

        # Add a circle marker and a popup to the map
        folium.CircleMarker(location=[lat, lng], radius=50, popup="Location").add_to(map)
        folium.Marker(location=[lat, lng], popup=str(geo)).add_to(map)

        # Remove the previous file if it exists
        if os.path.exists("iplocation.html"):
            os.remove("iplocation.html")

        # Save the map to the HTML file
        map.save("iplocation.html")
        print("\n" + "The map for the target location is saved in your current directory with the name 'iplocation.html'.")
        print("\n" + "IP coordinates: Latitude =", lat, "Longitude =", lng)
    else:
        print("Failed to retrieve geolocation for the IP address.")


"""""coordinates"""""


def cordtrack():
    import geocoder
    quest=input("Enter 1 for reverse geolocation or 2 for geolocating coordinates:")
    if quest=="1":
        from geopy.geocoders import Nominatim

        geolocator = Nominatim(user_agent="my-app")

        address = input("Enter an address: ")

        location = geolocator.geocode(address)
        if location is not None:
            latitude = location.latitude
            longitude = location.longitude
            print("Latitude:", latitude)
            print("Longitude:", longitude)
        else:
            print("Failed to retrieve geolocation data for the address:", address)

    else:
        # Get coordinates from user
        latitude = input("Enter latitude: ")
        longitude = input("Enter longitude: ")

        # Create geocoder object and get location information
        location = geocoder.osm([latitude, longitude], method='reverse')

        # Get address details
        address = location.address
        city = location.city
        state = location.state
        country = location.country

        # Print location details
        print(f"Address: {address}")
        print(f"City: {city}")
        print(f"State: {state}")
        print(f"Country: {country}")

        # Create map centered on the coordinates
        map_center = [latitude, longitude]
        m = folium.Map(location=map_center, zoom_start=12)

        # Add marker to the map
        folium.Marker(location=map_center, popup=address).add_to(m)

        # Save the map to an HTML file
        m.save("map.html")
        print("The map for the target location is saved in your current directory with the name 'map.html', open it to "
              "view the map")


def geolocation():
    import requests

    # Prompt the user for API key and cell tower details
    api_key = input("Enter your Google API key: ")
    cell_id = int(input("Enter the cell ID: "))
    location_area_code = int(input("Enter the location area code: "))
    mobile_country_code = int(input("Enter the mobile country code: "))
    mobile_network_code = int(input("Enter the mobile network code: "))
    signal_strength = int(input("Enter the signal strength: "))

    # Define the API endpoint
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}'

    # Create the JSON payload with the user input
    payload = {
        "considerIp": "true",
        "cellTowers": [
            {
                "cellId": cell_id,
                "locationAreaCode": location_area_code,
                "mobileCountryCode": mobile_country_code,
                "mobileNetworkCode": mobile_network_code,
                "signalStrength": signal_strength
            }
        ]
    }

    # Send a POST request to the API
    response = requests.post(url, json=payload)

    # Handle the response
    if response.status_code == 200:
        data = response.json()
        location = data['location']
        accuracy = data['accuracy']

        print("Latitude:", location['lat'])
        print("Longitude:", location['lng'])
        print("Accuracy:", accuracy)
    else:
        print("Error:", response.status_code)


def exif():
    import os
    import sys
    from PIL import Image
    from PIL.ExifTags import GPSTAGS, TAGS

    # Helper function
    def init_Gmaps_url(gps_coords):
        dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]), float(gps_coords["lat"][1]),
                                              float(gps_coords["lat"][2]), gps_coords["lat_ref"])

        dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]), float(gps_coords["lon"][1]),
                                              float(gps_coords["lon"][2]), gps_coords["lon_ref"])

        return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"

    def convert_decimal_degrees(degree, minutes, seconds, direction):
        decimal_degrees = degree + minutes / 60 + seconds / 3600
        if direction == "S" or direction == "W":
            decimal_degrees *= -1
        return decimal_degrees

    while True:
        output_choice = input("Where do you want to display the output:\n\n1 - File\n2 - Terminal\nEnter choice here: ")
        try:
            conv_val = int(output_choice)
            if conv_val == 1:
                sys.stdout = open("TargetLocation.txt", "w")
                break
            elif conv_val == 2:
                break
            else:
                print("Please choose the correct option")
        except:
            print("Enter the correct option")

    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, "images"))
    files = os.listdir()

    if len(files) == 0:
        print("No files found in /images")
        exit()
    for file in files:
        try:
            image = Image.open(file)
            print(
                f"_______________________________________________________________{file}_______________________________________________________________")
            gps_coords = {}
            if image._getexif() == None:
                print(f"{file} has no exif data.")
            else:
                for tag, value in image._getexif().items():
                    tag_name = TAGS.get(tag)
                    if tag_name == "GPSInfo":
                        for key, val in value.items():
                            print(f"{GPSTAGS.get(key)} - {val}")
                            if GPSTAGS.get(key) == "GPSLatitude":
                                gps_coords["lat"] = val
                            elif GPSTAGS.get(key) == "GPSLongitude":
                                gps_coords["lon"] = val
                            elif GPSTAGS.get(key) == "GPSLatitudeRef":
                                gps_coords["lat_ref"] = val
                            elif GPSTAGS.get(key) == "GPSLongitudeRef":
                                gps_coords["lon_ref"] = val
                    else:
                        print(f"{tag_name} - {value}")
                if gps_coords:
                    print(init_Gmaps_url(gps_coords))
        except IOError:
            print("File format not supported!")

    if output_choice == "1":
        sys.stdout.close()
    os.chdir(cwd)


import pyfiglet
from termcolor import colored

text = "PyTracker"

# Generate the banner
banner = pyfiglet.figlet_format(text)

# Add color to the banner
colored_banner = colored(banner, color="blue")

print(colored_banner)
menu_color = "green"
print(colored("          version 1.0", color=menu_color))
print(colored("          created by: Young Shark", color=menu_color))
print("---------------------------------------------")
print"\n" + (colored("1.Track phone number", color=menu_color))
print("\n" + (colored("2.Track ip address", color=menu_color))
print("\n" + colored("3.Track coordinates", color=menu_color))
print("\n" + colored("4.Get a geolocation. Note this gets location of a device with non geolocation feeature"
              "or gps from a cell tower or a wifi access point, you can read more from Google geolocation"
              "and it requires google geolocation api", color=menu_color))
print("\n" + colored("5.Track location from exif data", color=menu_color))
print(colored("---------------------------------------------------------", color=menu_color))
print(" ")
options = input(colored("Enter 1,2,3,4 or 5:", color=menu_color))
if options == "1":
    phonetrack()
elif options == "2":
    iptrack()
elif options == "3":
    cordtrack()
elif options == "4":
    geolocation()
elif options == "5":
    exif()
else:
    print("you have entered a wrong option please select the correct option ")
