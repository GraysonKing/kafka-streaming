import time
import os
import simplejson as json
from flask import Flask, Response, render_template, request
from kafka import KafkaProducer, KafkaConsumer

# Connecting to Kafka and assigning a topic
KAFKA_IP = os.environ['KAFKA_CLIENT_ADDRESS']
topic = 'chat_feed'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', chat_feed=chatstream())

# Read chat json and append to an array so it can be used in the html
def chatstream():
    chat_feed = list()
    try:
        consumer = KafkaConsumer(topic, bootstrap_servers=KAFKA_IP, auto_offset_reset='earliest', group_id='chat_consumer', consumer_timeout_ms=10000)
        for msg in consumer:
            chat_json = json.loads(msg.decode('utf-8'))
            if chat_json:
                chat_name = chat_json['chat_name']
                chat_text = chat_json['chat_text']
                chat_feed.append((chat_name, chat_text))
            #chat_feed.append(msg)
            return chat_feed
    except:
        chat_feed.append(('SYSTEM', 'ERROR OCCURED'))    
    finally:
        consumer.close()

@app.route('/chat_input', methods=['POST'])
def chat_input():
    try:
        producer = KafkaProducer(bootstrap_servers=KAFKA_IP)
        chat_name = request.form['chat_name']
        chat_text = request.form['chat_text']
        #msg = '{"chat_name" : "%s", "chat_text" : "%s"}' % (chat_name, chat_text)
        msg = 'test'
        producer.send(topic, json.dumps(msg.encode('utf-8')))
        #print producer.send(topic, b'some_message_bytes').get(timeout=30)
        return index()
    finally:
        producer.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)