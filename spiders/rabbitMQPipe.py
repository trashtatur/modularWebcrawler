from rabbitmq_connector import RabbitMQProducer


class RabbitMQPipeline(object):

    def __init__(self):
        self.producer = RabbitMQProducer(exchange='forum40',
                                         exchange_type='topic',
                                         routing_key='twitter.tweets.raw',
                                         url='amqp://guest:guest@192.168.99.100/%2f')
        """
        :param exchange is relevant to set the exchange
        :param exchange_type This one is topic. Others can be 'direct', 'fanout', 'headers'
        :param routing_key Is a publishing key for rabbitMQ
        :param url sets the connectivity to RabbitMQ
        :param 
        """
        self.producer.start()

    def process_item(self, item):
        self.producer.add(item)
