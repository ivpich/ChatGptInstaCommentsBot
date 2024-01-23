# ChatGptInstaCommentsBot
Бот, основанный на gpt-3.5-turbo, который отвечает на все новые комментарии на выбранной инстаграм странице. Бот использует информацию из описания поста, дополнительную информацию, указанную пользователем и текст комментария. Бот отвечает не на все комментарии, а способен отличать стоящие вопросы от спама и нерелевантных комментов.
Бот использует:
- OpenAI API для интеграции ChatGPT
- Facebook Graph API для взаимодействия с Instagram (для использования необходимо зарегестрировать приложение в meta for developers)
- Модель классификации комментариев, которая позволяет отличить комментарии на которые нужно ответить, а какие можно пропустить. Основа - fine-tuned bert-base-multilingual-cased на задачу классификации (BertForSequenceClassification) на размеченном вручную датасете комментариев инстаграм
- Yandex Cloud (Compute Cloud, Container Registry, Managed PostgreSQL server, Datalens) для облачного хостинга, облачной БД и real-time мониторинга работы бота.

![telegram-cloud-photo-size-2-5294357992407420427-y](https://github.com/ivpich/ChatGptInstaCommentsBot/assets/127900049/c6b28196-82ab-4d48-ac06-da7d788ccbcd)

## Возможности

- Интеграция с Instagram API
- Классификация и ответ на комментарии инстаграм
- Мониторинг ответов, активности и стоимости бота (в токенах)


### Использование
Для работы необходимо указать в качестве переменных окружения:
- INSTAGRAM_PAGE_ID
- ACCESS_TOKEN (Facebook Graph API access token)
- DATABASE_URL
- OPENAI_API_TOKEN



