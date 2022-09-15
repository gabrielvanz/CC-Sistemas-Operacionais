import os
from datetime import datetime

from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

import sys
validador = False

for arg in range(1, len(sys.argv)):
    if (sys.argv[arg]) == "-r":
        validador = True


if (validador == True):
    os.environ["pubsub_uuid"] = "feerposser-pc"

    pnconfig = PNConfiguration()

    pnconfig.publish_key = "pub-c-4e5ccfef-72b0-4643-9a77-f9964bc0c67c"
    pnconfig.subscribe_key = "sub-c-44bdf90f-bd2d-4d22-b54c-b267068234e0"
    pnconfig.uuid = os.environ["pubsub_uuid"]

    canal = "Atitus"

    pubnub = PubNub(pnconfig)


    class RecebeMensagem(SubscribeCallback):
        def presence(self, pubnub, event):
            pass

        def status(self, pubnub, event):
            pass

        def message(self, pubnub, event):
            print("{}: {}\n{}".format(event.message["usr"], event.message["msg"], datetime.now().strftime("%H:%M:%S")))

    pubnub.add_listener(RecebeMensagem())
    pubnub.subscribe().channels(canal).with_presence().execute()

else:
    print("Nenhum argumento válido!")
    print("Utilize '-r' como argumento")

