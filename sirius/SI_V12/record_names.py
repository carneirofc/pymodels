
from . import families as _families


def get_record_names(accelerator, subsystem = None):
    """Return a dictionary of record names for given subsystem
    each entry is another dictionary of model families whose
    values are the indices in the pyaccel model of the magnets
    that belong to the family. The magnet models ca be segmented,
    in which case the value is a python list of lists."""

    if not isinstance(accelerator, dict):
        family_data = _families.get_family_data(accelerator)
    else:
        family_data = accelerator

    if subsystem == None:
        subsystems = ['sipa', 'sidi', 'sirf', 'sips', 'siti']
        record_names_dict = {}
        for subsystem in subsystems:
            record_names_dict.update(get_record_names(family_data, subsystem))
        return record_names_dict

    if subsystem.lower() == 'sirf':
        indices = family_data['cav']['index']
        _dict = {
            'SIRF-FREQUENCY':{'cav':indices},
            'SIRF-VOLTAGE':{'cav':indices},
        }
        return _dict

    if subsystem.lower() == 'sipa':
        _dict = {
                'SIPA-CHROMX':{},
                'SIPA-CHROMY':{},
                'SIPA-LIFETIME':{},
                'SIPA-BLIFETIME':{},
                'SIPA-SIGX':{},
                'SIPA-SIGY':{},
                'SIPA-SIGS':{},
                'SIPA-EMITX':{},
                'SIPA-EMITY':{},
                'SIPA-SIGX':{},
                'SIPA-SIGY':{},
                'SIPA-SIGS':{},
        }
        return _dict

    if subsystem.lower() == 'sidi':
        prefix = 'SIDI-'

        _dict = {
                'SIDI-TUNEH':{},
                'SIDI-TUNEV':{},
                'SIDI-TUNES':{},
                'SIDI-CURRENT':{},
                'SIDI-BCURRENT':{},
        }
        bpm_dict = get_element_names(family_data, element = 'bpm', prefix = prefix)
        _dict.update(bpm_dict)
        bpm_fam_dict = get_family_names(family_data, family = 'bpm', prefix = prefix)
        _dict.update(bpm_fam_dict)
        return _dict

    if subsystem.lower() == 'sips':
        prefix = 'SIPS-'

        element_dict = {}
        element_dict.update(get_element_names(family_data, element = 'quad', prefix = prefix))
        element_dict.update(get_element_names(family_data, element = 'sext', prefix = prefix))
        element_dict.update(get_element_names(family_data, element = 'hcorr', prefix = prefix))
        element_dict.update(get_element_names(family_data, element = 'vcorr', prefix = prefix))
        element_dict.update(get_element_names(family_data, element = 'qs', prefix = prefix))

        family_dict = {}
        family_dict.update(get_family_names(family_data, family = 'bend', prefix = prefix))
        family_dict.update(get_family_names(family_data, family = 'quad', prefix = prefix))
        family_dict.update(get_family_names(family_data, family = 'sext', prefix = prefix))

        _dict = {}
        _dict.update(element_dict)
        _dict.update(family_dict)
        return _dict

    if subsystem.lower() == 'sima':
        prefix = 'SIMA-'

        element_dict = {}
        element_dict.update(get_element_names(family_data, element = 'bend', prefix = prefix))
        element_dict.update(get_element_names(family_data, element = 'quad', prefix = prefix))
        element_dict.update(get_element_names(family_data, element = 'sext', prefix = prefix))
        element_dict.update(get_element_names(family_data, element = 'hcorr', prefix = prefix))
        element_dict.update(get_element_names(family_data, element = 'vcorr', prefix = prefix))
        element_dict.update(get_element_names(family_data, element = 'qs', prefix = prefix))

        return element_dict

    if subsystem.lower() == 'siti':
        _dict = {
                'SITI-KICKINJ-ENABLED':{},
                'SITI-KICKINJ-DELAY':{},
                'SITI-PMM-ENABLED':{},
                'SITI-PMM-DELAY':{},
        }
        return _dict

    else:
        raise Exception('Subsystem %s not found'%subsystem)


def get_family_names(accelerator, family = None, prefix = ''):

    if not isinstance(accelerator, dict):
        family_data = _families.get_family_data(accelerator)
    else:
        family_data = accelerator

    if family == None:

        family_names = []
        family_names += _families.families_dipoles()
        family_names += _families.families_quadrupoles()
        family_names += _families.families_sextupoles()
        family_names += ['bpm']

        _dict = {}
        for family in family_names:
            _dict.update(get_family_names(family_data, family, prefix = prefix))
        return _dict

    if family.lower() == 'bend':
        _dict = { prefix + 'BEND-FAM' :
            {'b1' : family_data['b1']['index'],
             'b2' : family_data['b2']['index'],
            }
        }
        return _dict

    if family.lower() == 'quad':
        family_names = _families.families_quadrupoles()
        _dict = {}
        for family in family_names:
            _dict.update(get_family_names(family_data, family, prefix = prefix))
        return _dict

    if family.lower() == 'sext':
        family_names = _families.families_sextupoles()
        _dict = {}
        for family in family_names:
            _dict.update(get_family_names(family_data, family, prefix = prefix))
        return _dict

    if family.lower() == 'bpm':
        indices = family_data['bpm']['index']
        _dict = {prefix + 'BPM-FAM-X': {'bpm': indices},
                 prefix + 'BPM-FAM-Y': {'bpm': indices},
                }
        return _dict

    if family.lower() == 'qfa':
        indices = family_data['qfa']['index']
        _dict = {prefix + 'QFA-FAM': {'qfa': indices}}
        return _dict

    if family.lower() == 'qda':
        indices = family_data['qda']['index']
        _dict = {prefix + 'QDA-FAM': {'qda': indices}}
        return _dict

    if family.lower() == 'qfb':
        indices = family_data['qfb']['index']
        _dict = {prefix + 'QFB-FAM': {'qfb': indices}}
        return _dict

    if family.lower() == 'qdb1':
        indices = family_data['qdb1']['index']
        _dict = {prefix + 'QDB1-FAM': {'qdb1': indices}}
        return _dict

    if family.lower() == 'qdb2':
        indices = family_data['qdb2']['index']
        _dict = {prefix + 'QDB2-FAM': {'qdb2': indices}}
        return _dict

    if family.lower() == 'qf1':
        indices = family_data['qf1']['index']
        _dict = {prefix + 'QF1-FAM': {'qf1': indices}}
        return _dict

    if family.lower() == 'qf2':
        indices = family_data['qf2']['index']
        _dict = {prefix + 'QF2-FAM': {'qf2': indices}}
        return _dict

    if family.lower() == 'qf3':
        indices = family_data['qf3']['index']
        _dict = {prefix + 'QF3-FAM': {'qf3': indices}}
        return _dict

    if family.lower() == 'qf4':
        indices = family_data['qf4']['index']
        _dict = {prefix + 'QF4-FAM': {'qf4': indices}}
        return _dict

    if family.lower() == 'sfa':
        indices = family_data['sfa']['index']
        _dict = {prefix + 'SFA-FAM': {'sfa': indices}}
        return _dict

    if family.lower() == 'sda':
        indices = family_data['sda']['index']
        _dict = {prefix + 'SDA-FAM': {'sda': indices}}
        return _dict

    if family.lower() == 'sd1j':
        indices = family_data['sd1j']['index']
        _dict = {prefix + 'SD1J-FAM': {'sd1j': indices}}
        return _dict

    if family.lower() == 'sf1j':
        indices = family_data['sf1j']['index']
        _dict = {prefix + 'SF1J-FAM': {'sf1j': indices}}
        return _dict

    if family.lower() == 'sd2j':
        indices = family_data['sd2j']['index']
        _dict = {prefix + 'SD2J-FAM': {'sd2j': indices}}
        return _dict

    if family.lower() == 'sd3j':
        indices = family_data['sd3j']['index']
        _dict = {prefix + 'SD3J-FAM': {'sd3j': indices}}
        return _dict

    if family.lower() == 'sf2j':
        indices = family_data['sf2j']['index']
        _dict = {prefix + 'SF2J-FAM': {'sf2j': indices}}
        return _dict

    if family.lower() == 'sf2k':
        indices = family_data['sf2k']['index']
        _dict = {prefix + 'SF2K-FAM': {'sf2k': indices}}
        return _dict

    if family.lower() == 'sd3k':
        indices = family_data['sd3k']['index']
        _dict = {prefix + 'SD3K-FAM': {'sd3k': indices}}
        return _dict

    if family.lower() == 'sd2k':
        indices = family_data['sd2k']['index']
        _dict = {prefix + 'SD2K-FAM': {'sd2k': indices}}
        return _dict

    if family.lower() == 'sf1k':
        indices = family_data['sf1k']['index']
        _dict = {prefix + 'SF1K-FAM': {'sf1k': indices}}
        return _dict

    if family.lower() == 'sd1k':
        indices = family_data['sd1k']['index']
        _dict = {prefix + 'SD1K-FAM': {'sd1k': indices}}
        return _dict

    if family.lower() == 'sdb':
        indices = family_data['sdb']['index']
        _dict = {prefix + 'SDB-FAM': {'sdb': indices}}
        return _dict

    if family.lower() == 'sfb':
        indices = family_data['sfb']['index']
        _dict = {prefix + 'SFB-FAM': {'sfb': indices}}
        return _dict

    else:
        raise Exception('Family %s not found'%family)


