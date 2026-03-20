#import required modules
import requests
def get_current_location():
    #make a request to the ipinfo.io API to get the current location based on the user's IP address
    URL="https://ipinfo.io/json"
    response=requests.get(URL)
    data=response.json()
    city=data["city"]
    region=data["region"]    
    country=data["country"]
    loc=data["loc"]
    postal=data["postal"]
    timezone=data["timezone"]
    return city, region, country, loc, postal, timezone
if __name__=="__main__":
    city, region, country, loc, postal, timezone = get_current_location()
    print("\ndetected location")
    print("-------------------")
    print(f"City:{city}")
    print(f"Region:{region}")
    print(f"Country:{country}")
    print(f"Location:{loc}")
    print(f"Postal Code:{postal}")
    print(f"Timezone:{timezone}")

    
