
#####################

import requests
from celery import Celery
#   pip install celery==3.1.21

app = Celery('tasks', broker='amqp://localhost/')
#   using docker for both broker and backend
#   docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:management
#     $  docker run -d -p 5672:5672 -p 15672:15672 --name url-rabbit rabbitmq:management
#     $  celery -A consumer.py worker --loglevel=info

@app.task
def download_url(url):
    print("-> Starting: [{}]".format(url))
    try:
        req = requests.get(url)
        if req.status_code == 200:
            with open("data.html", 'w') as f:
                f.write(req.content)
            print(f"-> saved html: [{url}]")
    except:
        print(f'error: {url}')


#   celery -A celery_grabhtml_redis worker --loglevel=info
#   ^ run above celery command in terminal while situated in same folder as current file

#   from celery.task.control import discard_all
#   discard_all()
#   ^ use above to clear celery queue

