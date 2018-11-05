# Use an official Python images as the base
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r res/requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable for the Kafka client
ENV KAFKA_CLIENT_ADDRESS='localhost:9092'

# Run consumer.py and producer.py in parallel when the container launches
#CMD res/parallel_commands.sh "python res/producer.py" "python res/consumer.py"
#CMD python res/producer.py && python res/consumer.py
CMD python res/app.py
