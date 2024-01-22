import asyncio
from instagram_api import InstagramAPI
from gpt.chat_gpt import ChatGPT
from db.database_operations import get_db_session, add_comment, get_comment_by_id
import logging
from to_answer_classification_model.answer_decision_model import decide_to_reply,  model, tokenizer, device

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def monitor_and_respond():
    instagram_api = InstagramAPI()
    chat_gpt = ChatGPT()
    # TODO Сделать RAG для FAQ
    additional_info = """
    Ты отвечаешь на комментарии потенциальных покупателей нашего магазина одежды в инстаграм.
    Основываясь на предоставленной информации о магазине и описании инстаграм-публикации (поста), под которым
    оставлен комментарий, ответь на комментарий. Будь лаконичен, но при этом ответь на запрос клиента.
    Если какая-то информация не указана, или ты ее не знаешь, не выдумывай, а предложи уточнить в наших мессенджерах. К примеру,
    ты не имешь информации о наличии изделий. Если клиент желает приобрести, всегда проси клиента уточнить наличие в месенджерах.
    Информация о магазине: наш магазин \"Black Fox\" находится в городе Орехово-Зуево. Мы доставляем посылки по всей России.
    Уточнить наличие, оформить заказ и получить более подробную информацию о товаре можно, если написать нам в телеграм или вотсап по номеру 89163815990.
    В шапке профиля можно найти ссылки на наши мессенджеры, а также наш телеграм канал, в котором еще больше публикаций.
    """

    while True:
        recent_posts = instagram_api.get_recent_posts(limit=2)

        for post in recent_posts:
            comments = instagram_api.get_comments_from_post(post['id'])

            with get_db_session() as db:
                for comment in comments:
                    print('got_comment')
                    if not get_comment_by_id(db, comment['id']):
                        verdict = decide_to_reply(comment['text'], model, tokenizer, device)
                        if verdict == 0:
                            logging.info(f"comment: {comment['text']} was skipped as irrelevant")
                            continue
                        reply = chat_gpt.generate_reply(post['caption'], comment['text'], additional_info)
                        logging.info(f"Post caption: {post['caption']}")
                        logging.info(f"Comment: {comment['text']}")
                        print(comment['text'])
                        if reply:
                            response_text = reply.choices[0].message.content
                            usage = reply.usage.total_tokens
                            # instagram_api.reply_to_comment(comment['id'], response_text) # Comment for testing
                            logging.info(f"Response: {response_text}")
                            comment_data = {
                                "comment_id": comment['id'],
                                "post_id": post['id'],
                                "comment_text": comment['text'],
                                "response_text": response_text,
                                "tokens_spent": usage
                            }
                            add_comment(db, comment_data)

            await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(monitor_and_respond())
