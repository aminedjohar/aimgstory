from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

load_dotenv(find_dotenv())

# img2text


def img2text(url):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-base")

    text = image_to_text(url)

    print(text)
    return text


img2text("photo_2023-07-14_17-38-34.jpg")

# largelanguageModel (llm)

# text2Speech
