import os
import requests
from PIL import Image
import io


def generate_poster_with_postermywall(title):
    POSTERMYWALL_API_URL = "https://www.postermywall.com/api/1.0/public/designs"
    POSTERMYWALL_API_KEY = "oPsQiZjNQA2AzWwrDF6mSWLO35ddxBLC"  # Replace with your PosterMyWall API key

    headers = {
        "Authorization": f"Bearer {POSTERMYWALL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "templateId": "YOUR_TEMPLATE_ID",  # Replace with your template ID
        "fields": {
            "title": title
        }
    }

    try:
        response = requests.post(POSTERMYWALL_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        design_id = response.json().get('id')
        
        # Download the generated design
        download_url = f"https://www.postermywall.com/api/1.0/public/designs/{design_id}/download"
        response = requests.get(download_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Create PIL image from response content
        image_data = requests.get(response.json()['url']).content
        image = Image.open(io.BytesIO(image_data))
        return image.resize((800, 600))  # Resize image to fit the poster

    except requests.RequestException as e:
        print(f"Error generating poster with PosterMyWall: {e}")
        return None

def generate_poster(title):
    # Generate poster using PosterMyWall
    image = generate_poster_with_postermywall(title)
    
    if image:
        img_path = os.path.join("static", "poster.png")
        image.save(img_path)
        return img_path
    else:
        return None
