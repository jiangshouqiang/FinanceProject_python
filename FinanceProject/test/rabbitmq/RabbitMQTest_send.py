import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='jiang'
))

channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='first3 ')
print(" sent 'hello world' ")
connection.close()