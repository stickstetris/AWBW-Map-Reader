#Given a url to a map, saves the html of the page and the PNG file of the map to be used 
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def downloadMapImage(url, save_path='AWBW-Map-READER/saved/map.png'):
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

            # Modify the image URL
            modified_img_url = img_url.replace('/maps/', '/maps_test/aw2/')

            # Download the modified image
            img_data = requests.get(modified_img_url).content
            with open(save_path, 'wb') as f:
                f.write(img_data)

            print(f"Image downloaded and saved to {save_path}")
        else:
            print("No image found with id 'map-background'.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


def download_html(url, save_path='AWBW-Map-Reader\saved\html_content.txt'):
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML content saved to {save_path}")
        return save_path
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    

def getBoth(url):
    download_html(url)
    downloadMapImage(url)