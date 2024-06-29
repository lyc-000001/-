import json
from kafka import KafkaProducer
from Utils.tools import get_base
from Conf.kafka import *


class KafkaMsgProducer:
    def __init__(self, server):
        self._server = server
        self.producer = None

    def connect(self):
        if self.producer is None:
            producer = KafkaProducer(bootstrap_servers=self._server)
            self.producer = producer

    def close(self):
        if self.producer is not None:
            self.producer.close()
            self.producer = None

    def send(self, topic, msg):
        if self.producer is not None:
            if not isinstance(msg, bytes):
                msg = json.dumps(msg).encode()
        future = self.producer.send(topic=topic, value=msg)
        return future


def connects(msg):
    # producer = KafkaMsgProducer("b-2.uat-sg.fd8oxq.c4.kafka.cn-northwest-1.amazonaws.com.cn:9092")
    producer = KafkaMsgProducer(msg['kafka'])
    producer.connect()  # 建立连接

    print("Start sending msg to kafka!")
    return producer


def send_kafka(producer, key_):
    topic = "wlas_eventinfo_extract_mkt"
    future = producer.send(topic=topic, msg=kafka_data[key_])
    ret = future.get(timeout=10)
    print(ret)


if __name__ == '__main__':
    msg = get_base('pre', 'us')
    producer = connects(msg)
    send_kafka(producer=producer, key_='注册事件-5024')
