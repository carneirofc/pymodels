
from .lattice import energy
from .lattice import single_bunch_charge
from .lattice import multi_bunch_charge
from .lattice import single_bunch_pulse_duration
from .lattice import multi_bunch_pulse_duration
from .lattice import frequency
from .lattice import default_optics_mode
from .lattice import default_operation_mode

from .accelerator import accelerator_data
from .accelerator import create_accelerator

from .families import get_family_data
from .families import family_mapping
from .families import get_section_name_mapping

from . import virtual_accel_interface
device_names  = virtual_accel_interface.LIDeviceNames()
del virtual_accel_interface

# -- default accelerator values for LI_V01_01-
lattice_version             = accelerator_data['lattice_version']
get_device_names            = device_names.get_device_names
