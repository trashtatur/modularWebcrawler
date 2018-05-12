import os

from rabbitmq_connector import RabbitMQProducer


class RabbitMQPipeline(object):
    exchange = os.environ.get("CLOUDAMQP_EXCHANGE", "forum40")
    exchange_type = os.environ.get("CLOUDAMQP_EXCHANGE_TYPE", "topic")
    url = os.environ.get("CLOUDAMQP_URL", "amqp://guest:guest@192.168.99.100/%2f")

    def __init__(self):
        self.producer = RabbitMQProducer(exchange=RabbitMQPipeline.exchange,
                                         exchange_type=RabbitMQPipeline.exchange_type,
                                         routing_key='twitter.tweets.raw',
                                         url=RabbitMQPipeline.url)
        self.producer.start()

        """
        :var exchange is relevant to set the exchange
        :var exchange_type This one is topic. Others can be 'direct', 'fanout', 'headers'
        :var routing_key Is a publishing key for rabbitMQ
        :var url sets the connectivity to RabbitMQ
        """

    def process_item(self, item):
        self.producer.add(item)
