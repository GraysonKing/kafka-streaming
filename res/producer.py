import time
import os
from kafka import KafkaProducer

# Connecting to Kafka and assigning a topic
KAFKA_IP = os.environ['KAFKA_CLIENT_ADDRESS']
checkKafka = True
print('Producer checking: ' + KAFKA_IP)
while checkKafka:
    try:
        producer = KafkaProducer(bootstrap_servers=KAFKA_IP)
        topic = 'video'
        checkKafka = False # If we don't get an exception, then Kafka is available
    except:
        time.sleep(2)

#print(cv2.getBuildInformation())
# Reading and emitting the video to the broker
def video_emitter(videoFile):
    try:
        if os.path.isfile(videoFile):
            print('file exists')
        video = cv2.VideoCapture(videoFile)
        print('emitting video')

        if video.isOpened():
            print('video has been opened')

        while (video.isOpened()):
            success, image = video.read()

            if not success:
                print('bad read')
                print(success, image)
                break
            else:
                success, jpeg = cv2.imencode('.jpg', image)
                if success:
                    producer.send(topic, jpeg.tobytes())
                    time.sleep(0.2) # Reduce CPU usage
                else:
                    print('not converted...')
                    break
        else:
            print('video not opened')

    finally:
        producer.close()
        video.release()
        print('done emitting')

if __name__ == '__main__':
    video_emitter('/app/res/video.avi')