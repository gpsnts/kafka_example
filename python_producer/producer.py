from time import sleep
from random import randint
from sys import argv, exit
from kafka import KafkaProducer

SERIALIZER = lambda x: str(x).encode("utf-8")

def main():
  len_argv = len(argv)
  
  if len_argv != 2:
    print("Deve-se passar apenas um argumento: o tópico do Kafka")
    exit(1)
 
 
  KAFKA_TOPIC = argv[1]
  print(f"SELECTED TOPIC -- {KAFKA_TOPIC}")
  
  producer = KafkaProducer(
    bootstrap_servers="localhost:9092", # Broker(s) receptores
    value_serializer=SERIALIZER					# Serializa e passa o "enconding" da mensagem
  )
  
  counter = 1
  
  while counter <= 50:
    current = randint(56, 789)
    print(f"Sending - {current}")
    producer.send(KAFKA_TOPIC, current)
    sleep(6.0)
    counter += 1