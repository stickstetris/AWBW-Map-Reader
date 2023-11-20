#Given the left and top coordinates of the animated portions of the map, returns what the animated object is. 
import requests
from bs4 import BeautifulSoup

def arrayIndexToCoordinateLeft(left): #The coordinates for left and top of the website source do not match, here's the conversion function
    return left * 16 + 1

def arrayIndexToCoordinateTop(top):

    return (top) * 16 + 1

def findTile(leftNum, topNum):
    leftNum = arrayIndexToCoordinateLeft(leftNum)
    topNum = arrayIndexToCoordinateTop(topNum)


    # Values to check for topNum
    top_values_to_check = [topNum, topNum - 2, topNum - 6, topNum - 8, topNum - 9, topNum - 15]

    

    for current_top in top_values_to_check:
        with open('AWBW-Map-Reader\saved\html_content.txt', 'r', encoding='utf-8') as file:
            relevant_lines = file.readlines()[250:400]
            html_content = "\n".join(relevant_lines)
            
            # Use BeautifulSoup to parse the relevant HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Construct the style string based on leftNum and current_top
            style_string = f'left:{leftNum}; top:{current_top}; position:absolute; border: 0px; z-index:100;'

            # Find the span element with the specified style
            span_element = soup.find('span', style=style_string)

            if span_element:
                # Extract the src attribute from the img tag within the span element
                img_src = span_element.find('img')['src']

                # Check for multiple keywords and print the matching one
                keywords = ['city', 'comtower', 'base', 'airport', 'pipe', 'port', 'silo', 'hq', 'infantry', 'lab']
                matched_keyword = next((keyword for keyword in keywords if keyword in img_src), None)

                if matched_keyword:
                    return matched_keyword
                else:
                    print(f"No matching keyword found for style 'left:{leftNum}; top:{current_top}'.")
                


