
#####################
#   using docker for both broker and backend
#     $  docker run -d -p 5672:5672 -p 15672:15672 --name url-rabbit rabbitmq:management
#     $  celery -A consumer worker --loglevel=info


import requests
from celery import Celery
#   pip install celery==3.1.21
# ^ windows

app = Celery('tasks', broker='amqp://localhost/')

@app.task
def download_url(url):
    print(f"-> Starting: [{url}]")
    try:
        req = requests.get(url)
        if req.status_code == 200:

            print(f"-> Success Download: [{url}]")
    except:
        print(f'error: {url}')


#   celery -A consumer worker --loglevel=info
#   ^ run above celery command in terminal while situated in same folder as current file

#   from celery.task.control import discard_all
#   discard_all()
#   ^ use above to clear celery queue


