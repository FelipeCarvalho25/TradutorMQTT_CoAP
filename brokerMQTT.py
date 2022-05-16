import logging
import asyncio

from hbmqtt.broker import Broker
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1


logger = logging.getLogger(__name__)

config ={
    'listeners' : {
        'default': {
            'type': 'tcp',
            'bind': 'localhost:9999 '
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': False
    }
}

broker = Broker(config)

@asyncio.coroutine
def startBroker():
    yield from broker.start()

@asyncio.coroutine
def brokerGetMessage():
    Cli = MQTTClient()
    yield from Cli.connect('mqtt://localhost:1883')
    yield from Cli.subscribe([
        ("topic2/teste", QOS_1)
    ])
    logger.info("Me inscrevi!")
    try:
        for i in range(1, 100):
            message = yield from Cli.deliver_message()
            packet = message.publish_packet
            print(packet)
    except ClientException as ce:
        logger.error("Client exception: %s" %ce)


if __name__ == "__main__":
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level = logging.INFO, format = formatter)
    asyncio.get_event_loop().run_until_complete(startBroker())
    #asyncio.get_event_loop().run_until_complete(brokerGetMessage())
    asyncio.get_event_loop().run_forever()