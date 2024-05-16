import pika, os
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()
print("[✅] Channel over a connection created")

channel.queue_declare(queue='hello_world')

channel.basic_publish('', "hello_world", "Hello World")
channel.basic_publish('', "hello_world", "Hello World")
channel.basic_publish('', "hello_world", "Hello World")

try:
    connection.close()
    print("[❎] Connection closed")
except Exception as e:
    print(f"Error: #{e}")
