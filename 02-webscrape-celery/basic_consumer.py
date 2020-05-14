#!/usr/bin/env python
import pika
import requests
from bs4 import BeautifulSoup
# python3 -m venv venv

# activates the virtualenv
# source venv/bin/activate
# pip3 install bs4 requests celery pika
# python basic_consumer.py

def on_message(channel, method_frame, header_frame, body):
    print(f"-> Starting: [{body}]")
    r = requests.get(body)
    soup = BeautifulSoup(r.text)
    print(f"-> Extracted: {soup.html.head.title}")
    print(f"-> Done: [{body}]")
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
print('* Handling messages.')

channel.basic_consume('pages', on_message)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