def get_element_names(accelerator, element = None, prefix = ''):

    if not isinstance(accelerator, dict):
        family_data = _families.get_family_data(accelerator)
    else:
        family_data = accelerator

    if element == None:
        elements = []
        elements += _families.families_dipoles()
        elements += _families.families_quadrupoles()
        elements += _families.families_sextupoles()
        elements += _families.families_horizontal_correctors()
        elements += _families.families_vertical_correctors()
        elements += _families.families_skew_correctors()
        elements += ['bpm']

        _dict = {}
        for element in elements:
            _dict.update(get_element_names(family_data, element, prefix = prefix))
        return _dict

    if element.lower() == 'bend':
        _dict = {}
        _dict.update(get_element_names(family_data, 'b1', prefix = prefix))
        _dict.update(get_element_names(family_data, 'b2', prefix = prefix))
        _dict.update(get_element_names(family_data, 'bc', prefix = prefix))
        return _dict

    if element.lower() == 'quad':
        elements = _families.families_quadrupoles()
        _dict = {}
        for element in elements:
            _dict.update(get_element_names(family_data, element, prefix = prefix))
        return _dict

    if element.lower() == 'sext':
        elements = _families.families_sextupoles()
        _dict = {}
        for element in elements:
            _dict.update(get_element_names(family_data, element, prefix = prefix))
        return _dict

    if element.lower() == 'corr':
        elements = _families.families_horizontal_correctors()
        elements += _families.families_vertical_correctors()
        _dict = {}
        for element in elements:
            _dict.update(get_element_names(family_data, element, prefix = prefix))
        return _dict

    if element.lower() == 'hcorr':
        elements = _families.families_horizontal_correctors()
        _dict = {}
        for element in elements:
            _dict.update(get_element_names(family_data, element, prefix = prefix))
        return _dict

    if element.lower() == 'vcorr':
        elements = _families.families_vertical_correctors()
        _dict = {}
        for element in elements:
            _dict.update(get_element_names(family_data, element, prefix = prefix))
        return _dict

    if element.lower() == 'bpm':
        prefix = prefix + 'BPM-'
        _dict = {
            # Sector 01
            prefix + '01M1'   : { 'bpm' : [family_data['bpm']['index'][159]]},
            prefix + '01M2'   : { 'bpm' : [family_data['bpm']['index'][0]]},
            prefix + '01C1-A' : { 'bpm' : [family_data['bpm']['index'][1]]},
            prefix + '01C1-B' : { 'bpm' : [family_data['bpm']['index'][2]]},
            prefix + '01C2'   : { 'bpm' : [family_data['bpm']['index'][3]]},
            prefix + '01C3-A' : { 'bpm' : [family_data['bpm']['index'][4]]},
            prefix + '01C3-B' : { 'bpm' : [family_data['bpm']['index'][5]]},
            prefix + '01C4'   : { 'bpm' : [family_data['bpm']['index'][6]]},

            # Sector 02
            prefix + '02M1'   : { 'bpm' : [family_data['bpm']['index'][7]]},
            prefix + '02M2'   : { 'bpm' : [family_data['bpm']['index'][8]]},
            prefix + '02C1-A' : { 'bpm' : [family_data['bpm']['index'][9]]},
            prefix + '02C1-B' : { 'bpm' : [family_data['bpm']['index'][10]]},
            prefix + '02C2'   : { 'bpm' : [family_data['bpm']['index'][11]]},
            prefix + '02C3-A' : { 'bpm' : [family_data['bpm']['index'][12]]},
            prefix + '02C3-B' : { 'bpm' : [family_data['bpm']['index'][13]]},
            prefix + '02C4'   : { 'bpm' : [family_data['bpm']['index'][14]]},

            # Sector 03
            prefix + '03M1'   : { 'bpm' : [family_data['bpm']['index'][15]]},
            prefix + '03M2'   : { 'bpm' : [family_data['bpm']['index'][16]]},
            prefix + '03C1-A' : { 'bpm' : [family_data['bpm']['index'][17]]},
            prefix + '03C1-B' : { 'bpm' : [family_data['bpm']['index'][18]]},
            prefix + '03C2'   : { 'bpm' : [family_data['bpm']['index'][19]]},
            prefix + '03C3-A' : { 'bpm' : [family_data['bpm']['index'][20]]},
            prefix + '03C3-B' : { 'bpm' : [family_data['bpm']['index'][21]]},
            prefix + '03C4'   : { 'bpm' : [family_data['bpm']['index'][22]]},

            # Sector 04
            prefix + '04M1'   : { 'bpm' : [family_data['bpm']['index'][23]]},
            prefix + '04M2'   : { 'bpm' : [family_data['bpm']['index'][24]]},
            prefix + '04C1-A' : { 'bpm' : [family_data['bpm']['index'][25]]},
            prefix + '04C1-B' : { 'bpm' : [family_data['bpm']['index'][26]]},
            prefix + '04C2'   : { 'bpm' : [family_data['bpm']['index'][27]]},
            prefix + '04C3-A' : { 'bpm' : [family_data['bpm']['index'][28]]},
            prefix + '04C3-B' : { 'bpm' : [family_data['bpm']['index'][29]]},
            prefix + '04C4'   : { 'bpm' : [family_data['bpm']['index'][30]]},

            # Sector 05
            prefix + '05M1'   : { 'bpm' : [family_data['bpm']['index'][31]]},
            prefix + '05M2'   : { 'bpm' : [family_data['bpm']['index'][32]]},
            prefix + '05C1-A' : { 'bpm' : [family_data['bpm']['index'][33]]},
            prefix + '05C1-B' : { 'bpm' : [family_data['bpm']['index'][34]]},
            prefix + '05C2'   : { 'bpm' : [family_data['bpm']['index'][35]]},
            prefix + '05C3-A' : { 'bpm' : [family_data['bpm']['index'][36]]},
            prefix + '05C3-B' : { 'bpm' : [family_data['bpm']['index'][37]]},
            prefix + '05C4'   : { 'bpm' : [family_data['bpm']['index'][38]]},

            # Sector 06
            prefix + '06M1'   : { 'bpm' : [family_data['bpm']['index'][39]]},
            prefix + '06M2'   : { 'bpm' : [family_data['bpm']['index'][40]]},
            prefix + '06C1-A' : { 'bpm' : [family_data['bpm']['index'][41]]},
            prefix + '06C1-B' : { 'bpm' : [family_data['bpm']['index'][42]]},
            prefix + '06C2'   : { 'bpm' : [family_data['bpm']['index'][43]]},
            prefix + '06C3-A' : { 'bpm' : [family_data['bpm']['index'][44]]},
            prefix + '06C3-B' : { 'bpm' : [family_data['bpm']['index'][45]]},
            prefix + '06C4'   : { 'bpm' : [family_data['bpm']['index'][46]]},

            # Sector 07
            prefix + '07M1'   : { 'bpm' : [family_data['bpm']['index'][47]]},
            prefix + '07M2'   : { 'bpm' : [family_data['bpm']['index'][48]]},
            prefix + '07C1-A' : { 'bpm' : [family_data['bpm']['index'][49]]},
            prefix + '07C1-B' : { 'bpm' : [family_data['bpm']['index'][50]]},
            prefix + '07C2'   : { 'bpm' : [family_data['bpm']['index'][51]]},
            prefix + '07C3-A' : { 'bpm' : [family_data['bpm']['index'][52]]},
            prefix + '07C3-B' : { 'bpm' : [family_data['bpm']['index'][53]]},
            prefix + '07C4'   : { 'bpm' : [family_data['bpm']['index'][54]]},

            # Sector 08
            prefix + '08M1'   : { 'bpm' : [family_data['bpm']['index'][55]]},
            prefix + '08M2'   : { 'bpm' : [family_data['bpm']['index'][56]]},
            prefix + '08C1-A' : { 'bpm' : [family_data['bpm']['index'][57]]},
            prefix + '08C1-B' : { 'bpm' : [family_data['bpm']['index'][58]]},
            prefix + '08C2'   : { 'bpm' : [family_data['bpm']['index'][59]]},
            prefix + '08C3-A' : { 'bpm' : [family_data['bpm']['index'][60]]},
            prefix + '08C3-B' : { 'bpm' : [family_data['bpm']['index'][61]]},
            prefix + '08C4'   : { 'bpm' : [family_data['bpm']['index'][62]]},

            # Sector 09
            prefix + '09M1'   : { 'bpm' : [family_data['bpm']['index'][63]]},
            prefix + '09M2'   : { 'bpm' : [family_data['bpm']['index'][64]]},
            prefix + '09C1-A' : { 'bpm' : [family_data['bpm']['index'][65]]},
            prefix + '09C1-B' : { 'bpm' : [family_data['bpm']['index'][66]]},
            prefix + '09C2'   : { 'bpm' : [family_data['bpm']['index'][67]]},
            prefix + '09C3-A' : { 'bpm' : [family_data['bpm']['index'][68]]},
            prefix + '09C3-B' : { 'bpm' : [family_data['bpm']['index'][69]]},
            prefix + '09C4'   : { 'bpm' : [family_data['bpm']['index'][70]]},

            # Sector 10
            prefix + '10M1'   : { 'bpm' : [family_data['bpm']['index'][71]]},
            prefix + '10M2'   : { 'bpm' : [family_data['bpm']['index'][72]]},
            prefix + '10C1-A' : { 'bpm' : [family_data['bpm']['index'][73]]},
            prefix + '10C1-B' : { 'bpm' : [family_data['bpm']['index'][74]]},
            prefix + '10C2'   : { 'bpm' : [family_data['bpm']['index'][75]]},
            prefix + '10C3-A' : { 'bpm' : [family_data['bpm']['index'][76]]},
            prefix + '10C3-B' : { 'bpm' : [family_data['bpm']['index'][77]]},
            prefix + '10C4'   : { 'bpm' : [family_data['bpm']['index'][78]]},

            # Sector 11
            prefix + '11M1'   : { 'bpm' : [family_data['bpm']['index'][79]]},
            prefix + '11M2'   : { 'bpm' : [family_data['bpm']['index'][80]]},
            prefix + '11C1-A' : { 'bpm' : [family_data['bpm']['index'][81]]},
            prefix + '11C1-B' : { 'bpm' : [family_data['bpm']['index'][82]]},
            prefix + '11C2'   : { 'bpm' : [family_data['bpm']['index'][83]]},
            prefix + '11C3-A' : { 'bpm' : [family_data['bpm']['index'][84]]},
            prefix + '11C3-B' : { 'bpm' : [family_data['bpm']['index'][85]]},
            prefix + '11C4'   : { 'bpm' : [family_data['bpm']['index'][86]]},

            # Sector 12
            prefix + '12M1'   : { 'bpm' : [family_data['bpm']['index'][87]]},
            prefix + '12M2'   : { 'bpm' : [family_data['bpm']['index'][88]]},
            prefix + '12C1-A' : { 'bpm' : [family_data['bpm']['index'][89]]},
            prefix + '12C1-B' : { 'bpm' : [family_data['bpm']['index'][90]]},
            prefix + '12C2'   : { 'bpm' : [family_data['bpm']['index'][91]]},
            prefix + '12C3-A' : { 'bpm' : [family_data['bpm']['index'][92]]},
            prefix + '12C3-B' : { 'bpm' : [family_data['bpm']['index'][93]]},
            prefix + '12C4'   : { 'bpm' : [family_data['bpm']['index'][94]]},

            # Sector 13
            prefix + '13M1'   : { 'bpm' : [family_data['bpm']['index'][95]]},
            prefix + '13M2'   : { 'bpm' : [family_data['bpm']['index'][96]]},
            prefix + '13C1-A' : { 'bpm' : [family_data['bpm']['index'][97]]},
            prefix + '13C1-B' : { 'bpm' : [family_data['bpm']['index'][98]]},
            prefix + '13C2'   : { 'bpm' : [family_data['bpm']['index'][99]]},
            prefix + '13C3-A' : { 'bpm' : [family_data['bpm']['index'][100]]},
            prefix + '13C3-B' : { 'bpm' : [family_data['bpm']['index'][101]]},
            prefix + '13C4'   : { 'bpm' : [family_data['bpm']['index'][102]]},

            # Sector 14
            prefix + '14M1'   : { 'bpm' : [family_data['bpm']['index'][103]]},
            prefix + '14M2'   : { 'bpm' : [family_data['bpm']['index'][104]]},
            prefix + '14C1-A' : { 'bpm' : [family_data['bpm']['index'][105]]},
            prefix + '14C1-B' : { 'bpm' : [family_data['bpm']['index'][106]]},
            prefix + '14C2'   : { 'bpm' : [family_data['bpm']['index'][107]]},
            prefix + '14C3-A' : { 'bpm' : [family_data['bpm']['index'][108]]},
            prefix + '14C3-B' : { 'bpm' : [family_data['bpm']['index'][109]]},
            prefix + '14C4'   : { 'bpm' : [family_data['bpm']['index'][110]]},

            # Sector 15
            prefix + '15M1'   : { 'bpm' : [family_data['bpm']['index'][111]]},
            prefix + '15M2'   : { 'bpm' : [family_data['bpm']['index'][112]]},
            prefix + '15C1-A' : { 'bpm' : [family_data['bpm']['index'][113]]},
            prefix + '15C1-B' : { 'bpm' : [family_data['bpm']['index'][114]]},
            prefix + '15C2'   : { 'bpm' : [family_data['bpm']['index'][115]]},
            prefix + '15C3-A' : { 'bpm' : [family_data['bpm']['index'][116]]},
            prefix + '15C3-B' : { 'bpm' : [family_data['bpm']['index'][117]]},
            prefix + '15C4'   : { 'bpm' : [family_data['bpm']['index'][118]]},

            # Sector 16
            prefix + '16M1'   : { 'bpm' : [family_data['bpm']['index'][119]]},
            prefix + '16M2'   : { 'bpm' : [family_data['bpm']['index'][120]]},
            prefix + '16C1-A' : { 'bpm' : [family_data['bpm']['index'][121]]},
            prefix + '16C1-B' : { 'bpm' : [family_data['bpm']['index'][122]]},
            prefix + '16C2'   : { 'bpm' : [family_data['bpm']['index'][123]]},
            prefix + '16C3-A' : { 'bpm' : [family_data['bpm']['index'][124]]},
            prefix + '16C3-B' : { 'bpm' : [family_data['bpm']['index'][125]]},
            prefix + '16C4'   : { 'bpm' : [family_data['bpm']['index'][126]]},

            # Sector 17
            prefix + '17M1'   : { 'bpm' : [family_data['bpm']['index'][127]]},
            prefix + '17M2'   : { 'bpm' : [family_data['bpm']['index'][128]]},
            prefix + '17C1-A' : { 'bpm' : [family_data['bpm']['index'][129]]},
            prefix + '17C1-B' : { 'bpm' : [family_data['bpm']['index'][130]]},
            prefix + '17C2'   : { 'bpm' : [family_data['bpm']['index'][131]]},
            prefix + '17C3-A' : { 'bpm' : [family_data['bpm']['index'][132]]},
            prefix + '17C3-B' : { 'bpm' : [family_data['bpm']['index'][133]]},
            prefix + '17C4'   : { 'bpm' : [family_data['bpm']['index'][134]]},

            # Sector 18
            prefix + '18M1'   : { 'bpm' : [family_data['bpm']['index'][135]]},
            prefix + '18M2'   : { 'bpm' : [family_data['bpm']['index'][136]]},
            prefix + '18C1-A' : { 'bpm' : [family_data['bpm']['index'][137]]},
            prefix + '18C1-B' : { 'bpm' : [family_data['bpm']['index'][138]]},
            prefix + '18C2'   : { 'bpm' : [family_data['bpm']['index'][139]]},
            prefix + '18C3-A' : { 'bpm' : [family_data['bpm']['index'][140]]},
            prefix + '18C3-B' : { 'bpm' : [family_data['bpm']['index'][141]]},
            prefix + '18C4'   : { 'bpm' : [family_data['bpm']['index'][142]]},

            # Sector 19
            prefix + '19M1'   : { 'bpm' : [family_data['bpm']['index'][143]]},
            prefix + '19M2'   : { 'bpm' : [family_data['bpm']['index'][144]]},
            prefix + '19C1-A' : { 'bpm' : [family_data['bpm']['index'][145]]},
            prefix + '19C1-B' : { 'bpm' : [family_data['bpm']['index'][146]]},
            prefix + '19C2'   : { 'bpm' : [family_data['bpm']['index'][147]]},
            prefix + '19C3-A' : { 'bpm' : [family_data['bpm']['index'][148]]},
            prefix + '19C3-B' : { 'bpm' : [family_data['bpm']['index'][149]]},
            prefix + '19C4'   : { 'bpm' : [family_data['bpm']['index'][150]]},

            # Sector 20
            prefix + '20M1'   : { 'bpm' : [family_data['bpm']['index'][151]]},
            prefix + '20M2'   : { 'bpm' : [family_data['bpm']['index'][152]]},
            prefix + '20C1-A' : { 'bpm' : [family_data['bpm']['index'][153]]},
            prefix + '20C1-B' : { 'bpm' : [family_data['bpm']['index'][154]]},
            prefix + '20C2'   : { 'bpm' : [family_data['bpm']['index'][155]]},
            prefix + '20C3-A' : { 'bpm' : [family_data['bpm']['index'][156]]},
            prefix + '20C3-B' : { 'bpm' : [family_data['bpm']['index'][157]]},
            prefix + '20C4'   : { 'bpm' : [family_data['bpm']['index'][158]]},
        }
        return _dict


    if element.lower() == 'qs':
        prefix = prefix + 'QS-'
        _dict = {
            #Sector 01
            prefix + '01M1'   : { 'qs' : [family_data['qs']['index'][79]]},
			prefix + '01M2'   : { 'qs' : [family_data['qs']['index'][0]]},
			prefix + '01C1'   : { 'qs' : [family_data['qs']['index'][1]]},
			prefix + '01C4'   : { 'qs' : [family_data['qs']['index'][2]]},

            #Sector 02
			prefix + '02M1'   : { 'qs' : [family_data['qs']['index'][3]]},
			prefix + '02M2'   : { 'qs' : [family_data['qs']['index'][4]]},
			prefix + '02C1'   : { 'qs' : [family_data['qs']['index'][5]]},
			prefix + '02C4'   : { 'qs' : [family_data['qs']['index'][6]]},

            #Sector 03
			prefix + '03M1'   : { 'qs' : [family_data['qs']['index'][7]]},
			prefix + '03M2'   : { 'qs' : [family_data['qs']['index'][8]]},
			prefix + '03C1'   : { 'qs' : [family_data['qs']['index'][9]]},
			prefix + '03C4'   : { 'qs' : [family_data['qs']['index'][10]]},

            #Sector 04
            prefix + '04M1'   : { 'qs' : [family_data['qs']['index'][11]]},
			prefix + '04M2'   : { 'qs' : [family_data['qs']['index'][12]]},
			prefix + '04C1'   : { 'qs' : [family_data['qs']['index'][13]]},
			prefix + '04C4'   : { 'qs' : [family_data['qs']['index'][14]]},

            #Sector 05
            prefix + '05M1'   : { 'qs' : [family_data['qs']['index'][15]]},
			prefix + '05M2'   : { 'qs' : [family_data['qs']['index'][16]]},
			prefix + '05C1'   : { 'qs' : [family_data['qs']['index'][17]]},
			prefix + '05C4'   : { 'qs' : [family_data['qs']['index'][18]]},

            #Sector 05
            prefix + '06M1'   : { 'qs' : [family_data['qs']['index'][19]]},
			prefix + '06M2'   : { 'qs' : [family_data['qs']['index'][20]]},
			prefix + '06C1'   : { 'qs' : [family_data['qs']['index'][21]]},
			prefix + '06C4'   : { 'qs' : [family_data['qs']['index'][22]]},

            #Sector 07
            prefix + '07M1'   : { 'qs' : [family_data['qs']['index'][23]]},
			prefix + '07M2'   : { 'qs' : [family_data['qs']['index'][24]]},
			prefix + '07C1'   : { 'qs' : [family_data['qs']['index'][25]]},
			prefix + '07C4'   : { 'qs' : [family_data['qs']['index'][26]]},

            #Sector 08
            prefix + '08M1'   : { 'qs' : [family_data['qs']['index'][27]]},
			prefix + '08M2'   : { 'qs' : [family_data['qs']['index'][28]]},
			prefix + '08C1'   : { 'qs' : [family_data['qs']['index'][29]]},
			prefix + '08C4'   : { 'qs' : [family_data['qs']['index'][30]]},

            #Sector 09
            prefix + '09M1'   : { 'qs' : [family_data['qs']['index'][31]]},
			prefix + '09M2'   : { 'qs' : [family_data['qs']['index'][32]]},
			prefix + '09C1'   : { 'qs' : [family_data['qs']['index'][33]]},
			prefix + '09C4'   : { 'qs' : [family_data['qs']['index'][34]]},

            #Sector 10
            prefix + '10M1'   : { 'qs' : [family_data['qs']['index'][35]]},
			prefix + '10M2'   : { 'qs' : [family_data['qs']['index'][36]]},
			prefix + '10C1'   : { 'qs' : [family_data['qs']['index'][37]]},
			prefix + '10C4'   : { 'qs' : [family_data['qs']['index'][38]]},

            #Sector 11
            prefix + '11M1'   : { 'qs' : [family_data['qs']['index'][39]]},
			prefix + '11M2'   : { 'qs' : [family_data['qs']['index'][40]]},
			prefix + '11C1'   : { 'qs' : [family_data['qs']['index'][41]]},
			prefix + '11C4'   : { 'qs' : [family_data['qs']['index'][42]]},

            #Sector 12
            prefix + '12M1'   : { 'qs' : [family_data['qs']['index'][43]]},
			prefix + '12M2'   : { 'qs' : [family_data['qs']['index'][44]]},
			prefix + '12C1'   : { 'qs' : [family_data['qs']['index'][45]]},
			prefix + '12C4'   : { 'qs' : [family_data['qs']['index'][46]]},

            #Sector 13
            prefix + '13M1'   : { 'qs' : [family_data['qs']['index'][47]]},
			prefix + '13M2'   : { 'qs' : [family_data['qs']['index'][48]]},
			prefix + '13C1'   : { 'qs' : [family_data['qs']['index'][49]]},
			prefix + '13C4'   : { 'qs' : [family_data['qs']['index'][50]]},

            #Sector 14
            prefix + '14M1'   : { 'qs' : [family_data['qs']['index'][51]]},
			prefix + '14M2'   : { 'qs' : [family_data['qs']['index'][52]]},
			prefix + '14C1'   : { 'qs' : [family_data['qs']['index'][53]]},
			prefix + '14C4'   : { 'qs' : [family_data['qs']['index'][54]]},

            #Sector 15
            prefix + '15M1'   : { 'qs' : [family_data['qs']['index'][55]]},
			prefix + '15M2'   : { 'qs' : [family_data['qs']['index'][56]]},
			prefix + '15C1'   : { 'qs' : [family_data['qs']['index'][57]]},
			prefix + '15C4'   : { 'qs' : [family_data['qs']['index'][58]]},

            #Sector 16
            prefix + '16M1'   : { 'qs' : [family_data['qs']['index'][59]]},
			prefix + '16M2'   : { 'qs' : [family_data['qs']['index'][60]]},
			prefix + '16C1'   : { 'qs' : [family_data['qs']['index'][61]]},
			prefix + '16C4'   : { 'qs' : [family_data['qs']['index'][62]]},

            #Sector 17
            prefix + '17M1'   : { 'qs' : [family_data['qs']['index'][63]]},
			prefix + '17M2'   : { 'qs' : [family_data['qs']['index'][64]]},
			prefix + '17C1'   : { 'qs' : [family_data['qs']['index'][65]]},
			prefix + '17C4'   : { 'qs' : [family_data['qs']['index'][66]]},

            #Sector 18
            prefix + '18M1'   : { 'qs' : [family_data['qs']['index'][67]]},
			prefix + '18M2'   : { 'qs' : [family_data['qs']['index'][68]]},
			prefix + '18C1'   : { 'qs' : [family_data['qs']['index'][69]]},
			prefix + '18C4'   : { 'qs' : [family_data['qs']['index'][70]]},

            #Sector 19
            prefix + '19M1'   : { 'qs' : [family_data['qs']['index'][71]]},
			prefix + '19M2'   : { 'qs' : [family_data['qs']['index'][72]]},
			prefix + '19C1'   : { 'qs' : [family_data['qs']['index'][73]]},
			prefix + '19C4'   : { 'qs' : [family_data['qs']['index'][74]]},

            #Sector 20
            prefix + '20M1'   : { 'qs' : [family_data['qs']['index'][75]]},
			prefix + '20M2'   : { 'qs' : [family_data['qs']['index'][76]]},
			prefix + '20C1'   : { 'qs' : [family_data['qs']['index'][77]]},
			prefix + '20C4'   : { 'qs' : [family_data['qs']['index'][78]]},
		}
        return _dict

    if element.lower() == 'b1':
        prefix = prefix + 'B1-'
        _dict = {
            prefix + '01-A'   : {'b1' : [family_data['b1']['index'][0]]},
            prefix + '01-B'   : {'b1' : [family_data['b1']['index'][1]]},
            prefix + '02-A'   : {'b1' : [family_data['b1']['index'][2]]},
            prefix + '02-B'   : {'b1' : [family_data['b1']['index'][3]]},
            prefix + '03-A'   : {'b1' : [family_data['b1']['index'][4]]},
            prefix + '03-B'   : {'b1' : [family_data['b1']['index'][5]]},
            prefix + '04-A'   : {'b1' : [family_data['b1']['index'][6]]},
            prefix + '04-B'   : {'b1' : [family_data['b1']['index'][7]]},
            prefix + '05-A'   : {'b1' : [family_data['b1']['index'][8]]},
            prefix + '05-B'   : {'b1' : [family_data['b1']['index'][9]]},
            prefix + '06-A'   : {'b1' : [family_data['b1']['index'][10]]},
            prefix + '06-B'   : {'b1' : [family_data['b1']['index'][11]]},
            prefix + '07-A'   : {'b1' : [family_data['b1']['index'][12]]},
            prefix + '07-B'   : {'b1' : [family_data['b1']['index'][13]]},
            prefix + '08-A'   : {'b1' : [family_data['b1']['index'][14]]},
            prefix + '08-B'   : {'b1' : [family_data['b1']['index'][15]]},
            prefix + '09-A'   : {'b1' : [family_data['b1']['index'][16]]},
            prefix + '09-B'   : {'b1' : [family_data['b1']['index'][17]]},
            prefix + '10-A'   : {'b1' : [family_data['b1']['index'][18]]},
            prefix + '10-B'   : {'b1' : [family_data['b1']['index'][19]]},
            prefix + '11-A'   : {'b1' : [family_data['b1']['index'][20]]},
            prefix + '11-B'   : {'b1' : [family_data['b1']['index'][21]]},
            prefix + '12-A'   : {'b1' : [family_data['b1']['index'][22]]},
            prefix + '12-B'   : {'b1' : [family_data['b1']['index'][23]]},
            prefix + '13-A'   : {'b1' : [family_data['b1']['index'][24]]},
            prefix + '13-B'   : {'b1' : [family_data['b1']['index'][25]]},
            prefix + '14-A'   : {'b1' : [family_data['b1']['index'][26]]},
            prefix + '14-B'   : {'b1' : [family_data['b1']['index'][27]]},
            prefix + '15-A'   : {'b1' : [family_data['b1']['index'][28]]},
            prefix + '15-B'   : {'b1' : [family_data['b1']['index'][29]]},
            prefix + '16-A'   : {'b1' : [family_data['b1']['index'][30]]},
            prefix + '16-B'   : {'b1' : [family_data['b1']['index'][31]]},
            prefix + '17-A'   : {'b1' : [family_data['b1']['index'][32]]},
            prefix + '17-B'   : {'b1' : [family_data['b1']['index'][33]]},
            prefix + '18-A'   : {'b1' : [family_data['b1']['index'][34]]},
            prefix + '18-B'   : {'b1' : [family_data['b1']['index'][35]]},
            prefix + '19-A'   : {'b1' : [family_data['b1']['index'][36]]},
            prefix + '19-B'   : {'b1' : [family_data['b1']['index'][37]]},
            prefix + '20-A'   : {'b1' : [family_data['b1']['index'][38]]},
            prefix + '20-B'   : {'b1' : [family_data['b1']['index'][39]]},
        }
        return _dict

    if element.lower() == 'b2':
        prefix = prefix + 'B2-'
        _dict = {
            prefix + '01-A'   : {'b2' : [family_data['b2']['index'][0]]},
            prefix + '01-B'   : {'b2' : [family_data['b2']['index'][1]]},
            prefix + '02-A'   : {'b2' : [family_data['b2']['index'][2]]},
            prefix + '02-B'   : {'b2' : [family_data['b2']['index'][3]]},
            prefix + '03-A'   : {'b2' : [family_data['b2']['index'][4]]},
            prefix + '03-B'   : {'b2' : [family_data['b2']['index'][5]]},
            prefix + '04-A'   : {'b2' : [family_data['b2']['index'][6]]},
            prefix + '04-B'   : {'b2' : [family_data['b2']['index'][7]]},
            prefix + '05-A'   : {'b2' : [family_data['b2']['index'][8]]},
            prefix + '05-B'   : {'b2' : [family_data['b2']['index'][9]]},
            prefix + '06-A'   : {'b2' : [family_data['b2']['index'][10]]},
            prefix + '06-B'   : {'b2' : [family_data['b2']['index'][11]]},
            prefix + '07-A'   : {'b2' : [family_data['b2']['index'][12]]},
            prefix + '07-B'   : {'b2' : [family_data['b2']['index'][13]]},
            prefix + '08-A'   : {'b2' : [family_data['b2']['index'][14]]},
            prefix + '08-B'   : {'b2' : [family_data['b2']['index'][15]]},
            prefix + '09-A'   : {'b2' : [family_data['b2']['index'][16]]},
            prefix + '09-B'   : {'b2' : [family_data['b2']['index'][17]]},
            prefix + '10-A'   : {'b2' : [family_data['b2']['index'][18]]},
            prefix + '10-B'   : {'b2' : [family_data['b2']['index'][19]]},
            prefix + '11-A'   : {'b2' : [family_data['b2']['index'][20]]},
            prefix + '11-B'   : {'b2' : [family_data['b2']['index'][21]]},
            prefix + '12-A'   : {'b2' : [family_data['b2']['index'][22]]},
            prefix + '12-B'   : {'b2' : [family_data['b2']['index'][23]]},
            prefix + '13-A'   : {'b2' : [family_data['b2']['index'][24]]},
            prefix + '13-B'   : {'b2' : [family_data['b2']['index'][25]]},
            prefix + '14-A'   : {'b2' : [family_data['b2']['index'][26]]},
            prefix + '14-B'   : {'b2' : [family_data['b2']['index'][27]]},
            prefix + '15-A'   : {'b2' : [family_data['b2']['index'][28]]},
            prefix + '15-B'   : {'b2' : [family_data['b2']['index'][29]]},
            prefix + '16-A'   : {'b2' : [family_data['b2']['index'][30]]},
            prefix + '16-B'   : {'b2' : [family_data['b2']['index'][31]]},
            prefix + '17-A'   : {'b2' : [family_data['b2']['index'][32]]},
            prefix + '17-B'   : {'b2' : [family_data['b2']['index'][33]]},
            prefix + '18-A'   : {'b2' : [family_data['b2']['index'][34]]},
            prefix + '18-B'   : {'b2' : [family_data['b2']['index'][35]]},
            prefix + '19-A'   : {'b2' : [family_data['b2']['index'][36]]},
            prefix + '19-B'   : {'b2' : [family_data['b2']['index'][37]]},
            prefix + '20-A'   : {'b2' : [family_data['b2']['index'][38]]},
            prefix + '20-B'   : {'b2' : [family_data['b2']['index'][39]]},
        }
        return _dict

    if element.lower() == 'bc':
        prefix = prefix + 'BC-'
        _dict = {
            prefix + '01'   : {'bc' : sorted([family_data['bc_lf']['index'][0]] + [family_data['bc_hf']['index'][0]])},
            prefix + '02'   : {'bc' : sorted([family_data['bc_lf']['index'][1]] + [family_data['bc_hf']['index'][1]])},
            prefix + '03'   : {'bc' : sorted([family_data['bc_lf']['index'][2]] + [family_data['bc_hf']['index'][2]])},
            prefix + '04'   : {'bc' : sorted([family_data['bc_lf']['index'][3]] + [family_data['bc_hf']['index'][3]])},
            prefix + '05'   : {'bc' : sorted([family_data['bc_lf']['index'][4]] + [family_data['bc_hf']['index'][4]])},
            prefix + '06'   : {'bc' : sorted([family_data['bc_lf']['index'][5]] + [family_data['bc_hf']['index'][5]])},
            prefix + '07'   : {'bc' : sorted([family_data['bc_lf']['index'][6]] + [family_data['bc_hf']['index'][6]])},
            prefix + '08'   : {'bc' : sorted([family_data['bc_lf']['index'][7]] + [family_data['bc_hf']['index'][7]])},
            prefix + '09'   : {'bc' : sorted([family_data['bc_lf']['index'][8]] + [family_data['bc_hf']['index'][8]])},
            prefix + '10'   : {'bc' : sorted([family_data['bc_lf']['index'][9]] + [family_data['bc_hf']['index'][9]])},
            prefix + '11'   : {'bc' : sorted([family_data['bc_lf']['index'][10]] + [family_data['bc_hf']['index'][10]])},
            prefix + '12'   : {'bc' : sorted([family_data['bc_lf']['index'][11]] + [family_data['bc_hf']['index'][11]])},
            prefix + '13'   : {'bc' : sorted([family_data['bc_lf']['index'][12]] + [family_data['bc_hf']['index'][12]])},
            prefix + '14'   : {'bc' : sorted([family_data['bc_lf']['index'][13]] + [family_data['bc_hf']['index'][13]])},
            prefix + '15'   : {'bc' : sorted([family_data['bc_lf']['index'][14]] + [family_data['bc_hf']['index'][14]])},
            prefix + '16'   : {'bc' : sorted([family_data['bc_lf']['index'][15]] + [family_data['bc_hf']['index'][15]])},
            prefix + '17'   : {'bc' : sorted([family_data['bc_lf']['index'][16]] + [family_data['bc_hf']['index'][16]])},
            prefix + '18'   : {'bc' : sorted([family_data['bc_lf']['index'][17]] + [family_data['bc_hf']['index'][17]])},
            prefix + '19'   : {'bc' : sorted([family_data['bc_lf']['index'][18]] + [family_data['bc_hf']['index'][18]])},
            prefix + '20'   : {'bc' : sorted([family_data['bc_lf']['index'][19]] + [family_data['bc_hf']['index'][19]])},
        }
        return _dict

    if element.lower() == 'ch':
        prefix = prefix + 'CH-'
        _dict = {
            prefix + '01M2'   : { 'ch' : [family_data['ch']['index'][0]]},
            prefix + '01C1'   : { 'ch' : [family_data['ch']['index'][1]]},
            prefix + '01C2'   : { 'ch' : [family_data['ch']['index'][2]]},
            prefix + '01C3'   : { 'ch' : [family_data['ch']['index'][3]]},
            prefix + '01C4'   : { 'ch' : [family_data['ch']['index'][4]]},
            prefix + '02M1'   : { 'ch' : [family_data['ch']['index'][5]]},
            prefix + '02M2'   : { 'ch' : [family_data['ch']['index'][6]]},
            prefix + '02C1'   : { 'ch' : [family_data['ch']['index'][7]]},
            prefix + '02C2'   : { 'ch' : [family_data['ch']['index'][8]]},
            prefix + '02C3'   : { 'ch' : [family_data['ch']['index'][9]]},
            prefix + '02C4'   : { 'ch' : [family_data['ch']['index'][10]]},
            prefix + '03M1'   : { 'ch' : [family_data['ch']['index'][11]]},
            prefix + '03M2'   : { 'ch' : [family_data['ch']['index'][12]]},
            prefix + '03C1'   : { 'ch' : [family_data['ch']['index'][13]]},
            prefix + '03C2'   : { 'ch' : [family_data['ch']['index'][14]]},
            prefix + '03C3'   : { 'ch' : [family_data['ch']['index'][15]]},
            prefix + '03C4'   : { 'ch' : [family_data['ch']['index'][16]]},
            prefix + '04M1'   : { 'ch' : [family_data['ch']['index'][17]]},
            prefix + '04M2'   : { 'ch' : [family_data['ch']['index'][18]]},
            prefix + '04C1'   : { 'ch' : [family_data['ch']['index'][19]]},
            prefix + '04C2'   : { 'ch' : [family_data['ch']['index'][20]]},
            prefix + '04C3'   : { 'ch' : [family_data['ch']['index'][21]]},
            prefix + '04C4'   : { 'ch' : [family_data['ch']['index'][22]]},
            prefix + '05M1'   : { 'ch' : [family_data['ch']['index'][23]]},
            prefix + '05M2'   : { 'ch' : [family_data['ch']['index'][24]]},
            prefix + '05C1'   : { 'ch' : [family_data['ch']['index'][25]]},
            prefix + '05C2'   : { 'ch' : [family_data['ch']['index'][26]]},
            prefix + '05C3'   : { 'ch' : [family_data['ch']['index'][27]]},
            prefix + '05C4'   : { 'ch' : [family_data['ch']['index'][28]]},
            prefix + '06M1'   : { 'ch' : [family_data['ch']['index'][29]]},
            prefix + '06M2'   : { 'ch' : [family_data['ch']['index'][30]]},
            prefix + '06C1'   : { 'ch' : [family_data['ch']['index'][31]]},
            prefix + '06C2'   : { 'ch' : [family_data['ch']['index'][32]]},
            prefix + '06C3'   : { 'ch' : [family_data['ch']['index'][33]]},
            prefix + '06C4'   : { 'ch' : [family_data['ch']['index'][34]]},
            prefix + '07M1'   : { 'ch' : [family_data['ch']['index'][35]]},
            prefix + '07M2'   : { 'ch' : [family_data['ch']['index'][36]]},
            prefix + '07C1'   : { 'ch' : [family_data['ch']['index'][37]]},
            prefix + '07C2'   : { 'ch' : [family_data['ch']['index'][38]]},
            prefix + '07C3'   : { 'ch' : [family_data['ch']['index'][39]]},
            prefix + '07C4'   : { 'ch' : [family_data['ch']['index'][40]]},
            prefix + '08M1'   : { 'ch' : [family_data['ch']['index'][41]]},
            prefix + '08M2'   : { 'ch' : [family_data['ch']['index'][42]]},
            prefix + '08C1'   : { 'ch' : [family_data['ch']['index'][43]]},
            prefix + '08C2'   : { 'ch' : [family_data['ch']['index'][44]]},
            prefix + '08C3'   : { 'ch' : [family_data['ch']['index'][45]]},
            prefix + '08C4'   : { 'ch' : [family_data['ch']['index'][46]]},
            prefix + '09M1'   : { 'ch' : [family_data['ch']['index'][47]]},
            prefix + '09M2'   : { 'ch' : [family_data['ch']['index'][48]]},
            prefix + '09C1'   : { 'ch' : [family_data['ch']['index'][49]]},
            prefix + '09C2'   : { 'ch' : [family_data['ch']['index'][50]]},
            prefix + '09C3'   : { 'ch' : [family_data['ch']['index'][51]]},
            prefix + '09C4'   : { 'ch' : [family_data['ch']['index'][52]]},
            prefix + '10M1'   : { 'ch' : [family_data['ch']['index'][53]]},
            prefix + '10M2'   : { 'ch' : [family_data['ch']['index'][54]]},
            prefix + '10C1'   : { 'ch' : [family_data['ch']['index'][55]]},
            prefix + '10C2'   : { 'ch' : [family_data['ch']['index'][56]]},
            prefix + '10C3'   : { 'ch' : [family_data['ch']['index'][57]]},
            prefix + '10C4'   : { 'ch' : [family_data['ch']['index'][58]]},
            prefix + '11M1'   : { 'ch' : [family_data['ch']['index'][59]]},
            prefix + '11M2'   : { 'ch' : [family_data['ch']['index'][60]]},
            prefix + '11C1'   : { 'ch' : [family_data['ch']['index'][61]]},
            prefix + '11C2'   : { 'ch' : [family_data['ch']['index'][62]]},
            prefix + '11C3'   : { 'ch' : [family_data['ch']['index'][63]]},
            prefix + '11C4'   : { 'ch' : [family_data['ch']['index'][64]]},
            prefix + '12M1'   : { 'ch' : [family_data['ch']['index'][65]]},
            prefix + '12M2'   : { 'ch' : [family_data['ch']['index'][66]]},
            prefix + '12C1'   : { 'ch' : [family_data['ch']['index'][67]]},
            prefix + '12C2'   : { 'ch' : [family_data['ch']['index'][68]]},
            prefix + '12C3'   : { 'ch' : [family_data['ch']['index'][69]]},
            prefix + '12C4'   : { 'ch' : [family_data['ch']['index'][70]]},
            prefix + '13M1'   : { 'ch' : [family_data['ch']['index'][71]]},
            prefix + '13M2'   : { 'ch' : [family_data['ch']['index'][72]]},
            prefix + '13C1'   : { 'ch' : [family_data['ch']['index'][73]]},
            prefix + '13C2'   : { 'ch' : [family_data['ch']['index'][74]]},
            prefix + '13C3'   : { 'ch' : [family_data['ch']['index'][75]]},
            prefix + '13C4'   : { 'ch' : [family_data['ch']['index'][76]]},
            prefix + '14M1'   : { 'ch' : [family_data['ch']['index'][77]]},
            prefix + '14M2'   : { 'ch' : [family_data['ch']['index'][78]]},
            prefix + '14C1'   : { 'ch' : [family_data['ch']['index'][79]]},
            prefix + '14C2'   : { 'ch' : [family_data['ch']['index'][80]]},
            prefix + '14C3'   : { 'ch' : [family_data['ch']['index'][81]]},
            prefix + '14C4'   : { 'ch' : [family_data['ch']['index'][82]]},
            prefix + '15M1'   : { 'ch' : [family_data['ch']['index'][83]]},
            prefix + '15M2'   : { 'ch' : [family_data['ch']['index'][84]]},
            prefix + '15C1'   : { 'ch' : [family_data['ch']['index'][85]]},
            prefix + '15C2'   : { 'ch' : [family_data['ch']['index'][86]]},
            prefix + '15C3'   : { 'ch' : [family_data['ch']['index'][87]]},
            prefix + '15C4'   : { 'ch' : [family_data['ch']['index'][88]]},
            prefix + '16M1'   : { 'ch' : [family_data['ch']['index'][89]]},
            prefix + '16M2'   : { 'ch' : [family_data['ch']['index'][90]]},
            prefix + '16C1'   : { 'ch' : [family_data['ch']['index'][91]]},
            prefix + '16C2'   : { 'ch' : [family_data['ch']['index'][92]]},
            prefix + '16C3'   : { 'ch' : [family_data['ch']['index'][93]]},
            prefix + '16C4'   : { 'ch' : [family_data['ch']['index'][94]]},
            prefix + '17M1'   : { 'ch' : [family_data['ch']['index'][95]]},
            prefix + '17M2'   : { 'ch' : [family_data['ch']['index'][96]]},
            prefix + '17C1'   : { 'ch' : [family_data['ch']['index'][97]]},
            prefix + '17C2'   : { 'ch' : [family_data['ch']['index'][98]]},
            prefix + '17C3'   : { 'ch' : [family_data['ch']['index'][99]]},
            prefix + '17C4'   : { 'ch' : [family_data['ch']['index'][100]]},
            prefix + '18M1'   : { 'ch' : [family_data['ch']['index'][101]]},
            prefix + '18M2'   : { 'ch' : [family_data['ch']['index'][102]]},
            prefix + '18C1'   : { 'ch' : [family_data['ch']['index'][103]]},
            prefix + '18C2'   : { 'ch' : [family_data['ch']['index'][104]]},
            prefix + '18C3'   : { 'ch' : [family_data['ch']['index'][105]]},
            prefix + '18C4'   : { 'ch' : [family_data['ch']['index'][106]]},
            prefix + '19M1'   : { 'ch' : [family_data['ch']['index'][107]]},
            prefix + '19M2'   : { 'ch' : [family_data['ch']['index'][108]]},
            prefix + '19C1'   : { 'ch' : [family_data['ch']['index'][109]]},
            prefix + '19C2'   : { 'ch' : [family_data['ch']['index'][110]]},
            prefix + '19C3'   : { 'ch' : [family_data['ch']['index'][111]]},
            prefix + '19C4'   : { 'ch' : [family_data['ch']['index'][112]]},
            prefix + '20M1'   : { 'ch' : [family_data['ch']['index'][113]]},
            prefix + '20M2'   : { 'ch' : [family_data['ch']['index'][114]]},
            prefix + '20C1'   : { 'ch' : [family_data['ch']['index'][115]]},
            prefix + '20C2'   : { 'ch' : [family_data['ch']['index'][116]]},
            prefix + '20C3'   : { 'ch' : [family_data['ch']['index'][117]]},
            prefix + '20C4'   : { 'ch' : [family_data['ch']['index'][118]]},
            prefix + '01M1'   : { 'ch' : [family_data['ch']['index'][119]]},
        }
        return _dict

    if element.lower() == 'cv':
        prefix = prefix + 'CV-'
        _dict = {
            prefix + '01M2'   : { 'cv' : [family_data['cv']['index'][0]]},
            prefix + '01C1'   : { 'cv' : [family_data['cv']['index'][1]]},
            prefix + '01C2-A' : { 'cv' : [family_data['cv']['index'][2]]},
            prefix + '01C2-B' : { 'cv' : [family_data['cv']['index'][3]]},
            prefix + '01C3-A' : { 'cv' : [family_data['cv']['index'][4]]},
            prefix + '01C3-B' : { 'cv' : [family_data['cv']['index'][5]]},
            prefix + '01C4'   : { 'cv' : [family_data['cv']['index'][6]]},
            prefix + '02M1'   : { 'cv' : [family_data['cv']['index'][7]]},
            prefix + '02M2'   : { 'cv' : [family_data['cv']['index'][8]]},
            prefix + '02C1'   : { 'cv' : [family_data['cv']['index'][9]]},
            prefix + '02C2-A' : { 'cv' : [family_data['cv']['index'][10]]},
            prefix + '02C2-B' : { 'cv' : [family_data['cv']['index'][11]]},
            prefix + '02C3-A' : { 'cv' : [family_data['cv']['index'][12]]},
            prefix + '02C3-B' : { 'cv' : [family_data['cv']['index'][13]]},
            prefix + '02C4'   : { 'cv' : [family_data['cv']['index'][14]]},
            prefix + '03M1'   : { 'cv' : [family_data['cv']['index'][15]]},
            prefix + '03M2'   : { 'cv' : [family_data['cv']['index'][16]]},
            prefix + '03C1'   : { 'cv' : [family_data['cv']['index'][17]]},
            prefix + '03C2-A' : { 'cv' : [family_data['cv']['index'][18]]},
            prefix + '03C2-B' : { 'cv' : [family_data['cv']['index'][19]]},
            prefix + '03C3-A' : { 'cv' : [family_data['cv']['index'][20]]},
            prefix + '03C3-B' : { 'cv' : [family_data['cv']['index'][21]]},
            prefix + '03C4'   : { 'cv' : [family_data['cv']['index'][22]]},
            prefix + '04M1'   : { 'cv' : [family_data['cv']['index'][23]]},
            prefix + '04M2'   : { 'cv' : [family_data['cv']['index'][24]]},
            prefix + '04C1'   : { 'cv' : [family_data['cv']['index'][25]]},
            prefix + '04C2-A' : { 'cv' : [family_data['cv']['index'][26]]},
            prefix + '04C2-B' : { 'cv' : [family_data['cv']['index'][27]]},
            prefix + '04C3-A' : { 'cv' : [family_data['cv']['index'][28]]},
            prefix + '04C3-B' : { 'cv' : [family_data['cv']['index'][29]]},
            prefix + '04C4'   : { 'cv' : [family_data['cv']['index'][30]]},
            prefix + '05M1'   : { 'cv' : [family_data['cv']['index'][31]]},
            prefix + '05M2'   : { 'cv' : [family_data['cv']['index'][32]]},
            prefix + '05C1'   : { 'cv' : [family_data['cv']['index'][33]]},
            prefix + '05C2-A' : { 'cv' : [family_data['cv']['index'][34]]},
            prefix + '05C2-B' : { 'cv' : [family_data['cv']['index'][35]]},
            prefix + '05C3-A' : { 'cv' : [family_data['cv']['index'][36]]},
            prefix + '05C3-B' : { 'cv' : [family_data['cv']['index'][37]]},
            prefix + '05C4'   : { 'cv' : [family_data['cv']['index'][38]]},
            prefix + '06M1'   : { 'cv' : [family_data['cv']['index'][39]]},
            prefix + '06M2'   : { 'cv' : [family_data['cv']['index'][40]]},
            prefix + '06C1'   : { 'cv' : [family_data['cv']['index'][41]]},
            prefix + '06C2-A' : { 'cv' : [family_data['cv']['index'][42]]},
            prefix + '06C2-B' : { 'cv' : [family_data['cv']['index'][43]]},
            prefix + '06C3-A' : { 'cv' : [family_data['cv']['index'][44]]},
            prefix + '06C3-B' : { 'cv' : [family_data['cv']['index'][45]]},
            prefix + '06C4'   : { 'cv' : [family_data['cv']['index'][46]]},
            prefix + '07M1'   : { 'cv' : [family_data['cv']['index'][47]]},
            prefix + '07M2'   : { 'cv' : [family_data['cv']['index'][48]]},
            prefix + '07C1'   : { 'cv' : [family_data['cv']['index'][49]]},
            prefix + '07C2-A' : { 'cv' : [family_data['cv']['index'][50]]},
            prefix + '07C2-B' : { 'cv' : [family_data['cv']['index'][51]]},
            prefix + '07C3-A' : { 'cv' : [family_data['cv']['index'][52]]},
            prefix + '07C3-B' : { 'cv' : [family_data['cv']['index'][53]]},
            prefix + '07C4'   : { 'cv' : [family_data['cv']['index'][54]]},
            prefix + '08M1'   : { 'cv' : [family_data['cv']['index'][55]]},
            prefix + '08M2'   : { 'cv' : [family_data['cv']['index'][56]]},
            prefix + '08C1'   : { 'cv' : [family_data['cv']['index'][57]]},
            prefix + '08C2-A' : { 'cv' : [family_data['cv']['index'][58]]},
            prefix + '08C2-B' : { 'cv' : [family_data['cv']['index'][59]]},
            prefix + '08C3-A' : { 'cv' : [family_data['cv']['index'][60]]},
            prefix + '08C3-B' : { 'cv' : [family_data['cv']['index'][61]]},
            prefix + '08C4'   : { 'cv' : [family_data['cv']['index'][62]]},
            prefix + '09M1'   : { 'cv' : [family_data['cv']['index'][63]]},
            prefix + '09M2'   : { 'cv' : [family_data['cv']['index'][64]]},
            prefix + '09C1'   : { 'cv' : [family_data['cv']['index'][65]]},
            prefix + '09C2-A' : { 'cv' : [family_data['cv']['index'][66]]},
            prefix + '09C2-B' : { 'cv' : [family_data['cv']['index'][67]]},
            prefix + '09C3-A' : { 'cv' : [family_data['cv']['index'][68]]},
            prefix + '09C3-B' : { 'cv' : [family_data['cv']['index'][69]]},
            prefix + '09C4'   : { 'cv' : [family_data['cv']['index'][70]]},
            prefix + '10M1'   : { 'cv' : [family_data['cv']['index'][71]]},
            prefix + '10M2'   : { 'cv' : [family_data['cv']['index'][72]]},
            prefix + '10C1'   : { 'cv' : [family_data['cv']['index'][73]]},
            prefix + '10C2-A' : { 'cv' : [family_data['cv']['index'][74]]},
            prefix + '10C2-B' : { 'cv' : [family_data['cv']['index'][75]]},
            prefix + '10C3-A' : { 'cv' : [family_data['cv']['index'][76]]},
            prefix + '10C3-B' : { 'cv' : [family_data['cv']['index'][77]]},
            prefix + '10C4'   : { 'cv' : [family_data['cv']['index'][78]]},
            prefix + '11M1'   : { 'cv' : [family_data['cv']['index'][79]]},
            prefix + '11M2'   : { 'cv' : [family_data['cv']['index'][80]]},
            prefix + '11C1'   : { 'cv' : [family_data['cv']['index'][81]]},
            prefix + '11C2-A' : { 'cv' : [family_data['cv']['index'][82]]},
            prefix + '11C2-B' : { 'cv' : [family_data['cv']['index'][83]]},
            prefix + '11C3-A' : { 'cv' : [family_data['cv']['index'][84]]},
            prefix + '11C3-B' : { 'cv' : [family_data['cv']['index'][85]]},
            prefix + '11C4'   : { 'cv' : [family_data['cv']['index'][86]]},
            prefix + '12M1'   : { 'cv' : [family_data['cv']['index'][87]]},
            prefix + '12M2'   : { 'cv' : [family_data['cv']['index'][88]]},
            prefix + '12C1'   : { 'cv' : [family_data['cv']['index'][89]]},
            prefix + '12C2-A' : { 'cv' : [family_data['cv']['index'][90]]},
            prefix + '12C2-B' : { 'cv' : [family_data['cv']['index'][91]]},
            prefix + '12C3-A' : { 'cv' : [family_data['cv']['index'][92]]},
            prefix + '12C3-B' : { 'cv' : [family_data['cv']['index'][93]]},
            prefix + '12C4'   : { 'cv' : [family_data['cv']['index'][94]]},
            prefix + '13M1'   : { 'cv' : [family_data['cv']['index'][95]]},
            prefix + '13M2'   : { 'cv' : [family_data['cv']['index'][96]]},
            prefix + '13C1'   : { 'cv' : [family_data['cv']['index'][97]]},
            prefix + '13C2-A' : { 'cv' : [family_data['cv']['index'][98]]},
            prefix + '13C2-B' : { 'cv' : [family_data['cv']['index'][99]]},
            prefix + '13C3-A' : { 'cv' : [family_data['cv']['index'][100]]},
            prefix + '13C3-B' : { 'cv' : [family_data['cv']['index'][101]]},
            prefix + '13C4'   : { 'cv' : [family_data['cv']['index'][102]]},
            prefix + '14M1'   : { 'cv' : [family_data['cv']['index'][103]]},
            prefix + '14M2'   : { 'cv' : [family_data['cv']['index'][104]]},
            prefix + '14C1'   : { 'cv' : [family_data['cv']['index'][105]]},
            prefix + '14C2-A' : { 'cv' : [family_data['cv']['index'][106]]},
            prefix + '14C2-B' : { 'cv' : [family_data['cv']['index'][107]]},
            prefix + '14C3-A' : { 'cv' : [family_data['cv']['index'][108]]},
            prefix + '14C3-B' : { 'cv' : [family_data['cv']['index'][109]]},
            prefix + '14C4'   : { 'cv' : [family_data['cv']['index'][110]]},
            prefix + '15M1'   : { 'cv' : [family_data['cv']['index'][111]]},
            prefix + '15M2'   : { 'cv' : [family_data['cv']['index'][112]]},
            prefix + '15C1'   : { 'cv' : [family_data['cv']['index'][113]]},
            prefix + '15C2-A' : { 'cv' : [family_data['cv']['index'][114]]},
            prefix + '15C2-B' : { 'cv' : [family_data['cv']['index'][115]]},
            prefix + '15C3-A' : { 'cv' : [family_data['cv']['index'][116]]},
            prefix + '15C3-B' : { 'cv' : [family_data['cv']['index'][117]]},
            prefix + '15C4'   : { 'cv' : [family_data['cv']['index'][118]]},
            prefix + '16M1'   : { 'cv' : [family_data['cv']['index'][119]]},
            prefix + '16M2'   : { 'cv' : [family_data['cv']['index'][120]]},
            prefix + '16C1'   : { 'cv' : [family_data['cv']['index'][121]]},
            prefix + '16C2-A' : { 'cv' : [family_data['cv']['index'][122]]},
            prefix + '16C2-B' : { 'cv' : [family_data['cv']['index'][123]]},
            prefix + '16C3-A' : { 'cv' : [family_data['cv']['index'][124]]},
            prefix + '16C3-B' : { 'cv' : [family_data['cv']['index'][125]]},
            prefix + '16C4'   : { 'cv' : [family_data['cv']['index'][126]]},
            prefix + '17M1'   : { 'cv' : [family_data['cv']['index'][127]]},
            prefix + '17M2'   : { 'cv' : [family_data['cv']['index'][128]]},
            prefix + '17C1'   : { 'cv' : [family_data['cv']['index'][129]]},
            prefix + '17C2-A' : { 'cv' : [family_data['cv']['index'][130]]},
            prefix + '17C2-B' : { 'cv' : [family_data['cv']['index'][131]]},
            prefix + '17C3-A' : { 'cv' : [family_data['cv']['index'][132]]},
            prefix + '17C3-B' : { 'cv' : [family_data['cv']['index'][133]]},
            prefix + '17C4'   : { 'cv' : [family_data['cv']['index'][134]]},
            prefix + '18M1'   : { 'cv' : [family_data['cv']['index'][135]]},
            prefix + '18M2'   : { 'cv' : [family_data['cv']['index'][136]]},
            prefix + '18C1'   : { 'cv' : [family_data['cv']['index'][137]]},
            prefix + '18C2-A' : { 'cv' : [family_data['cv']['index'][138]]},
            prefix + '18C2-B' : { 'cv' : [family_data['cv']['index'][139]]},
            prefix + '18C3-A' : { 'cv' : [family_data['cv']['index'][140]]},
            prefix + '18C3-B' : { 'cv' : [family_data['cv']['index'][141]]},
            prefix + '18C4'   : { 'cv' : [family_data['cv']['index'][142]]},
            prefix + '19M1'   : { 'cv' : [family_data['cv']['index'][143]]},
            prefix + '19M2'   : { 'cv' : [family_data['cv']['index'][144]]},
            prefix + '19C1'   : { 'cv' : [family_data['cv']['index'][145]]},
            prefix + '19C2-A' : { 'cv' : [family_data['cv']['index'][146]]},
            prefix + '19C2-B' : { 'cv' : [family_data['cv']['index'][147]]},
            prefix + '19C3-A' : { 'cv' : [family_data['cv']['index'][148]]},
            prefix + '19C3-B' : { 'cv' : [family_data['cv']['index'][149]]},
            prefix + '19C4'   : { 'cv' : [family_data['cv']['index'][150]]},
            prefix + '20M1'   : { 'cv' : [family_data['cv']['index'][151]]},
            prefix + '20M2'   : { 'cv' : [family_data['cv']['index'][152]]},
            prefix + '20C1'   : { 'cv' : [family_data['cv']['index'][153]]},
            prefix + '20C2-A' : { 'cv' : [family_data['cv']['index'][154]]},
            prefix + '20C2-B' : { 'cv' : [family_data['cv']['index'][155]]},
            prefix + '20C3-A' : { 'cv' : [family_data['cv']['index'][156]]},
            prefix + '20C3-B' : { 'cv' : [family_data['cv']['index'][157]]},
            prefix + '20C4'   : { 'cv' : [family_data['cv']['index'][158]]},
            prefix + '01M1'   : { 'cv' : [family_data['cv']['index'][159]]},
        }
        return _dict

    if element.lower() == 'fch':
        prefix = prefix + 'FCH-'
        _dict = {
            prefix + '01M2'   : { 'fch' : [family_data['fch']['index'][0]]},
            prefix + '01C2'   : { 'fch' : [family_data['fch']['index'][1]]},
            prefix + '01C3'   : { 'fch' : [family_data['fch']['index'][2]]},
            prefix + '02M1'   : { 'fch' : [family_data['fch']['index'][3]]},
            prefix + '02M2'   : { 'fch' : [family_data['fch']['index'][4]]},
            prefix + '02C2'   : { 'fch' : [family_data['fch']['index'][5]]},
            prefix + '02C3'   : { 'fch' : [family_data['fch']['index'][6]]},
            prefix + '03M1'   : { 'fch' : [family_data['fch']['index'][7]]},
            prefix + '03M2'   : { 'fch' : [family_data['fch']['index'][8]]},
            prefix + '03C2'   : { 'fch' : [family_data['fch']['index'][9]]},
            prefix + '03C3'   : { 'fch' : [family_data['fch']['index'][10]]},
            prefix + '04M1'   : { 'fch' : [family_data['fch']['index'][11]]},
            prefix + '04M2'   : { 'fch' : [family_data['fch']['index'][12]]},
            prefix + '04C2'   : { 'fch' : [family_data['fch']['index'][13]]},
            prefix + '04C3'   : { 'fch' : [family_data['fch']['index'][14]]},
            prefix + '05M1'   : { 'fch' : [family_data['fch']['index'][15]]},
            prefix + '05M2'   : { 'fch' : [family_data['fch']['index'][16]]},
            prefix + '05C2'   : { 'fch' : [family_data['fch']['index'][17]]},
            prefix + '05C3'   : { 'fch' : [family_data['fch']['index'][18]]},
            prefix + '06M1'   : { 'fch' : [family_data['fch']['index'][19]]},
            prefix + '06M2'   : { 'fch' : [family_data['fch']['index'][20]]},
            prefix + '06C2'   : { 'fch' : [family_data['fch']['index'][21]]},
            prefix + '06C3'   : { 'fch' : [family_data['fch']['index'][22]]},
            prefix + '07M1'   : { 'fch' : [family_data['fch']['index'][23]]},
            prefix + '07M2'   : { 'fch' : [family_data['fch']['index'][24]]},
            prefix + '07C2'   : { 'fch' : [family_data['fch']['index'][25]]},
            prefix + '07C3'   : { 'fch' : [family_data['fch']['index'][26]]},
            prefix + '08M1'   : { 'fch' : [family_data['fch']['index'][27]]},
            prefix + '08M2'   : { 'fch' : [family_data['fch']['index'][28]]},
            prefix + '08C2'   : { 'fch' : [family_data['fch']['index'][29]]},
            prefix + '08C3'   : { 'fch' : [family_data['fch']['index'][30]]},
            prefix + '09M1'   : { 'fch' : [family_data['fch']['index'][31]]},
            prefix + '09M2'   : { 'fch' : [family_data['fch']['index'][32]]},
            prefix + '09C2'   : { 'fch' : [family_data['fch']['index'][33]]},
            prefix + '09C3'   : { 'fch' : [family_data['fch']['index'][34]]},
            prefix + '10M1'   : { 'fch' : [family_data['fch']['index'][35]]},
            prefix + '10M2'   : { 'fch' : [family_data['fch']['index'][36]]},
            prefix + '10C2'   : { 'fch' : [family_data['fch']['index'][37]]},
            prefix + '10C3'   : { 'fch' : [family_data['fch']['index'][38]]},
            prefix + '11M1'   : { 'fch' : [family_data['fch']['index'][39]]},
            prefix + '11M2'   : { 'fch' : [family_data['fch']['index'][40]]},
            prefix + '11C2'   : { 'fch' : [family_data['fch']['index'][41]]},
            prefix + '11C3'   : { 'fch' : [family_data['fch']['index'][42]]},
            prefix + '12M1'   : { 'fch' : [family_data['fch']['index'][43]]},
            prefix + '12M2'   : { 'fch' : [family_data['fch']['index'][44]]},
            prefix + '12C2'   : { 'fch' : [family_data['fch']['index'][45]]},
            prefix + '12C3'   : { 'fch' : [family_data['fch']['index'][46]]},
            prefix + '13M1'   : { 'fch' : [family_data['fch']['index'][47]]},
            prefix + '13M2'   : { 'fch' : [family_data['fch']['index'][48]]},
            prefix + '13C2'   : { 'fch' : [family_data['fch']['index'][49]]},
            prefix + '13C3'   : { 'fch' : [family_data['fch']['index'][50]]},
            prefix + '14M1'   : { 'fch' : [family_data['fch']['index'][51]]},
            prefix + '14M2'   : { 'fch' : [family_data['fch']['index'][52]]},
            prefix + '14C2'   : { 'fch' : [family_data['fch']['index'][53]]},
            prefix + '14C3'   : { 'fch' : [family_data['fch']['index'][54]]},
            prefix + '15M1'   : { 'fch' : [family_data['fch']['index'][55]]},
            prefix + '15M2'   : { 'fch' : [family_data['fch']['index'][56]]},
            prefix + '15C2'   : { 'fch' : [family_data['fch']['index'][57]]},
            prefix + '15C3'   : { 'fch' : [family_data['fch']['index'][58]]},
            prefix + '16M1'   : { 'fch' : [family_data['fch']['index'][59]]},
            prefix + '16M2'   : { 'fch' : [family_data['fch']['index'][60]]},
            prefix + '16C2'   : { 'fch' : [family_data['fch']['index'][61]]},
            prefix + '16C3'   : { 'fch' : [family_data['fch']['index'][62]]},
            prefix + '17M1'   : { 'fch' : [family_data['fch']['index'][63]]},
            prefix + '17M2'   : { 'fch' : [family_data['fch']['index'][64]]},
            prefix + '17C2'   : { 'fch' : [family_data['fch']['index'][65]]},
            prefix + '17C3'   : { 'fch' : [family_data['fch']['index'][66]]},
            prefix + '18M1'   : { 'fch' : [family_data['fch']['index'][67]]},
            prefix + '18M2'   : { 'fch' : [family_data['fch']['index'][68]]},
            prefix + '18C2'   : { 'fch' : [family_data['fch']['index'][69]]},
            prefix + '18C3'   : { 'fch' : [family_data['fch']['index'][70]]},
            prefix + '19M1'   : { 'fch' : [family_data['fch']['index'][71]]},
            prefix + '19M2'   : { 'fch' : [family_data['fch']['index'][72]]},
            prefix + '19C2'   : { 'fch' : [family_data['fch']['index'][73]]},
            prefix + '19C3'   : { 'fch' : [family_data['fch']['index'][74]]},
            prefix + '20M1'   : { 'fch' : [family_data['fch']['index'][75]]},
            prefix + '20M2'   : { 'fch' : [family_data['fch']['index'][76]]},
            prefix + '20C2'   : { 'fch' : [family_data['fch']['index'][77]]},
            prefix + '20C3'   : { 'fch' : [family_data['fch']['index'][78]]},
            prefix + '01M1'   : { 'fch' : [family_data['fch']['index'][79]]},
        }
        return _dict


    if element.lower() == 'fcv':
        prefix = prefix + 'FCV-'
        _dict = {
            prefix + '01M2'   : { 'fcv' : [family_data['fcv']['index'][0]]},
            prefix + '01C2'   : { 'fcv' : [family_data['fcv']['index'][1]]},
            prefix + '01C3'   : { 'fcv' : [family_data['fcv']['index'][2]]},
            prefix + '02M1'   : { 'fcv' : [family_data['fcv']['index'][3]]},
            prefix + '02M2'   : { 'fcv' : [family_data['fcv']['index'][4]]},
            prefix + '02C2'   : { 'fcv' : [family_data['fcv']['index'][5]]},
            prefix + '02C3'   : { 'fcv' : [family_data['fcv']['index'][6]]},
            prefix + '03M1'   : { 'fcv' : [family_data['fcv']['index'][7]]},
            prefix + '03M2'   : { 'fcv' : [family_data['fcv']['index'][8]]},
            prefix + '03C2'   : { 'fcv' : [family_data['fcv']['index'][9]]},
            prefix + '03C3'   : { 'fcv' : [family_data['fcv']['index'][10]]},
            prefix + '04M1'   : { 'fcv' : [family_data['fcv']['index'][11]]},
            prefix + '04M2'   : { 'fcv' : [family_data['fcv']['index'][12]]},
            prefix + '04C2'   : { 'fcv' : [family_data['fcv']['index'][13]]},
            prefix + '04C3'   : { 'fcv' : [family_data['fcv']['index'][14]]},
            prefix + '05M1'   : { 'fcv' : [family_data['fcv']['index'][15]]},
            prefix + '05M2'   : { 'fcv' : [family_data['fcv']['index'][16]]},
            prefix + '05C2'   : { 'fcv' : [family_data['fcv']['index'][17]]},
            prefix + '05C3'   : { 'fcv' : [family_data['fcv']['index'][18]]},
            prefix + '06M1'   : { 'fcv' : [family_data['fcv']['index'][19]]},
            prefix + '06M2'   : { 'fcv' : [family_data['fcv']['index'][20]]},
            prefix + '06C2'   : { 'fcv' : [family_data['fcv']['index'][21]]},
            prefix + '06C3'   : { 'fcv' : [family_data['fcv']['index'][22]]},
            prefix + '07M1'   : { 'fcv' : [family_data['fcv']['index'][23]]},
            prefix + '07M2'   : { 'fcv' : [family_data['fcv']['index'][24]]},
            prefix + '07C2'   : { 'fcv' : [family_data['fcv']['index'][25]]},
            prefix + '07C3'   : { 'fcv' : [family_data['fcv']['index'][26]]},
            prefix + '08M1'   : { 'fcv' : [family_data['fcv']['index'][27]]},
            prefix + '08M2'   : { 'fcv' : [family_data['fcv']['index'][28]]},
            prefix + '08C2'   : { 'fcv' : [family_data['fcv']['index'][29]]},
            prefix + '08C3'   : { 'fcv' : [family_data['fcv']['index'][30]]},
            prefix + '09M1'   : { 'fcv' : [family_data['fcv']['index'][31]]},
            prefix + '09M2'   : { 'fcv' : [family_data['fcv']['index'][32]]},
            prefix + '09C2'   : { 'fcv' : [family_data['fcv']['index'][33]]},
            prefix + '09C3'   : { 'fcv' : [family_data['fcv']['index'][34]]},
            prefix + '10M1'   : { 'fcv' : [family_data['fcv']['index'][35]]},
            prefix + '10M2'   : { 'fcv' : [family_data['fcv']['index'][36]]},
            prefix + '10C2'   : { 'fcv' : [family_data['fcv']['index'][37]]},
            prefix + '10C3'   : { 'fcv' : [family_data['fcv']['index'][38]]},
            prefix + '11M1'   : { 'fcv' : [family_data['fcv']['index'][39]]},
            prefix + '11M2'   : { 'fcv' : [family_data['fcv']['index'][40]]},
            prefix + '11C2'   : { 'fcv' : [family_data['fcv']['index'][41]]},
            prefix + '11C3'   : { 'fcv' : [family_data['fcv']['index'][42]]},
            prefix + '12M1'   : { 'fcv' : [family_data['fcv']['index'][43]]},
            prefix + '12M2'   : { 'fcv' : [family_data['fcv']['index'][44]]},
            prefix + '12C2'   : { 'fcv' : [family_data['fcv']['index'][45]]},
            prefix + '12C3'   : { 'fcv' : [family_data['fcv']['index'][46]]},
            prefix + '13M1'   : { 'fcv' : [family_data['fcv']['index'][47]]},
            prefix + '13M2'   : { 'fcv' : [family_data['fcv']['index'][48]]},
            prefix + '13C2'   : { 'fcv' : [family_data['fcv']['index'][49]]},
            prefix + '13C3'   : { 'fcv' : [family_data['fcv']['index'][50]]},
            prefix + '14M1'   : { 'fcv' : [family_data['fcv']['index'][51]]},
            prefix + '14M2'   : { 'fcv' : [family_data['fcv']['index'][52]]},
            prefix + '14C2'   : { 'fcv' : [family_data['fcv']['index'][53]]},
            prefix + '14C3'   : { 'fcv' : [family_data['fcv']['index'][54]]},
            prefix + '15M1'   : { 'fcv' : [family_data['fcv']['index'][55]]},
            prefix + '15M2'   : { 'fcv' : [family_data['fcv']['index'][56]]},
            prefix + '15C2'   : { 'fcv' : [family_data['fcv']['index'][57]]},
            prefix + '15C3'   : { 'fcv' : [family_data['fcv']['index'][58]]},
            prefix + '16M1'   : { 'fcv' : [family_data['fcv']['index'][59]]},
            prefix + '16M2'   : { 'fcv' : [family_data['fcv']['index'][60]]},
            prefix + '16C2'   : { 'fcv' : [family_data['fcv']['index'][61]]},
            prefix + '16C3'   : { 'fcv' : [family_data['fcv']['index'][62]]},
            prefix + '17M1'   : { 'fcv' : [family_data['fcv']['index'][63]]},
            prefix + '17M2'   : { 'fcv' : [family_data['fcv']['index'][64]]},
            prefix + '17C2'   : { 'fcv' : [family_data['fcv']['index'][65]]},
            prefix + '17C3'   : { 'fcv' : [family_data['fcv']['index'][66]]},
            prefix + '18M1'   : { 'fcv' : [family_data['fcv']['index'][67]]},
            prefix + '18M2'   : { 'fcv' : [family_data['fcv']['index'][68]]},
            prefix + '18C2'   : { 'fcv' : [family_data['fcv']['index'][69]]},
            prefix + '18C3'   : { 'fcv' : [family_data['fcv']['index'][70]]},
            prefix + '19M1'   : { 'fcv' : [family_data['fcv']['index'][71]]},
            prefix + '19M2'   : { 'fcv' : [family_data['fcv']['index'][72]]},
            prefix + '19C2'   : { 'fcv' : [family_data['fcv']['index'][73]]},
            prefix + '19C3'   : { 'fcv' : [family_data['fcv']['index'][74]]},
            prefix + '20M1'   : { 'fcv' : [family_data['fcv']['index'][75]]},
            prefix + '20M2'   : { 'fcv' : [family_data['fcv']['index'][76]]},
            prefix + '20C2'   : { 'fcv' : [family_data['fcv']['index'][77]]},
            prefix + '20C3'   : { 'fcv' : [family_data['fcv']['index'][78]]},
            prefix + '01M1'   : { 'fcv' : [family_data['fcv']['index'][79]]},
        }
        return _dict

    if element.lower() == 'sfa':
        prefix = prefix + 'SFA-'
        _dict = {
            prefix + '01M2'   : { 'sfa' : [family_data['sfa']['index'][0]]},
            prefix + '02M2'   : { 'sfa' : [family_data['sfa']['index'][1]]},
            prefix + '03M2'   : { 'sfa' : [family_data['sfa']['index'][2]]},
            prefix + '04M2'   : { 'sfa' : [family_data['sfa']['index'][3]]},
            prefix + '05M2'   : { 'sfa' : [family_data['sfa']['index'][4]]},
            prefix + '06M2'   : { 'sfa' : [family_data['sfa']['index'][5]]},
            prefix + '07M2'   : { 'sfa' : [family_data['sfa']['index'][6]]},
            prefix + '08M2'   : { 'sfa' : [family_data['sfa']['index'][7]]},
            prefix + '09M2'   : { 'sfa' : [family_data['sfa']['index'][8]]},
            prefix + '10M2'   : { 'sfa' : [family_data['sfa']['index'][9]]},
            prefix + '11M2'   : { 'sfa' : [family_data['sfa']['index'][10]]},
            prefix + '12M2'   : { 'sfa' : [family_data['sfa']['index'][11]]},
            prefix + '13M2'   : { 'sfa' : [family_data['sfa']['index'][12]]},
            prefix + '14M2'   : { 'sfa' : [family_data['sfa']['index'][13]]},
            prefix + '15M2'   : { 'sfa' : [family_data['sfa']['index'][14]]},
            prefix + '16M2'   : { 'sfa' : [family_data['sfa']['index'][15]]},
            prefix + '17M2'   : { 'sfa' : [family_data['sfa']['index'][16]]},
            prefix + '18M2'   : { 'sfa' : [family_data['sfa']['index'][17]]},
            prefix + '19M2'   : { 'sfa' : [family_data['sfa']['index'][18]]},
            prefix + '20M2'   : { 'sfa' : [family_data['sfa']['index'][19]]},
        }
        return _dict

    if element.lower() == 'qfa':
        prefix = prefix + 'QFA-'
        _dict = {
            prefix + '01M2'   : { 'qfa' : [family_data['qfa']['index'][0]]},
            prefix + '02M2'   : { 'qfa' : [family_data['qfa']['index'][1]]},
            prefix + '03M2'   : { 'qfa' : [family_data['qfa']['index'][2]]},
            prefix + '04M2'   : { 'qfa' : [family_data['qfa']['index'][3]]},
            prefix + '05M2'   : { 'qfa' : [family_data['qfa']['index'][4]]},
            prefix + '06M2'   : { 'qfa' : [family_data['qfa']['index'][5]]},
            prefix + '07M2'   : { 'qfa' : [family_data['qfa']['index'][6]]},
            prefix + '08M2'   : { 'qfa' : [family_data['qfa']['index'][7]]},
            prefix + '09M2'   : { 'qfa' : [family_data['qfa']['index'][8]]},
            prefix + '10M2'   : { 'qfa' : [family_data['qfa']['index'][9]]},
            prefix + '11M2'   : { 'qfa' : [family_data['qfa']['index'][10]]},
            prefix + '12M2'   : { 'qfa' : [family_data['qfa']['index'][11]]},
            prefix + '13M2'   : { 'qfa' : [family_data['qfa']['index'][12]]},
            prefix + '14M2'   : { 'qfa' : [family_data['qfa']['index'][13]]},
            prefix + '15M2'   : { 'qfa' : [family_data['qfa']['index'][14]]},
            prefix + '16M2'   : { 'qfa' : [family_data['qfa']['index'][15]]},
            prefix + '17M2'   : { 'qfa' : [family_data['qfa']['index'][16]]},
            prefix + '18M2'   : { 'qfa' : [family_data['qfa']['index'][17]]},
            prefix + '19M2'   : { 'qfa' : [family_data['qfa']['index'][18]]},
            prefix + '20M2'   : { 'qfa' : [family_data['qfa']['index'][19]]},
        }
        return _dict

    if element.lower() == 'qda':
        prefix = prefix + 'QDA-'
        _dict = {
            prefix + '01M2'   : { 'qda' : [family_data['qda']['index'][0]]},
            prefix + '02M2'   : { 'qda' : [family_data['qda']['index'][1]]},
            prefix + '03M2'   : { 'qda' : [family_data['qda']['index'][2]]},
            prefix + '04M2'   : { 'qda' : [family_data['qda']['index'][3]]},
            prefix + '05M2'   : { 'qda' : [family_data['qda']['index'][4]]},
            prefix + '06M2'   : { 'qda' : [family_data['qda']['index'][5]]},
            prefix + '07M2'   : { 'qda' : [family_data['qda']['index'][6]]},
            prefix + '08M2'   : { 'qda' : [family_data['qda']['index'][7]]},
            prefix + '09M2'   : { 'qda' : [family_data['qda']['index'][8]]},
            prefix + '10M2'   : { 'qda' : [family_data['qda']['index'][9]]},
            prefix + '11M2'   : { 'qda' : [family_data['qda']['index'][10]]},
            prefix + '12M2'   : { 'qda' : [family_data['qda']['index'][11]]},
            prefix + '13M2'   : { 'qda' : [family_data['qda']['index'][12]]},
            prefix + '14M2'   : { 'qda' : [family_data['qda']['index'][13]]},
            prefix + '15M2'   : { 'qda' : [family_data['qda']['index'][14]]},
            prefix + '16M2'   : { 'qda' : [family_data['qda']['index'][15]]},
            prefix + '17M2'   : { 'qda' : [family_data['qda']['index'][16]]},
            prefix + '18M2'   : { 'qda' : [family_data['qda']['index'][17]]},
            prefix + '19M2'   : { 'qda' : [family_data['qda']['index'][18]]},
            prefix + '20M2'   : { 'qda' : [family_data['qda']['index'][19]]},
        }
        return _dict

    if element.lower() == 'sda':
        prefix = prefix + 'SDA-'
        _dict = {
            prefix + '01M2'   : { 'sda' : [family_data['sda']['index'][0]]},
            prefix + '02M2'   : { 'sda' : [family_data['sda']['index'][1]]},
            prefix + '03M2'   : { 'sda' : [family_data['sda']['index'][2]]},
            prefix + '04M2'   : { 'sda' : [family_data['sda']['index'][3]]},
            prefix + '05M2'   : { 'sda' : [family_data['sda']['index'][4]]},
            prefix + '06M2'   : { 'sda' : [family_data['sda']['index'][5]]},
            prefix + '07M2'   : { 'sda' : [family_data['sda']['index'][6]]},
            prefix + '08M2'   : { 'sda' : [family_data['sda']['index'][7]]},
            prefix + '09M2'   : { 'sda' : [family_data['sda']['index'][8]]},
            prefix + '10M2'   : { 'sda' : [family_data['sda']['index'][9]]},
            prefix + '11M2'   : { 'sda' : [family_data['sda']['index'][10]]},
            prefix + '12M2'   : { 'sda' : [family_data['sda']['index'][11]]},
            prefix + '13M2'   : { 'sda' : [family_data['sda']['index'][12]]},
            prefix + '14M2'   : { 'sda' : [family_data['sda']['index'][13]]},
            prefix + '15M2'   : { 'sda' : [family_data['sda']['index'][14]]},
            prefix + '16M2'   : { 'sda' : [family_data['sda']['index'][15]]},
            prefix + '17M2'   : { 'sda' : [family_data['sda']['index'][16]]},
            prefix + '18M2'   : { 'sda' : [family_data['sda']['index'][17]]},
            prefix + '19M2'   : { 'sda' : [family_data['sda']['index'][18]]},
            prefix + '20M2'   : { 'sda' : [family_data['sda']['index'][19]]},
        }
        return _dict

    if element.lower() == 'sd1j':
        prefix = prefix + 'SD1J-'
        _dict = {
            prefix + '01C1'   : { 'sd1j' : [family_data['sd1j']['index'][0]]},
            prefix + '02C1'   : { 'sd1j' : [family_data['sd1j']['index'][1]]},
            prefix + '03C1'   : { 'sd1j' : [family_data['sd1j']['index'][2]]},
            prefix + '04C1'   : { 'sd1j' : [family_data['sd1j']['index'][3]]},
            prefix + '05C1'   : { 'sd1j' : [family_data['sd1j']['index'][4]]},
            prefix + '06C1'   : { 'sd1j' : [family_data['sd1j']['index'][5]]},
            prefix + '07C1'   : { 'sd1j' : [family_data['sd1j']['index'][6]]},
            prefix + '08C1'   : { 'sd1j' : [family_data['sd1j']['index'][7]]},
            prefix + '09C1'   : { 'sd1j' : [family_data['sd1j']['index'][8]]},
            prefix + '10C1'   : { 'sd1j' : [family_data['sd1j']['index'][9]]},
            prefix + '11C1'   : { 'sd1j' : [family_data['sd1j']['index'][10]]},
            prefix + '12C1'   : { 'sd1j' : [family_data['sd1j']['index'][11]]},
            prefix + '13C1'   : { 'sd1j' : [family_data['sd1j']['index'][12]]},
            prefix + '14C1'   : { 'sd1j' : [family_data['sd1j']['index'][13]]},
            prefix + '15C1'   : { 'sd1j' : [family_data['sd1j']['index'][14]]},
            prefix + '16C1'   : { 'sd1j' : [family_data['sd1j']['index'][15]]},
            prefix + '17C1'   : { 'sd1j' : [family_data['sd1j']['index'][16]]},
            prefix + '18C1'   : { 'sd1j' : [family_data['sd1j']['index'][17]]},
            prefix + '19C1'   : { 'sd1j' : [family_data['sd1j']['index'][18]]},
            prefix + '20C1'   : { 'sd1j' : [family_data['sd1j']['index'][19]]},
        }
        return _dict

    if element.lower() == 'qf1':
        prefix = prefix + 'QF1-'
        _dict = {
            prefix + '01C1'   : { 'qf1' : [family_data['qf1']['index'][0]]},
            prefix + '01C4'   : { 'qf1' : [family_data['qf1']['index'][1]]},
            prefix + '02C1'   : { 'qf1' : [family_data['qf1']['index'][2]]},
            prefix + '02C4'   : { 'qf1' : [family_data['qf1']['index'][3]]},
            prefix + '03C1'   : { 'qf1' : [family_data['qf1']['index'][4]]},
            prefix + '03C4'   : { 'qf1' : [family_data['qf1']['index'][5]]},
            prefix + '04C1'   : { 'qf1' : [family_data['qf1']['index'][6]]},
            prefix + '04C4'   : { 'qf1' : [family_data['qf1']['index'][7]]},
            prefix + '05C1'   : { 'qf1' : [family_data['qf1']['index'][8]]},
            prefix + '05C4'   : { 'qf1' : [family_data['qf1']['index'][9]]},
            prefix + '06C1'   : { 'qf1' : [family_data['qf1']['index'][10]]},
            prefix + '06C4'   : { 'qf1' : [family_data['qf1']['index'][11]]},
            prefix + '07C1'   : { 'qf1' : [family_data['qf1']['index'][12]]},
            prefix + '07C4'   : { 'qf1' : [family_data['qf1']['index'][13]]},
            prefix + '08C1'   : { 'qf1' : [family_data['qf1']['index'][14]]},
            prefix + '08C4'   : { 'qf1' : [family_data['qf1']['index'][15]]},
            prefix + '09C1'   : { 'qf1' : [family_data['qf1']['index'][16]]},
            prefix + '09C4'   : { 'qf1' : [family_data['qf1']['index'][17]]},
            prefix + '10C1'   : { 'qf1' : [family_data['qf1']['index'][18]]},
            prefix + '10C4'   : { 'qf1' : [family_data['qf1']['index'][19]]},
            prefix + '11C1'   : { 'qf1' : [family_data['qf1']['index'][20]]},
            prefix + '11C4'   : { 'qf1' : [family_data['qf1']['index'][21]]},
            prefix + '12C1'   : { 'qf1' : [family_data['qf1']['index'][22]]},
            prefix + '12C4'   : { 'qf1' : [family_data['qf1']['index'][23]]},
            prefix + '13C1'   : { 'qf1' : [family_data['qf1']['index'][24]]},
            prefix + '13C4'   : { 'qf1' : [family_data['qf1']['index'][25]]},
            prefix + '14C1'   : { 'qf1' : [family_data['qf1']['index'][26]]},
            prefix + '14C4'   : { 'qf1' : [family_data['qf1']['index'][27]]},
            prefix + '15C1'   : { 'qf1' : [family_data['qf1']['index'][28]]},
            prefix + '15C4'   : { 'qf1' : [family_data['qf1']['index'][29]]},
            prefix + '16C1'   : { 'qf1' : [family_data['qf1']['index'][30]]},
            prefix + '16C4'   : { 'qf1' : [family_data['qf1']['index'][31]]},
            prefix + '17C1'   : { 'qf1' : [family_data['qf1']['index'][32]]},
            prefix + '17C4'   : { 'qf1' : [family_data['qf1']['index'][33]]},
            prefix + '18C1'   : { 'qf1' : [family_data['qf1']['index'][34]]},
            prefix + '18C4'   : { 'qf1' : [family_data['qf1']['index'][35]]},
            prefix + '19C1'   : { 'qf1' : [family_data['qf1']['index'][36]]},
            prefix + '19C4'   : { 'qf1' : [family_data['qf1']['index'][37]]},
            prefix + '20C1'   : { 'qf1' : [family_data['qf1']['index'][38]]},
            prefix + '20C4'   : { 'qf1' : [family_data['qf1']['index'][39]]},
        }
        return _dict

    if element.lower() == 'sf1j':
        prefix = prefix + 'SF1J-'
        _dict = {
            prefix + '01C1'   : { 'sf1j' : [family_data['sf1j']['index'][0]]},
            prefix + '02C1'   : { 'sf1j' : [family_data['sf1j']['index'][1]]},
            prefix + '03C1'   : { 'sf1j' : [family_data['sf1j']['index'][2]]},
            prefix + '04C1'   : { 'sf1j' : [family_data['sf1j']['index'][3]]},
            prefix + '05C1'   : { 'sf1j' : [family_data['sf1j']['index'][4]]},
            prefix + '06C1'   : { 'sf1j' : [family_data['sf1j']['index'][5]]},
            prefix + '07C1'   : { 'sf1j' : [family_data['sf1j']['index'][6]]},
            prefix + '08C1'   : { 'sf1j' : [family_data['sf1j']['index'][7]]},
            prefix + '09C1'   : { 'sf1j' : [family_data['sf1j']['index'][8]]},
            prefix + '10C1'   : { 'sf1j' : [family_data['sf1j']['index'][9]]},
            prefix + '11C1'   : { 'sf1j' : [family_data['sf1j']['index'][10]]},
            prefix + '12C1'   : { 'sf1j' : [family_data['sf1j']['index'][11]]},
            prefix + '13C1'   : { 'sf1j' : [family_data['sf1j']['index'][12]]},
            prefix + '14C1'   : { 'sf1j' : [family_data['sf1j']['index'][13]]},
            prefix + '15C1'   : { 'sf1j' : [family_data['sf1j']['index'][14]]},
            prefix + '16C1'   : { 'sf1j' : [family_data['sf1j']['index'][15]]},
            prefix + '17C1'   : { 'sf1j' : [family_data['sf1j']['index'][16]]},
            prefix + '18C1'   : { 'sf1j' : [family_data['sf1j']['index'][17]]},
            prefix + '19C1'   : { 'sf1j' : [family_data['sf1j']['index'][18]]},
            prefix + '20C1'   : { 'sf1j' : [family_data['sf1j']['index'][19]]},
        }
        return _dict

    if element.lower() == 'qf2':
        prefix = prefix + 'QF2-'
        _dict = {
            prefix + '01C1'   : { 'qf2' : [family_data['qf2']['index'][0]]},
            prefix + '01C4'   : { 'qf2' : [family_data['qf2']['index'][1]]},
            prefix + '02C1'   : { 'qf2' : [family_data['qf2']['index'][2]]},
            prefix + '02C4'   : { 'qf2' : [family_data['qf2']['index'][3]]},
            prefix + '03C1'   : { 'qf2' : [family_data['qf2']['index'][4]]},
            prefix + '03C4'   : { 'qf2' : [family_data['qf2']['index'][5]]},
            prefix + '04C1'   : { 'qf2' : [family_data['qf2']['index'][6]]},
            prefix + '04C4'   : { 'qf2' : [family_data['qf2']['index'][7]]},
            prefix + '05C1'   : { 'qf2' : [family_data['qf2']['index'][8]]},
            prefix + '05C4'   : { 'qf2' : [family_data['qf2']['index'][9]]},
            prefix + '06C1'   : { 'qf2' : [family_data['qf2']['index'][10]]},
            prefix + '06C4'   : { 'qf2' : [family_data['qf2']['index'][11]]},
            prefix + '07C1'   : { 'qf2' : [family_data['qf2']['index'][12]]},
            prefix + '07C4'   : { 'qf2' : [family_data['qf2']['index'][13]]},
            prefix + '08C1'   : { 'qf2' : [family_data['qf2']['index'][14]]},
            prefix + '08C4'   : { 'qf2' : [family_data['qf2']['index'][15]]},
            prefix + '09C1'   : { 'qf2' : [family_data['qf2']['index'][16]]},
            prefix + '09C4'   : { 'qf2' : [family_data['qf2']['index'][17]]},
            prefix + '10C1'   : { 'qf2' : [family_data['qf2']['index'][18]]},
            prefix + '10C4'   : { 'qf2' : [family_data['qf2']['index'][19]]},
            prefix + '11C1'   : { 'qf2' : [family_data['qf2']['index'][20]]},
            prefix + '11C4'   : { 'qf2' : [family_data['qf2']['index'][21]]},
            prefix + '12C1'   : { 'qf2' : [family_data['qf2']['index'][22]]},
            prefix + '12C4'   : { 'qf2' : [family_data['qf2']['index'][23]]},
            prefix + '13C1'   : { 'qf2' : [family_data['qf2']['index'][24]]},
            prefix + '13C4'   : { 'qf2' : [family_data['qf2']['index'][25]]},
            prefix + '14C1'   : { 'qf2' : [family_data['qf2']['index'][26]]},
            prefix + '14C4'   : { 'qf2' : [family_data['qf2']['index'][27]]},
            prefix + '15C1'   : { 'qf2' : [family_data['qf2']['index'][28]]},
            prefix + '15C4'   : { 'qf2' : [family_data['qf2']['index'][29]]},
            prefix + '16C1'   : { 'qf2' : [family_data['qf2']['index'][30]]},
            prefix + '16C4'   : { 'qf2' : [family_data['qf2']['index'][31]]},
            prefix + '17C1'   : { 'qf2' : [family_data['qf2']['index'][32]]},
            prefix + '17C4'   : { 'qf2' : [family_data['qf2']['index'][33]]},
            prefix + '18C1'   : { 'qf2' : [family_data['qf2']['index'][34]]},
            prefix + '18C4'   : { 'qf2' : [family_data['qf2']['index'][35]]},
            prefix + '19C1'   : { 'qf2' : [family_data['qf2']['index'][36]]},
            prefix + '19C4'   : { 'qf2' : [family_data['qf2']['index'][37]]},
            prefix + '20C1'   : { 'qf2' : [family_data['qf2']['index'][38]]},
            prefix + '20C4'   : { 'qf2' : [family_data['qf2']['index'][39]]},
        }
        return _dict

    if element.lower() == 'sd2j':
        prefix = prefix + 'SD2J-'
        _dict = {
            prefix + '01C1'   : { 'sd2j' : [family_data['sd2j']['index'][0]]},
            prefix + '02C1'   : { 'sd2j' : [family_data['sd2j']['index'][1]]},
            prefix + '03C1'   : { 'sd2j' : [family_data['sd2j']['index'][2]]},
            prefix + '04C1'   : { 'sd2j' : [family_data['sd2j']['index'][3]]},
            prefix + '05C1'   : { 'sd2j' : [family_data['sd2j']['index'][4]]},
            prefix + '06C1'   : { 'sd2j' : [family_data['sd2j']['index'][5]]},
            prefix + '07C1'   : { 'sd2j' : [family_data['sd2j']['index'][6]]},
            prefix + '08C1'   : { 'sd2j' : [family_data['sd2j']['index'][7]]},
            prefix + '09C1'   : { 'sd2j' : [family_data['sd2j']['index'][8]]},
            prefix + '10C1'   : { 'sd2j' : [family_data['sd2j']['index'][9]]},
            prefix + '11C1'   : { 'sd2j' : [family_data['sd2j']['index'][10]]},
            prefix + '12C1'   : { 'sd2j' : [family_data['sd2j']['index'][11]]},
            prefix + '13C1'   : { 'sd2j' : [family_data['sd2j']['index'][12]]},
            prefix + '14C1'   : { 'sd2j' : [family_data['sd2j']['index'][13]]},
            prefix + '15C1'   : { 'sd2j' : [family_data['sd2j']['index'][14]]},
            prefix + '16C1'   : { 'sd2j' : [family_data['sd2j']['index'][15]]},
            prefix + '17C1'   : { 'sd2j' : [family_data['sd2j']['index'][16]]},
            prefix + '18C1'   : { 'sd2j' : [family_data['sd2j']['index'][17]]},
            prefix + '19C1'   : { 'sd2j' : [family_data['sd2j']['index'][18]]},
            prefix + '20C1'   : { 'sd2j' : [family_data['sd2j']['index'][19]]},
        }
        return _dict

    if element.lower() == 'sd3j':
        prefix = prefix + 'SD3J-'
        _dict = {
            prefix + '01C2'   : { 'sd3j' : [family_data['sd3j']['index'][0]]},
            prefix + '02C2'   : { 'sd3j' : [family_data['sd3j']['index'][1]]},
            prefix + '03C2'   : { 'sd3j' : [family_data['sd3j']['index'][2]]},
            prefix + '04C2'   : { 'sd3j' : [family_data['sd3j']['index'][3]]},
            prefix + '05C2'   : { 'sd3j' : [family_data['sd3j']['index'][4]]},
            prefix + '06C2'   : { 'sd3j' : [family_data['sd3j']['index'][5]]},
            prefix + '07C2'   : { 'sd3j' : [family_data['sd3j']['index'][6]]},
            prefix + '08C2'   : { 'sd3j' : [family_data['sd3j']['index'][7]]},
            prefix + '09C2'   : { 'sd3j' : [family_data['sd3j']['index'][8]]},
            prefix + '10C2'   : { 'sd3j' : [family_data['sd3j']['index'][9]]},
            prefix + '11C2'   : { 'sd3j' : [family_data['sd3j']['index'][10]]},
            prefix + '12C2'   : { 'sd3j' : [family_data['sd3j']['index'][11]]},
            prefix + '13C2'   : { 'sd3j' : [family_data['sd3j']['index'][12]]},
            prefix + '14C2'   : { 'sd3j' : [family_data['sd3j']['index'][13]]},
            prefix + '15C2'   : { 'sd3j' : [family_data['sd3j']['index'][14]]},
            prefix + '16C2'   : { 'sd3j' : [family_data['sd3j']['index'][15]]},
            prefix + '17C2'   : { 'sd3j' : [family_data['sd3j']['index'][16]]},
            prefix + '18C2'   : { 'sd3j' : [family_data['sd3j']['index'][17]]},
            prefix + '19C2'   : { 'sd3j' : [family_data['sd3j']['index'][18]]},
            prefix + '20C2'   : { 'sd3j' : [family_data['sd3j']['index'][19]]},
        }
        return _dict

    if element.lower() == 'qf3':
        prefix = prefix + 'QF3-'
        _dict = {
            prefix + '01C2'   : { 'qf3' : [family_data['qf3']['index'][0]]},
            prefix + '01C3'   : { 'qf3' : [family_data['qf3']['index'][1]]},
            prefix + '02C2'   : { 'qf3' : [family_data['qf3']['index'][2]]},
            prefix + '02C3'   : { 'qf3' : [family_data['qf3']['index'][3]]},
            prefix + '03C2'   : { 'qf3' : [family_data['qf3']['index'][4]]},
            prefix + '03C3'   : { 'qf3' : [family_data['qf3']['index'][5]]},
            prefix + '04C2'   : { 'qf3' : [family_data['qf3']['index'][6]]},
            prefix + '04C3'   : { 'qf3' : [family_data['qf3']['index'][7]]},
            prefix + '05C2'   : { 'qf3' : [family_data['qf3']['index'][8]]},
            prefix + '05C3'   : { 'qf3' : [family_data['qf3']['index'][9]]},
            prefix + '06C2'   : { 'qf3' : [family_data['qf3']['index'][10]]},
            prefix + '06C3'   : { 'qf3' : [family_data['qf3']['index'][11]]},
            prefix + '07C2'   : { 'qf3' : [family_data['qf3']['index'][12]]},
            prefix + '07C3'   : { 'qf3' : [family_data['qf3']['index'][13]]},
            prefix + '08C2'   : { 'qf3' : [family_data['qf3']['index'][14]]},
            prefix + '08C3'   : { 'qf3' : [family_data['qf3']['index'][15]]},
            prefix + '09C2'   : { 'qf3' : [family_data['qf3']['index'][16]]},
            prefix + '09C3'   : { 'qf3' : [family_data['qf3']['index'][17]]},
            prefix + '10C2'   : { 'qf3' : [family_data['qf3']['index'][18]]},
            prefix + '10C3'   : { 'qf3' : [family_data['qf3']['index'][19]]},
            prefix + '11C2'   : { 'qf3' : [family_data['qf3']['index'][20]]},
            prefix + '11C3'   : { 'qf3' : [family_data['qf3']['index'][21]]},
            prefix + '12C2'   : { 'qf3' : [family_data['qf3']['index'][22]]},
            prefix + '12C3'   : { 'qf3' : [family_data['qf3']['index'][23]]},
            prefix + '13C2'   : { 'qf3' : [family_data['qf3']['index'][24]]},
            prefix + '13C3'   : { 'qf3' : [family_data['qf3']['index'][25]]},
            prefix + '14C2'   : { 'qf3' : [family_data['qf3']['index'][26]]},
            prefix + '14C3'   : { 'qf3' : [family_data['qf3']['index'][27]]},
            prefix + '15C2'   : { 'qf3' : [family_data['qf3']['index'][28]]},
            prefix + '15C3'   : { 'qf3' : [family_data['qf3']['index'][29]]},
            prefix + '16C2'   : { 'qf3' : [family_data['qf3']['index'][30]]},
            prefix + '16C3'   : { 'qf3' : [family_data['qf3']['index'][31]]},
            prefix + '17C2'   : { 'qf3' : [family_data['qf3']['index'][32]]},
            prefix + '17C3'   : { 'qf3' : [family_data['qf3']['index'][33]]},
            prefix + '18C2'   : { 'qf3' : [family_data['qf3']['index'][34]]},
            prefix + '18C3'   : { 'qf3' : [family_data['qf3']['index'][35]]},
            prefix + '19C2'   : { 'qf3' : [family_data['qf3']['index'][36]]},
            prefix + '19C3'   : { 'qf3' : [family_data['qf3']['index'][37]]},
            prefix + '20C2'   : { 'qf3' : [family_data['qf3']['index'][38]]},
            prefix + '20C3'   : { 'qf3' : [family_data['qf3']['index'][39]]},
        }
        return _dict

    if element.lower() == 'sf2j':
        prefix = prefix + 'SF2J-'
        _dict = {
            prefix + '01C2'   : { 'sf2j' : [family_data['sf2j']['index'][0]]},
            prefix + '02C2'   : { 'sf2j' : [family_data['sf2j']['index'][1]]},
            prefix + '03C2'   : { 'sf2j' : [family_data['sf2j']['index'][2]]},
            prefix + '04C2'   : { 'sf2j' : [family_data['sf2j']['index'][3]]},
            prefix + '05C2'   : { 'sf2j' : [family_data['sf2j']['index'][4]]},
            prefix + '06C2'   : { 'sf2j' : [family_data['sf2j']['index'][5]]},
            prefix + '07C2'   : { 'sf2j' : [family_data['sf2j']['index'][6]]},
            prefix + '08C2'   : { 'sf2j' : [family_data['sf2j']['index'][7]]},
            prefix + '09C2'   : { 'sf2j' : [family_data['sf2j']['index'][8]]},
            prefix + '10C2'   : { 'sf2j' : [family_data['sf2j']['index'][9]]},
            prefix + '11C2'   : { 'sf2j' : [family_data['sf2j']['index'][10]]},
            prefix + '12C2'   : { 'sf2j' : [family_data['sf2j']['index'][11]]},
            prefix + '13C2'   : { 'sf2j' : [family_data['sf2j']['index'][12]]},
            prefix + '14C2'   : { 'sf2j' : [family_data['sf2j']['index'][13]]},
            prefix + '15C2'   : { 'sf2j' : [family_data['sf2j']['index'][14]]},
            prefix + '16C2'   : { 'sf2j' : [family_data['sf2j']['index'][15]]},
            prefix + '17C2'   : { 'sf2j' : [family_data['sf2j']['index'][16]]},
            prefix + '18C2'   : { 'sf2j' : [family_data['sf2j']['index'][17]]},
            prefix + '19C2'   : { 'sf2j' : [family_data['sf2j']['index'][18]]},
            prefix + '20C2'   : { 'sf2j' : [family_data['sf2j']['index'][19]]},
        }
        return _dict

    if element.lower() == 'qf4':
        prefix = prefix + 'QF4-'
        _dict = {
            prefix + '01C2'   : { 'qf4' : [family_data['qf4']['index'][0]]},
            prefix + '01C3'   : { 'qf4' : [family_data['qf4']['index'][1]]},
            prefix + '02C2'   : { 'qf4' : [family_data['qf4']['index'][2]]},
            prefix + '02C3'   : { 'qf4' : [family_data['qf4']['index'][3]]},
            prefix + '03C2'   : { 'qf4' : [family_data['qf4']['index'][4]]},
            prefix + '03C3'   : { 'qf4' : [family_data['qf4']['index'][5]]},
            prefix + '04C2'   : { 'qf4' : [family_data['qf4']['index'][6]]},
            prefix + '04C3'   : { 'qf4' : [family_data['qf4']['index'][7]]},
            prefix + '05C2'   : { 'qf4' : [family_data['qf4']['index'][8]]},
            prefix + '05C3'   : { 'qf4' : [family_data['qf4']['index'][9]]},
            prefix + '06C2'   : { 'qf4' : [family_data['qf4']['index'][10]]},
            prefix + '06C3'   : { 'qf4' : [family_data['qf4']['index'][11]]},
            prefix + '07C2'   : { 'qf4' : [family_data['qf4']['index'][12]]},
            prefix + '07C3'   : { 'qf4' : [family_data['qf4']['index'][13]]},
            prefix + '08C2'   : { 'qf4' : [family_data['qf4']['index'][14]]},
            prefix + '08C3'   : { 'qf4' : [family_data['qf4']['index'][15]]},
            prefix + '09C2'   : { 'qf4' : [family_data['qf4']['index'][16]]},
            prefix + '09C3'   : { 'qf4' : [family_data['qf4']['index'][17]]},
            prefix + '10C2'   : { 'qf4' : [family_data['qf4']['index'][18]]},
            prefix + '10C3'   : { 'qf4' : [family_data['qf4']['index'][19]]},
            prefix + '11C2'   : { 'qf4' : [family_data['qf4']['index'][20]]},
            prefix + '11C3'   : { 'qf4' : [family_data['qf4']['index'][21]]},
            prefix + '12C2'   : { 'qf4' : [family_data['qf4']['index'][22]]},
            prefix + '12C3'   : { 'qf4' : [family_data['qf4']['index'][23]]},
            prefix + '13C2'   : { 'qf4' : [family_data['qf4']['index'][24]]},
            prefix + '13C3'   : { 'qf4' : [family_data['qf4']['index'][25]]},
            prefix + '14C2'   : { 'qf4' : [family_data['qf4']['index'][26]]},
            prefix + '14C3'   : { 'qf4' : [family_data['qf4']['index'][27]]},
            prefix + '15C2'   : { 'qf4' : [family_data['qf4']['index'][28]]},
            prefix + '15C3'   : { 'qf4' : [family_data['qf4']['index'][29]]},
            prefix + '16C2'   : { 'qf4' : [family_data['qf4']['index'][30]]},
            prefix + '16C3'   : { 'qf4' : [family_data['qf4']['index'][31]]},
            prefix + '17C2'   : { 'qf4' : [family_data['qf4']['index'][32]]},
            prefix + '17C3'   : { 'qf4' : [family_data['qf4']['index'][33]]},
            prefix + '18C2'   : { 'qf4' : [family_data['qf4']['index'][34]]},
            prefix + '18C3'   : { 'qf4' : [family_data['qf4']['index'][35]]},
            prefix + '19C2'   : { 'qf4' : [family_data['qf4']['index'][36]]},
            prefix + '19C3'   : { 'qf4' : [family_data['qf4']['index'][37]]},
            prefix + '20C2'   : { 'qf4' : [family_data['qf4']['index'][38]]},
            prefix + '20C3'   : { 'qf4' : [family_data['qf4']['index'][39]]},
        }
        return _dict

    if element.lower() == 'sf2k':
        prefix = prefix + 'SF2K-'
        _dict = {
            prefix + '01C3'   : { 'sf2k' : [family_data['sf2k']['index'][0]]},
            prefix + '02C3'   : { 'sf2k' : [family_data['sf2k']['index'][1]]},
            prefix + '03C3'   : { 'sf2k' : [family_data['sf2k']['index'][2]]},
            prefix + '04C3'   : { 'sf2k' : [family_data['sf2k']['index'][3]]},
            prefix + '05C3'   : { 'sf2k' : [family_data['sf2k']['index'][4]]},
            prefix + '06C3'   : { 'sf2k' : [family_data['sf2k']['index'][5]]},
            prefix + '07C3'   : { 'sf2k' : [family_data['sf2k']['index'][6]]},
            prefix + '08C3'   : { 'sf2k' : [family_data['sf2k']['index'][7]]},
            prefix + '09C3'   : { 'sf2k' : [family_data['sf2k']['index'][8]]},
            prefix + '10C3'   : { 'sf2k' : [family_data['sf2k']['index'][9]]},
            prefix + '11C3'   : { 'sf2k' : [family_data['sf2k']['index'][10]]},
            prefix + '12C3'   : { 'sf2k' : [family_data['sf2k']['index'][11]]},
            prefix + '13C3'   : { 'sf2k' : [family_data['sf2k']['index'][12]]},
            prefix + '14C3'   : { 'sf2k' : [family_data['sf2k']['index'][13]]},
            prefix + '15C3'   : { 'sf2k' : [family_data['sf2k']['index'][14]]},
            prefix + '16C3'   : { 'sf2k' : [family_data['sf2k']['index'][15]]},
            prefix + '17C3'   : { 'sf2k' : [family_data['sf2k']['index'][16]]},
            prefix + '18C3'   : { 'sf2k' : [family_data['sf2k']['index'][17]]},
            prefix + '19C3'   : { 'sf2k' : [family_data['sf2k']['index'][18]]},
            prefix + '20C3'   : { 'sf2k' : [family_data['sf2k']['index'][19]]},
        }
        return _dict

    if element.lower() == 'sd3k':
        prefix = prefix + 'SD3K-'
        _dict = {
            prefix + '01C3'   : { 'sd3k' : [family_data['sd3k']['index'][0]]},
            prefix + '02C3'   : { 'sd3k' : [family_data['sd3k']['index'][1]]},
            prefix + '03C3'   : { 'sd3k' : [family_data['sd3k']['index'][2]]},
            prefix + '04C3'   : { 'sd3k' : [family_data['sd3k']['index'][3]]},
            prefix + '05C3'   : { 'sd3k' : [family_data['sd3k']['index'][4]]},
            prefix + '06C3'   : { 'sd3k' : [family_data['sd3k']['index'][5]]},
            prefix + '07C3'   : { 'sd3k' : [family_data['sd3k']['index'][6]]},
            prefix + '08C3'   : { 'sd3k' : [family_data['sd3k']['index'][7]]},
            prefix + '09C3'   : { 'sd3k' : [family_data['sd3k']['index'][8]]},
            prefix + '10C3'   : { 'sd3k' : [family_data['sd3k']['index'][9]]},
            prefix + '11C3'   : { 'sd3k' : [family_data['sd3k']['index'][10]]},
            prefix + '12C3'   : { 'sd3k' : [family_data['sd3k']['index'][11]]},
            prefix + '13C3'   : { 'sd3k' : [family_data['sd3k']['index'][12]]},
            prefix + '14C3'   : { 'sd3k' : [family_data['sd3k']['index'][13]]},
            prefix + '15C3'   : { 'sd3k' : [family_data['sd3k']['index'][14]]},
            prefix + '16C3'   : { 'sd3k' : [family_data['sd3k']['index'][15]]},
            prefix + '17C3'   : { 'sd3k' : [family_data['sd3k']['index'][16]]},
            prefix + '18C3'   : { 'sd3k' : [family_data['sd3k']['index'][17]]},
            prefix + '19C3'   : { 'sd3k' : [family_data['sd3k']['index'][18]]},
            prefix + '20C3'   : { 'sd3k' : [family_data['sd3k']['index'][19]]},
        }
        return _dict

    if element.lower() == 'sd2k':
        prefix = prefix + 'SD2K-'
        _dict = {
            prefix + '01C4'   : { 'sd2k' : [family_data['sd2k']['index'][0]]},
            prefix + '02C4'   : { 'sd2k' : [family_data['sd2k']['index'][1]]},
            prefix + '03C4'   : { 'sd2k' : [family_data['sd2k']['index'][2]]},
            prefix + '04C4'   : { 'sd2k' : [family_data['sd2k']['index'][3]]},
            prefix + '05C4'   : { 'sd2k' : [family_data['sd2k']['index'][4]]},
            prefix + '06C4'   : { 'sd2k' : [family_data['sd2k']['index'][5]]},
            prefix + '07C4'   : { 'sd2k' : [family_data['sd2k']['index'][6]]},
            prefix + '08C4'   : { 'sd2k' : [family_data['sd2k']['index'][7]]},
            prefix + '09C4'   : { 'sd2k' : [family_data['sd2k']['index'][8]]},
            prefix + '10C4'   : { 'sd2k' : [family_data['sd2k']['index'][9]]},
            prefix + '11C4'   : { 'sd2k' : [family_data['sd2k']['index'][10]]},
            prefix + '12C4'   : { 'sd2k' : [family_data['sd2k']['index'][11]]},
            prefix + '13C4'   : { 'sd2k' : [family_data['sd2k']['index'][12]]},
            prefix + '14C4'   : { 'sd2k' : [family_data['sd2k']['index'][13]]},
            prefix + '15C4'   : { 'sd2k' : [family_data['sd2k']['index'][14]]},
            prefix + '16C4'   : { 'sd2k' : [family_data['sd2k']['index'][15]]},
            prefix + '17C4'   : { 'sd2k' : [family_data['sd2k']['index'][16]]},
            prefix + '18C4'   : { 'sd2k' : [family_data['sd2k']['index'][17]]},
            prefix + '19C4'   : { 'sd2k' : [family_data['sd2k']['index'][18]]},
            prefix + '20C4'   : { 'sd2k' : [family_data['sd2k']['index'][19]]},
        }
        return _dict

    if element.lower() == 'sf1k':
        prefix = prefix + 'SF1K-'
        _dict = {
            prefix + '01C4'   : { 'sf1k' : [family_data['sf1k']['index'][0]]},
            prefix + '02C4'   : { 'sf1k' : [family_data['sf1k']['index'][1]]},
            prefix + '03C4'   : { 'sf1k' : [family_data['sf1k']['index'][2]]},
            prefix + '04C4'   : { 'sf1k' : [family_data['sf1k']['index'][3]]},
            prefix + '05C4'   : { 'sf1k' : [family_data['sf1k']['index'][4]]},
            prefix + '06C4'   : { 'sf1k' : [family_data['sf1k']['index'][5]]},
            prefix + '07C4'   : { 'sf1k' : [family_data['sf1k']['index'][6]]},
            prefix + '08C4'   : { 'sf1k' : [family_data['sf1k']['index'][7]]},
            prefix + '09C4'   : { 'sf1k' : [family_data['sf1k']['index'][8]]},
            prefix + '10C4'   : { 'sf1k' : [family_data['sf1k']['index'][9]]},
            prefix + '11C4'   : { 'sf1k' : [family_data['sf1k']['index'][10]]},
            prefix + '12C4'   : { 'sf1k' : [family_data['sf1k']['index'][11]]},
            prefix + '13C4'   : { 'sf1k' : [family_data['sf1k']['index'][12]]},
            prefix + '14C4'   : { 'sf1k' : [family_data['sf1k']['index'][13]]},
            prefix + '15C4'   : { 'sf1k' : [family_data['sf1k']['index'][14]]},
            prefix + '16C4'   : { 'sf1k' : [family_data['sf1k']['index'][15]]},
            prefix + '17C4'   : { 'sf1k' : [family_data['sf1k']['index'][16]]},
            prefix + '18C4'   : { 'sf1k' : [family_data['sf1k']['index'][17]]},
            prefix + '19C4'   : { 'sf1k' : [family_data['sf1k']['index'][18]]},
            prefix + '20C4'   : { 'sf1k' : [family_data['sf1k']['index'][19]]},
        }
        return _dict

    if element.lower() == 'sd1k':
        prefix = prefix + 'SD1K-'
        _dict = {
            prefix + '01C4'   : { 'sd1k' : [family_data['sd1k']['index'][0]]},
            prefix + '02C4'   : { 'sd1k' : [family_data['sd1k']['index'][1]]},
            prefix + '03C4'   : { 'sd1k' : [family_data['sd1k']['index'][2]]},
            prefix + '04C4'   : { 'sd1k' : [family_data['sd1k']['index'][3]]},
            prefix + '05C4'   : { 'sd1k' : [family_data['sd1k']['index'][4]]},
            prefix + '06C4'   : { 'sd1k' : [family_data['sd1k']['index'][5]]},
            prefix + '07C4'   : { 'sd1k' : [family_data['sd1k']['index'][6]]},
            prefix + '08C4'   : { 'sd1k' : [family_data['sd1k']['index'][7]]},
            prefix + '09C4'   : { 'sd1k' : [family_data['sd1k']['index'][8]]},
            prefix + '10C4'   : { 'sd1k' : [family_data['sd1k']['index'][9]]},
            prefix + '11C4'   : { 'sd1k' : [family_data['sd1k']['index'][10]]},
            prefix + '12C4'   : { 'sd1k' : [family_data['sd1k']['index'][11]]},
            prefix + '13C4'   : { 'sd1k' : [family_data['sd1k']['index'][12]]},
            prefix + '14C4'   : { 'sd1k' : [family_data['sd1k']['index'][13]]},
            prefix + '15C4'   : { 'sd1k' : [family_data['sd1k']['index'][14]]},
            prefix + '16C4'   : { 'sd1k' : [family_data['sd1k']['index'][15]]},
            prefix + '17C4'   : { 'sd1k' : [family_data['sd1k']['index'][16]]},
            prefix + '18C4'   : { 'sd1k' : [family_data['sd1k']['index'][17]]},
            prefix + '19C4'   : { 'sd1k' : [family_data['sd1k']['index'][18]]},
            prefix + '20C4'   : { 'sd1k' : [family_data['sd1k']['index'][19]]},
        }
        return _dict

    if element.lower() == 'sdb':
        prefix = prefix + 'SDB-'
        _dict = {
            prefix + '02M1'   : { 'sdb' : [family_data['sdb']['index'][0]]},
            prefix + '03M1'   : { 'sdb' : [family_data['sdb']['index'][1]]},
            prefix + '04M1'   : { 'sdb' : [family_data['sdb']['index'][2]]},
            prefix + '05M1'   : { 'sdb' : [family_data['sdb']['index'][3]]},
            prefix + '06M1'   : { 'sdb' : [family_data['sdb']['index'][4]]},
            prefix + '07M1'   : { 'sdb' : [family_data['sdb']['index'][5]]},
            prefix + '08M1'   : { 'sdb' : [family_data['sdb']['index'][6]]},
            prefix + '09M1'   : { 'sdb' : [family_data['sdb']['index'][7]]},
            prefix + '10M1'   : { 'sdb' : [family_data['sdb']['index'][8]]},
            prefix + '11M1'   : { 'sdb' : [family_data['sdb']['index'][9]]},
            prefix + '12M1'   : { 'sdb' : [family_data['sdb']['index'][10]]},
            prefix + '13M1'   : { 'sdb' : [family_data['sdb']['index'][11]]},
            prefix + '14M1'   : { 'sdb' : [family_data['sdb']['index'][12]]},
            prefix + '15M1'   : { 'sdb' : [family_data['sdb']['index'][13]]},
            prefix + '16M1'   : { 'sdb' : [family_data['sdb']['index'][14]]},
            prefix + '17M1'   : { 'sdb' : [family_data['sdb']['index'][15]]},
            prefix + '18M1'   : { 'sdb' : [family_data['sdb']['index'][16]]},
            prefix + '19M1'   : { 'sdb' : [family_data['sdb']['index'][17]]},
            prefix + '20M1'   : { 'sdb' : [family_data['sdb']['index'][18]]},
            prefix + '01M1'   : { 'sdb' : [family_data['sdb']['index'][19]]},
        }
        return _dict

    if element.lower() == 'qdb1':
        prefix = prefix + 'QDB1-'
        _dict = {
            prefix + '02M1'   : { 'qdb1' : [family_data['qdb1']['index'][0]]},
            prefix + '03M1'   : { 'qdb1' : [family_data['qdb1']['index'][1]]},
            prefix + '04M1'   : { 'qdb1' : [family_data['qdb1']['index'][2]]},
            prefix + '05M1'   : { 'qdb1' : [family_data['qdb1']['index'][3]]},
            prefix + '06M1'   : { 'qdb1' : [family_data['qdb1']['index'][4]]},
            prefix + '07M1'   : { 'qdb1' : [family_data['qdb1']['index'][5]]},
            prefix + '08M1'   : { 'qdb1' : [family_data['qdb1']['index'][6]]},
            prefix + '09M1'   : { 'qdb1' : [family_data['qdb1']['index'][7]]},
            prefix + '10M1'   : { 'qdb1' : [family_data['qdb1']['index'][8]]},
            prefix + '11M1'   : { 'qdb1' : [family_data['qdb1']['index'][9]]},
            prefix + '12M1'   : { 'qdb1' : [family_data['qdb1']['index'][10]]},
            prefix + '13M1'   : { 'qdb1' : [family_data['qdb1']['index'][11]]},
            prefix + '14M1'   : { 'qdb1' : [family_data['qdb1']['index'][12]]},
            prefix + '15M1'   : { 'qdb1' : [family_data['qdb1']['index'][13]]},
            prefix + '16M1'   : { 'qdb1' : [family_data['qdb1']['index'][14]]},
            prefix + '17M1'   : { 'qdb1' : [family_data['qdb1']['index'][15]]},
            prefix + '18M1'   : { 'qdb1' : [family_data['qdb1']['index'][16]]},
            prefix + '19M1'   : { 'qdb1' : [family_data['qdb1']['index'][17]]},
            prefix + '20M1'   : { 'qdb1' : [family_data['qdb1']['index'][18]]},
            prefix + '01M1'   : { 'qdb1' : [family_data['qdb1']['index'][19]]},
        }
        return _dict

    if element.lower() == 'qfb':
        prefix = prefix + 'QFB-'
        _dict = {
            prefix + '02M1'   : { 'qfb' : [family_data['qfb']['index'][0]]},
            prefix + '03M1'   : { 'qfb' : [family_data['qfb']['index'][1]]},
            prefix + '04M1'   : { 'qfb' : [family_data['qfb']['index'][2]]},
            prefix + '05M1'   : { 'qfb' : [family_data['qfb']['index'][3]]},
            prefix + '06M1'   : { 'qfb' : [family_data['qfb']['index'][4]]},
            prefix + '07M1'   : { 'qfb' : [family_data['qfb']['index'][5]]},
            prefix + '08M1'   : { 'qfb' : [family_data['qfb']['index'][6]]},
            prefix + '09M1'   : { 'qfb' : [family_data['qfb']['index'][7]]},
            prefix + '10M1'   : { 'qfb' : [family_data['qfb']['index'][8]]},
            prefix + '11M1'   : { 'qfb' : [family_data['qfb']['index'][9]]},
            prefix + '12M1'   : { 'qfb' : [family_data['qfb']['index'][10]]},
            prefix + '13M1'   : { 'qfb' : [family_data['qfb']['index'][11]]},
            prefix + '14M1'   : { 'qfb' : [family_data['qfb']['index'][12]]},
            prefix + '15M1'   : { 'qfb' : [family_data['qfb']['index'][13]]},
            prefix + '16M1'   : { 'qfb' : [family_data['qfb']['index'][14]]},
            prefix + '17M1'   : { 'qfb' : [family_data['qfb']['index'][15]]},
            prefix + '18M1'   : { 'qfb' : [family_data['qfb']['index'][16]]},
            prefix + '19M1'   : { 'qfb' : [family_data['qfb']['index'][17]]},
            prefix + '20M1'   : { 'qfb' : [family_data['qfb']['index'][18]]},
            prefix + '01M1'   : { 'qfb' : [family_data['qfb']['index'][19]]},
        }
        return _dict

    if element.lower() == 'sfb':
        prefix = prefix + 'SFB-'
        _dict = {
            prefix + '02M1'   : { 'sfb' : [family_data['sfb']['index'][0]]},
            prefix + '03M1'   : { 'sfb' : [family_data['sfb']['index'][1]]},
            prefix + '04M1'   : { 'sfb' : [family_data['sfb']['index'][2]]},
            prefix + '05M1'   : { 'sfb' : [family_data['sfb']['index'][3]]},
            prefix + '06M1'   : { 'sfb' : [family_data['sfb']['index'][4]]},
            prefix + '07M1'   : { 'sfb' : [family_data['sfb']['index'][5]]},
            prefix + '08M1'   : { 'sfb' : [family_data['sfb']['index'][6]]},
            prefix + '09M1'   : { 'sfb' : [family_data['sfb']['index'][7]]},
            prefix + '10M1'   : { 'sfb' : [family_data['sfb']['index'][8]]},
            prefix + '11M1'   : { 'sfb' : [family_data['sfb']['index'][9]]},
            prefix + '12M1'   : { 'sfb' : [family_data['sfb']['index'][10]]},
            prefix + '13M1'   : { 'sfb' : [family_data['sfb']['index'][11]]},
            prefix + '14M1'   : { 'sfb' : [family_data['sfb']['index'][12]]},
            prefix + '15M1'   : { 'sfb' : [family_data['sfb']['index'][13]]},
            prefix + '16M1'   : { 'sfb' : [family_data['sfb']['index'][14]]},
            prefix + '17M1'   : { 'sfb' : [family_data['sfb']['index'][15]]},
            prefix + '18M1'   : { 'sfb' : [family_data['sfb']['index'][16]]},
            prefix + '19M1'   : { 'sfb' : [family_data['sfb']['index'][17]]},
            prefix + '20M1'   : { 'sfb' : [family_data['sfb']['index'][18]]},
            prefix + '01M1'   : { 'sfb' : [family_data['sfb']['index'][19]]},
        }
        return _dict

    if element.lower() == 'qdb2':
        prefix = prefix + 'QDB2-'
        _dict = {
            prefix + '02M1'   : { 'qdb2' : [family_data['qdb2']['index'][0]]},
            prefix + '03M1'   : { 'qdb2' : [family_data['qdb2']['index'][1]]},
            prefix + '04M1'   : { 'qdb2' : [family_data['qdb2']['index'][2]]},
            prefix + '05M1'   : { 'qdb2' : [family_data['qdb2']['index'][3]]},
            prefix + '06M1'   : { 'qdb2' : [family_data['qdb2']['index'][4]]},
            prefix + '07M1'   : { 'qdb2' : [family_data['qdb2']['index'][5]]},
            prefix + '08M1'   : { 'qdb2' : [family_data['qdb2']['index'][6]]},
            prefix + '09M1'   : { 'qdb2' : [family_data['qdb2']['index'][7]]},
            prefix + '10M1'   : { 'qdb2' : [family_data['qdb2']['index'][8]]},
            prefix + '11M1'   : { 'qdb2' : [family_data['qdb2']['index'][9]]},
            prefix + '12M1'   : { 'qdb2' : [family_data['qdb2']['index'][10]]},
            prefix + '13M1'   : { 'qdb2' : [family_data['qdb2']['index'][11]]},
            prefix + '14M1'   : { 'qdb2' : [family_data['qdb2']['index'][12]]},
            prefix + '15M1'   : { 'qdb2' : [family_data['qdb2']['index'][13]]},
            prefix + '16M1'   : { 'qdb2' : [family_data['qdb2']['index'][14]]},
            prefix + '17M1'   : { 'qdb2' : [family_data['qdb2']['index'][15]]},
            prefix + '18M1'   : { 'qdb2' : [family_data['qdb2']['index'][16]]},
            prefix + '19M1'   : { 'qdb2' : [family_data['qdb2']['index'][17]]},
            prefix + '20M1'   : { 'qdb2' : [family_data['qdb2']['index'][18]]},
            prefix + '01M1'   : { 'qdb2' : [family_data['qdb2']['index'][19]]},
        }
        return _dict

    else:
        raise Exception('Element %s not found'%element)


def get_magnet_names(accelerator):
    return get_record_names(accelerator, 'sima')