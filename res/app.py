import time
import os
import simplejson as json
from flask import Flask, render_template, request
from kafka import KafkaProducer, KafkaConsumer

KAFKA_IP = os.environ['KAFKA_CLIENT_ADDRESS']
topic = 'chat_feed'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', chat_feed=chatstream(), min_msgs=0, max_msgs=10)

# Read json from the broker and append to the feed array to be used in index.html
def chatstream():
    chat_feed = list()
    chat_json = list()
    consumer = KafkaConsumer(topic, bootstrap_servers=KAFKA_IP, auto_offset_reset='earliest', group_id=None, consumer_timeout_ms=10000)
    try:
        for msg in consumer:
            chat_json = json.loads(msg.value.decode('utf-8'))
            if chat_json:
                chat_name = chat_json['chat_name']
                chat_text = chat_json['chat_text']
                chat_time = chat_json['chat_time']
                chat_feed.append((chat_name, chat_text, chat_time))
        return chat_feed
    finally:
        consumer.close()

# Requesting data from index.html to send to the broker
@app.route('/chat_input', methods=['POST'])
def chat_input():
    producer = KafkaProducer(bootstrap_servers=KAFKA_IP)
    try:
        chat_name = request.form['chat_name']
        chat_text = request.form['chat_text']
        chat_time = time.strftime('%d/%m/%Y %H:%M')
        if not chat_name:
            chat_name = 'Anonymous'
        msg_json = json.dumps({"chat_name" : chat_name, "chat_text" : chat_text, "chat_time" : chat_time})
        producer.send(topic, msg_json.encode('utf-8'))
        return index()
    finally:
        producer.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
