import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='jiang'
))

channel = connection.channel()

channel.queue_declare(queue='hello')

print("Waitting for message . To exit press ")

def callback(ch,method,properties,body):
    print("[x] Received %r" % (body,))

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
channel.start_consuming()