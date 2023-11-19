#Given a url to a map, returns a PNG file of the map to be used.
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def downloadMapImage(url, save_path='map.png'):
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the image tag with id "map-background"
        img_tag = soup.find('img', {'id': 'map-background'})

        if img_tag:
            # Extract the image URL
            img_url = urljoin(url, img_tag['src'])

            # Download the image
            img_data = requests.get(img_url).content
            with open(save_path, 'wb') as f:
                f.write(img_data)
            
            print(f"Image downloaded and saved to {save_path}")
        else:
            print("No image found with id 'map-background'.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

website_url = 'https://awbw.amarriner.com/prevmaps.php?maps_id=151870'
downloadMapImage(website_url)