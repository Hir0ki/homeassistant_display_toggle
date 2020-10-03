# homeassistant_display_toggle
Turn on/off the display output of a Raspberry Pi via MQTT.
Works with HomeAssistant MQTT Autodiscovery.

This can be used (for example) to turn on/off the screen attached to a Raspberry Pi running Grafana in kiosk mode via a motion detector.

## Configuration
Add the MQTT credentials and the device name to `config.ini`.

## Installation
Install the Package vcgencmd on your Raspberry Pi (if not available already) to control the screen:
`sudo apt-get install vcgencmd`  
After that you have to install the python dependencies using pip: 
`pip install -r requirements.txt`

## Usage
Run `main.py` with python3. An example systemd unit is provided to run this script as a service.
If everything works correctly, a switch with the configured device name should pop up in your Home Assistant instance.
