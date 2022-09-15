import os

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

import sys
validador = False

for arg in range(1, len(sys.argv)):
    if (sys.argv[arg]) == "-e":
        validador = True


if (validador == True):
    os.environ["pubsub_uuid"] = "feerposser-pc"

    pnconfig = PNConfiguration()

    pnconfig.publish_key = "pub-c-4e5ccfef-72b0-4643-9a77-f9964bc0c67c"
    pnconfig.subscribe_key = "sub-c-44bdf90f-bd2d-4d22-b54c-b267068234e0"

    pnconfig.uuid = os.environ["pubsub_uuid"]

    # pnconfig.publish_key = os.getenv("pubsub_pub")
    # pnconfig.subscribe_key = os.getenv("pubsub_sub")

    # set pubsub_pub=pub-c-18a9fb37-6f1b-4217-992b-fa9ec609c206
    # set pubsub_sub=sub-c-af1bcac4-11b5-11ec-83e9-0e85f81976b6

    canal = "Atitus"

    usr = input("Seu nome: ")
    print("-"*50)

    pubnub = PubNub(pnconfig)

    while True:
        msg = input("Fala ae: ")
        envelope = pubnub.publish().channel(canal).message({"msg": msg, "usr": usr}).sync()

        if envelope.status.is_error():
            print("->>>>> DEU PAU")

else:
    print("Nenhum argumento válido!")
    print("Utilize '-e' como argumento")