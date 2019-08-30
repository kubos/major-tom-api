import logging
import asyncio
import time
import argparse
from random import randint
from majortom_api.gateway import Gateway

logger = logging.getLogger(__name__)


# async def send_measurements(gateway, num_systems, num_subsystems, num_measurements):
#     while True:
#         for system in range(0, num_systems):
#             for subsystem in range(0, num_subsystems):
#                 metrics = []
#                 for measurement in range(0, num_measurements):
#                     metrics.append({"system": "system"+str(system),
#                                     "subsystem": "subsystem"+str(subsystem),
#                                     "metric": "metric"+str(measurement),
#                                     "value": randint(-1000, 1000)})
#                 asyncio.ensure_future(gateway.transmit_metrics(metrics))
#         await asyncio.sleep(1)
#
# # Set up command line arguments
# parser = argparse.ArgumentParser()
# parser._action_groups.pop()
# required = parser.add_argument_group('required arguments')
# optional = parser.add_argument_group('optional arguments')
# required.add_argument(
#     '-m',
#     '--majortomhost',
#     help='Major Tom host name. Can also be an IP address for local development/on prem deployments.',
#     required=True)
# required.add_argument(
#     '-g',
#     '--gatewaytoken',
#     help='Gateway Token used to authenticate the connection. Look this up in Major Tom under the gateway page for the gateway you are trying to connect.',
#     required=True)
# optional.add_argument(
#     '-b',
#     '--basicauth',
#     help='Basic Authentication credentials. Not required unless BasicAuth is active on the Major Tom instance. Must be in the format "username:password".',
#     required=False)
#
# args = parser.parse_args()
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# logger.info("Starting up!")
# loop = asyncio.get_event_loop()
#
# logger.debug("Setting up MajorTom")
# gateway = Gateway(
#     host=args.majortomhost,
#     gateway_token=args.gatewaytoken,
#     basic_auth=args.basicauth
# )
#
# logger.debug("Connecting to MajorTom")
# asyncio.ensure_future(gateway.connect_with_retries())
#
# logger.debug("Sending Measurements")
# asyncio.ensure_future(send_measurements(gateway=gateway,
#                                         num_systems=2,
#                                         num_subsystems=5,
#                                         num_measurements=100))
#
# logger.debug("Starting Event Loop")
# loop.run_forever()
