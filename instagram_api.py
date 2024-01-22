import requests
import os
from dotenv import load_dotenv

load_dotenv()


class InstagramAPI:
    def __init__(self):
        self.base_url = "https://graph.facebook.com/v18.0"
        self.page_id = os.getenv('INSTAGRAM_PAGE_ID')
        self.access_token = os.getenv('ACCESS_TOKEN')

    def get_recent_posts(self, limit=7):
        url = f"{self.base_url}/{self.page_id}/media?fields=id,caption,timestamp&limit={limit}&access_token={self.access_token}"
        response = requests.get(url)
        return response.json().get('data', [])

    def get_comments_from_post(self, post_id):
        url = f"{self.base_url}/{post_id}/comments?access_token={self.access_token}"
        response = requests.get(url)
        return response.json().get('data', [])

    def reply_to_comment(self, comment_id, message):
        url = f"{self.base_url}/{comment_id}/replies"
        data = {'message': message, 'access_token': self.access_token}
        return requests.post(url, data=data).json()
