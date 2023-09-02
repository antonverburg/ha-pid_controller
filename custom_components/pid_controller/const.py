"""Constants for the PID Controller integration."""
from homeassistant.const import Platform

from .ha_pid_shared.const import (
    ATTR_CYCLE_TIME,
    ATTR_LAST_CYCLE_START,
    ATTR_PID_ENABLE,
    ATTR_PID_ERROR,
    ATTR_PID_INPUT,
    ATTR_PID_KD,
    ATTR_PID_KI,
    ATTR_PID_KP,
    ATTR_PID_OUTPUT,
    ATTR_VALUE,
    CONF_CYCLE_TIME,
    CONF_PID_KD,
    CONF_PID_KI,
    CONF_PID_KP,
    SERVICE_ENABLE,
)

DOMAIN = "pid_controller"
PLATFORMS = [Platform.NUMBER]

ATTR_INPUT1 = "input1"
ATTR_INPUT2 = "input2"
ATTR_OUTPUT = "output"

CONF_NUMBERS = "numbers"
CONF_INPUT1 = "input1"
CONF_INPUT2 = "input2"
CONF_OUTPUT = "output"
CONF_STEP = "step"
CONF_PID_DIR = "direction"

MODE_SLIDER = "slider"
MODE_BOX = "box"
MODE_AUTO = "auto"

SERVICE_SET_KI = "set_ki"
SERVICE_SET_KP = "set_kp"
SERVICE_SET_KD = "set_kd"

PID_DIR_DIRECT = "direct"
PID_DIR_REVERSE = "reverse"

DEFAULT_MODE = MODE_SLIDER
DEFAULT_CYCLE_TIME = {"seconds": 30}

DEFAULT_PID_DIR = PID_DIR_DIRECT
DEFAULT_PID_KI = 1.0
DEFAULT_PID_KP = 0.1
DEFAULT_PID_KD = 0.0
