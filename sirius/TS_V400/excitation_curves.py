
import re as _re
from . import record_names as _record_names


_bend_re = _re.compile('TSMA-B.*')
_q_re    = _re.compile('TSMA-Q.*')
_c_re    = _re.compile('TSMA-C.*')
_sep_re  = _re.compile('TSPM-S.*')


def get_excitation_curve_mapping(accelerator):
    """Get mapping from magnet to excitation curve file names

    Returns dict.
    """
    magnets = _record_names.get_magnet_names(accelerator)

    ec = dict()
    for name in magnets:
        if _bend_re.match(name) is not None: ec[name] = 'tsma-bend.txt'
        elif _q_re.match(name) is not None: ec[name] = 'tsma-q.txt'
        elif _c_re.match(name) is not None: ec[name] = 'tsma-c.txt'
        elif _sep_re.match(name) is not None: ec[name] = 'tspm-sep.txt'
        else: ec[name] = 'tsma-q.txt'

    return ec
