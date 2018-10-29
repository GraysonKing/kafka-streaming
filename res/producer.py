import time
import cv2
import os
from kafka import SimpleProducer, KafkaClient, KafkaProducer

# Connecting to Kafka and assigning a topic
print os.environ['KAFKA_CLIENT_ADDRESS']
KAFKA_VERSION=(0,10)
#kafka = KafkaClient('165.227.31.0:9092')
#producer = SimpleProducer(kafka)
producer = KafkaProducer(bootstrap_servers=os.environ['KAFKA_CLIENT_ADDRESS'], api_version=KAFKA_VERSION, value_serializer=str.encode)
topic = 'video'

# Reading and emitting the video to the broker
def video_emitter(video):
    video = cv2.VideoCapture(video)
    print('emitting.....')

    while (video.isOpened):
        success, image = video.read()

        if not success:
            break

        ret, png = cv2.imencode('.png', image)

        producer.send_messages(topic, jpeg.tobytes())
        time.sleep(0.2) # Reduce CPU usage

    video.release()
    print('done emitting')

if __name__ == '__main__':
    video_emitter('video.mp4')