from aiokafka import AIOKafkaProducer #type:ignore 
from sqlmodel import Session #type:ignore
from app.db_engine import engine #type:ignore

# Kafka Producer as a dependency
async def get_kafka_producer():
    producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()

def get_session():
    with Session(engine) as session:
        yield session
