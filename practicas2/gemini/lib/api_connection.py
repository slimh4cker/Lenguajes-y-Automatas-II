import google.generativeai as genai
from google.generativeai.types import ContentType
from PIL import Image
from IPython.display import Markdown
import time


def api_connection(prompt):
    GOOGLE_API_KEY = ("AIzaSyC1X9VgwNigoW4PVroXW7ZN0xDUCKdDaVQ")
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)
    return response.text