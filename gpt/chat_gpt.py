from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class ChatGPT:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_TOKEN')

    def generate_reply(self, caption, comment, additional_info):
        full_prompt = f"""
        {additional_info}
        Информация из описания инстаграм поста:
        '{caption}'
        Тебе необходимо ответить на следующий комментарий от лица магазина - комментарий:
        """

        try:
            client = OpenAI(api_key=self.api_key)
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": full_prompt,
                    },
                    {"role": "user",
                     "content": comment}
                ],
                model="gpt-3.5-turbo",
            )
            return chat_completion
        except Exception as e:
            print(f"Error in generating GPT reply: {e}")
            return None
