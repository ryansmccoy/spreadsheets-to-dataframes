#!/usr/bin/env python
import time
import pika
# activate spreadsheets_to_dataframes
# python basic_producer.py

print("* Connecting to RabbitMQ broker")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='pages')

def produce():
    with open('webscraping_celery/urls.txt', 'r') as f:
        urls = f.read().splitlines()

    for url in urls:
        print(f"* Pushed: [{url}]")
        channel.basic_publish(exchange='', routing_key='pages', body=url)

counter = 0

produce()

connection.close()
