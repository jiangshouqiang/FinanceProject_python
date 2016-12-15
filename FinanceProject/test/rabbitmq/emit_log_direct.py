import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='jiang'
))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

serverity = sys.argv[1] if len(sys.argv) > 1 else 'info'

message = ' '.join(sys.argv[2:]) or 'HELLO WORLD'

channel.basic_publish(exchange='direct_logs',
                      routing_key=serverity,
                      body=message)
print("[x] sent %r:%r" % (serverity,message))
connection.close()