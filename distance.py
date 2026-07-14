import http.client
import json
from geopy import distance


def get_coordinates(pincode, conn, headers):
    try:
        conn.request("GET", f"/api/v1/pincode/{pincode}", headers=headers)
        res = conn.getresponse()
        if res.status == 200:
            data = res.read()
            result = data.decode('utf-8')
            result_json = json.loads(result)
            if result_json:
                return (result_json[0]["lat"], result_json[0]["lng"])
            else:
                print(f"No results found for pincode {pincode}")
                return None
        else:
            print(f"Failed to retrieve coordinates for pincode {pincode}. Status code: {res.status}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def calculate_distance(pincode1, pincode2):
    error = 0.9
    conn = http.client.HTTPSConnection("india-pincode-with-latitude-and-longitude.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "8922f7cb31mshc124a6b4a078330p195988jsna0f76f4667ba",
        'x-rapidapi-host': "india-pincode-with-latitude-and-longitude.p.rapidapi.com"
    }

    coords = []
    for pincode in (pincode1, pincode2):
        coord = get_coordinates(pincode, conn, headers)
        if coord:
            coords.append(coord)

    if len(coords) == 2:
        dist = distance.distance(coords[0], coords[1])
        return float(str(dist).partition("km")[0]) + error
    else:
        print("Failed to retrieve coordinates for one or both pincodes.")

    conn.close()
