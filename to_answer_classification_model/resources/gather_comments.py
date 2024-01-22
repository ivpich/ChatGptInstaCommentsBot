import pickle
from time import sleep

from instagram_api import InstagramAPI

instagram_api = InstagramAPI()
# recent_posts = instagram_api.get_recent_posts(limit=150)

# with open('posts.pkl', 'wb') as file:
#     pickle.dump(recent_posts, file)
#


with open('posts.pkl', 'rb') as file:
    recent_posts = pickle.load(file)


list_of_comments = []
counter = 0
for post in recent_posts:
    try:
        comments = instagram_api.get_comments_from_post(post['id'])
        for comment in comments:
            try:
                list_of_comments.append(comment['text'])
            except Exception as e:
                print(e)
        print(list_of_comments[counter:])
        counter += len(comments)
        sleep(0.5)
    except Exception as e:
        print(e)

with open('comments.pkl', 'wb') as file:
    pickle.dump(list_of_comments, file)