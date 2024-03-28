import requests

"""
style-ids
1. 21 - ANIME
2. 26 - POTRAIT
3. 29 - REALISTIC
4. 122 - SDXL 1.0 - Innovative AI
5. 27 - Imagine V1 - Master an adaptable art style: photo-realistic
6. 28 - Imagine V3 - Master photo-realism with an adaptable style
7. 30 - Imagine V4 - Discover a style mastering photo-realism
8. 31 - Imagine V4 (Creative) - Merge photorealism with adaptable
9. 32 - Imagine V4.1 - Versatile art merging photorealism with limitless stylized creativity.
10. 33 - Imagine V5 - A boundary-defying art style seamlessly merging realism and limitless creativity.
11. 34 - Anime V5 - Anime-infused art style: dynamic, expressive, and brimming with vibrant storytelling in every stroke.
"""
url = 'https://api.vyro.ai/v1/imagine/api/generations'
API_KEY = '	vk-b7U3NLEnk9lfoKMmezAYdBmbRkoUhzjvPDBsjw5a9P2oNE'

headers = {
  'Authorization': f'Bearer {API_KEY}'
}

prompt = input('Enter Prompt: ')
payload = {
  'prompt': (None, f'{prompt}'),
  'style_id': (None, '26')
}

response = requests.post(url, headers=headers, files=payload)

if response.status_code == 200:
  with open('image.jpg', 'wb') as f:
    f.write(response.content)
else:
  print('Error:', response.status_code)