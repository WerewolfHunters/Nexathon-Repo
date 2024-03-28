import os
import requests
from PIL import Image
import io
import random
import replicate
from dotenv import load_dotenv

load_dotenv()

def generate_design(title, event_title, venue):
    input = {
        "prompt": f"mdjrny-v4 {title}, event title as {event_title}, venue as {venue}, realistic, potrait, 8k",
        "guidance_scale": 7,
        "num_outputs": 3,
        "image": "https://th.bing.com/th/id/OIG4.FCV6rmNQBfIIk81EKbba?pid=ImgGn"
    } 

    
    output = replicate.run(
    "prompthero/openjourney:ad59ca21177f9e217b9075e7300cf6e14f7e5b4505b87b9689dbd866e9768969",
    input=input
    )

    op = "".join(output)
    print("".join(output))
    op2 = op.replace('.png', '.png,')
    op2 = op2.split(',')
    op2.pop()
    data = op2

    img = []

    if data:
        for item in data:
            # Create PIL image from response content
            image_data = requests.get(item).content
            image = Image.open(io.BytesIO(image_data))
            img.append(image.resize((11000, 12000)))

        return img  # Resize image to fit the poster
    else:
        return None


def generate_poster(title, event_title, venue):
    img_list = generate_design(title, event_title, venue)
    count = 0
    path_list = []
    for image in img_list:
        if image:
            img_path = os.path.join("static", f"poster{count}.png")
            image.save(img_path)
            path_list.append(img_path)
            count += 1
        else:
            path_list.append(None)

    return path_list
