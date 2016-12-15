import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='jiang'
))

channel = connection.channel()

channel.exchange_declare(exchange='logs',type='fanout')

message = ' '.join(sys.argv[1:]) or 'info: HELLO WORLD!'

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print("x sent %r" %(message,))
connection.close()