
import re as _re
from . import device_names as _device_names

_kick_in_re = _re.compile('BOPM-KICKERINJ.*')
_kick_ex_re = _re.compile('BOPM-KICKEREX.*')

def get_pulse_curve_mapping(accelerator):
    """Get mapping from pulsed magnet to pulse curve file names

    Returns dict.
    """
    pulsed_magnets = _device_names.get_device_names(accelerator, 'bopm')

    pc = dict()
    for name in pulsed_magnets:
        if _kick_in_re.match(name) is not None: pc[name] = 'bopm-kickinj-pulse.txt'
        elif _kick_ex_re.match(name) is not None: pc[name] = 'bopm-kickex-pulse.txt'

    return pc

def get_magnet_delay_mapping(accelerator):
    """Get mapping from pulsed magnet to timing delay

    Returns dict.
    """
    pulsed_magnets = _device_names.get_device_names(accelerator, 'bopm')
    timing_variables = _device_names.get_device_names(accelerator, 'boti')

    mapping = dict()
    for magnet in pulsed_magnets.keys():
        magnet_name = magnet.split('-')[1]
        for timing_variable in timing_variables.keys():
            name = timing_variable[5:]
            if _re.match(magnet_name, name) is not None and 'DELAY' in name:
                mapping[magnet] = timing_variable

    inverse_mapping = dict()
    for key, value in mapping.items():
        inverse_mapping[value] = key

    return mapping, inverse_mapping


def get_magnet_enabled_mapping(accelerator):
    """Get mapping from pulsed magnet to timing enabled

    Returns dict.
    """
    pulsed_magnets = _device_names.get_device_names(accelerator, 'bopm')
    timing_variables = _device_names.get_device_names(accelerator, 'boti')

    mapping = dict()
    for magnet in pulsed_magnets.keys():
        magnet_name = magnet.split('-')[1]
        for timing_variable in timing_variables.keys():
            name = timing_variable[5:]
            if _re.match(magnet_name, name) is not None and 'ENABLED' in name:
                mapping[magnet] = timing_variable


    inverse_mapping = dict()
    for key, value in mapping.items():
        inverse_mapping[value] = key


    return mapping, inverse_mapping
