#!/usr/bin/python3 -u 

from config.settings import CONFIG
from subprocess import call
import paho.mqtt.client as mqtt
import logging

def on_message(client, userdata, message):
    logging.info(f"Got mqtt payload: {message.payload}")
    if message.payload == b'ON' :
        logging.info("turning screen on")
        call(["xrandr", "--output", "HDMI-1", "--auto"])
    if message.payload == b'OFF':
        logging.info("turning screen off")
        call(["xrandr", "--output", "HDMI-1", "--off"])

def run(client: mqtt.Client):

    client.publish(f"homeassistant/switch/{CONFIG.get_device_name()}/screen/config", f'{{"unique_id": "screen-{CONFIG.get_device_name()}", "name": "{CONFIG.get_device_name()} Screen", "device": {{"identifiers": ["{CONFIG.get_device_name()}"], "name": "{CONFIG.get_device_name()}"}}, "~": "homeassistant/switch/{CONFIG.get_device_name()}/screen", "availability_topic": "~/state", "command_topic": "~/set", "retain": true}}', retain=True)
    client.publish(f"homeassistant/switch/{CONFIG.get_device_name()}/screen/state", "online", retain=True)
    logging.info("Set mqtt toptic state to online")

    client.subscribe(f"homeassistant/switch/{CONFIG.get_device_name()}/screen/set")
    client.on_message = on_message

    client.loop_forever()

def main():
    client = mqtt.Client()

    client.enable_logger(logger=logging.getLogger("mqtt"))
    client.username_pw_set(CONFIG.get_username() ,CONFIG.get_password())

    #set last will for mqtt broker
    client.will_set(retain=True, payload="offline",topic=f"homeassistant/switch/{CONFIG.get_device_name()}/screen/state")

    client.connect(CONFIG.get_url(), CONFIG.get_port() )

    run(client)

if __name__ == "__main__":
    main()
