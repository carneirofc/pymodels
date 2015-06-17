
import sirius

def families_dipoles():
    return ('bend',)

def families_quadrupoles():
    return ('qfa', 'qda', 'qfb', 'qdb1', 'qdb2','qf1', 'qf2', 'qf3', 'qf4',)

def families_sextupoles():
    return ('sfa', 'sda', 'sfb', 'sdb','sd1', 'sd2', 'sd3', 'sd4', 'sd5', 'sd6','sf1', 'sf2', 'sf3', 'sf4',)

def families_horizontal_correctors():
    return ('chf', 'chs',)

def families_vertical_correctors():
    return ('cvf', 'cvs',)

def families_skew_correctors():
    return ('qs',)

def families_rf():
    return ('cav',)

def get_record_names(family_name = None):

    family_data = sirius.SI_V07.lattice._family_data

    if family_name == None:

        families = ['sipa', 'sidi', 'sirf']

        # record_name groups for individual magnets
        families.extend(families_quadrupoles())
        families.extend(families_sextupoles())
        families.extend(families_horizontal_correctors())
        families.extend(families_vertical_correctors())
        families.extend(families_skew_correctors())
        # record_name groups for families
        families.extend([name+'-fam' for name in families_dipoles()])
        families.extend([name+'-fam' for name in families_quadrupoles()])
        families.extend([name+'-fam' for name in families_sextupoles()])


        record_names_dict = {}
        for i in range(len(families)):
            record_names_dict.update(get_record_names(families[i]))
        return record_names_dict

    if family_name.lower() == 'sirf':
        indices = family_data['cav']['index']
        #_dict = {'SIRF-FREQUENCY': {'cav': indices}}
        #return _dict
        _dict = {
            'SIRF-FREQUENCY':{'cav':indices},
            'SIRF-VOLTAGE':{'cav':indices},
        }
        return _dict

    if family_name.lower() == 'sipa':
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

    if family_name.lower() == 'sidi':
        _dict = {
                'SIDI-TUNEH':{},
                'SIDI-TUNEV':{},
                'SIDI-TUNES':{},
                'SIDI-CURRENT':{},
                'SIDI-BCURRENT':{},
        }
        bpm_dict = get_record_names(family_name = 'bpm')
        _dict.update(bpm_dict)
        bpm_fam_dict = get_record_names(family_name = 'bpm-fam')
        _dict.update(bpm_fam_dict)
        return _dict

    if family_name.lower() == 'bpm-fam':
        indices = family_data['bpm']['index']
        _dict = {'SIDI-BPM-FAM-X': {'bpm': indices},
                 'SIDI-BPM-FAM-Y': {'bpm': indices}
                }
        return _dict

    if family_name.lower() == 'qfa-fam':
        indices = family_data['qfa']['index']
        _dict = {'SIPS-QFA-FAM': {'qfa': indices}}
        return _dict

    if family_name.lower() == 'qda-fam':
        indices = family_data['qda']['index']
        _dict = {'SIPS-QDA-FAM': {'qda': indices}}
        return _dict

    if family_name.lower() == 'qfb-fam':
        indices = family_data['qfb']['index']
        _dict = {'SIPS-QFB-FAM': {'qfb': indices}}
        return _dict

    if family_name.lower() == 'qdb1-fam':
        indices = family_data['qdb1']['index']
        _dict = {'SIPS-QDB1-FAM': {'qdb1': indices}}
        return _dict

    if family_name.lower() == 'qdb2-fam':
        indices = family_data['qdb2']['index']
        _dict = {'SIPS-QDB2-FAM': {'qdb2': indices}}
        return _dict

    if family_name.lower() == 'qf1-fam':
        indices = family_data['qf1']['index']
        _dict = {'SIPS-QF1-FAM': {'qf1': indices}}
        return _dict

    if family_name.lower() == 'qf2-fam':
        indices = family_data['qf2']['index']
        _dict = {'SIPS-QF2-FAM': {'qf2': indices}}
        return _dict

    if family_name.lower() == 'qf3-fam':
        indices = family_data['qf3']['index']
        _dict = {'SIPS-QF3-FAM': {'qf3': indices}}
        return _dict

    if family_name.lower() == 'qf4-fam':
        indices = family_data['qf4']['index']
        _dict = {'SIPS-QF4-FAM': {'qf4': indices}}
        return _dict

    if family_name.lower() == 'sfa-fam':
        indices = family_data['sfa']['index']
        _dict = {'SIPS-SFA-FAM': {'sfa': indices}}
        return _dict

    if family_name.lower() == 'sda-fam':
        indices = family_data['sda']['index']
        _dict = {'SIPS-SDA-FAM': {'sda': indices}}
        return _dict

    if family_name.lower() == 'sd1-fam':
        indices = family_data['sd1']['index']
        _dict = {'SIPS-SD1-FAM': {'sd1': indices}}
        return _dict

    if family_name.lower() == 'sf1-fam':
        indices = family_data['sf1']['index']
        _dict = {'SIPS-SF1-FAM': {'sf1': indices}}
        return _dict

    if family_name.lower() == 'sd2-fam':
        indices = family_data['sd2']['index']
        _dict = {'SIPS-SD2-FAM': {'sd2': indices}}
        return _dict

    if family_name.lower() == 'sd3-fam':
        indices = family_data['sd3']['index']
        _dict = {'SIPS-SD3-FAM': {'sd3': indices}}
        return _dict

    if family_name.lower() == 'sf2-fam':
        indices = family_data['sf2']['index']
        _dict = {'SIPS-SF2-FAM': {'sf2': indices}}
        return _dict

    if family_name.lower() == 'sf3-fam':
        indices = family_data['sf3']['index']
        _dict = {'SIPS-SF3-FAM': {'sf3': indices}}
        return _dict

    if family_name.lower() == 'sd4-fam':
        indices = family_data['sd4']['index']
        _dict = {'SIPS-SD4-FAM': {'sd4': indices}}
        return _dict

    if family_name.lower() == 'sd5-fam':
        indices = family_data['sd5']['index']
        _dict = {'SIPS-SD5-FAM': {'sd5': indices}}
        return _dict

    if family_name.lower() == 'sf4-fam':
        indices = family_data['sf4']['index']
        _dict = {'SIPS-SF4-FAM': {'sf4': indices}}
        return _dict

    if family_name.lower() == 'sd6-fam':
        indices = family_data['sd6']['index']
        _dict = {'SIPS-SD6-FAM': {'sd6': indices}}
        return _dict

    if family_name.lower() == 'sdb-fam':
        indices = family_data['sdb']['index']
        _dict = {'SIPS-SDB-FAM': {'sdb': indices}}
        return _dict

    if family_name.lower() == 'sfb-fam':
        indices = family_data['sfb']['index']
        _dict = {'SIPS-SFB-FAM': {'sfb': indices}}
        return _dict

    if family_name.lower() == 'bpm':
        indices = family_data['bpm']['index']
        prefix = 'SIDI-BPM-'
        bpm_dict = {

            #Sector 01
            prefix + '01M1'   : {'bpm' : [indices[179]]},
            prefix + '01M2'   : {'bpm' : [family_data['bpm']['index'][0]]},
            prefix + '01C1-A' : {'bpm' : [family_data['bpm']['index'][1]]},
            prefix + '01C1-B' : {'bpm' : [family_data['bpm']['index'][2]]},
            prefix + '01C2-A' : {'bpm' : [family_data['bpm']['index'][3]]},
            prefix + '01C2-B' : {'bpm' : [family_data['bpm']['index'][4]]},
            prefix + '01C4'   : {'bpm' : [family_data['bpm']['index'][5]]},
            prefix + '01C5-A' : {'bpm' : [family_data['bpm']['index'][6]]},
            prefix + '01C5-B' : {'bpm' : [family_data['bpm']['index'][7]]},

            #Sector 02
            prefix + '02M1'   : {'bpm' : [family_data['bpm']['index'][8]]},
            prefix + '02M2'   : {'bpm' : [family_data['bpm']['index'][9]]},
            prefix + '02C1-A' : {'bpm' : [family_data['bpm']['index'][10]]},
            prefix + '02C1-B' : {'bpm' : [family_data['bpm']['index'][11]]},
            prefix + '02C2-A' : {'bpm' : [family_data['bpm']['index'][12]]},
            prefix + '02C2-B' : {'bpm' : [family_data['bpm']['index'][13]]},
            prefix + '02C4'   : {'bpm' : [family_data['bpm']['index'][14]]},
            prefix + '02C5-A' : {'bpm' : [family_data['bpm']['index'][15]]},
            prefix + '02C5-B' : {'bpm' : [family_data['bpm']['index'][16]]},

            #Sector 03
            prefix + '03M1'   : {'bpm' : [family_data['bpm']['index'][17]]},
            prefix + '03M2'   : {'bpm' : [family_data['bpm']['index'][18]]},
            prefix + '03C1-A' : {'bpm' : [family_data['bpm']['index'][19]]},
            prefix + '03C1-B' : {'bpm' : [family_data['bpm']['index'][20]]},
            prefix + '03C2-A' : {'bpm' : [family_data['bpm']['index'][21]]},
            prefix + '03C2-B' : {'bpm' : [family_data['bpm']['index'][22]]},
            prefix + '03C4'   : {'bpm' : [family_data['bpm']['index'][23]]},
            prefix + '03C5-A' : {'bpm' : [family_data['bpm']['index'][24]]},
            prefix + '03C5-B' : {'bpm' : [family_data['bpm']['index'][25]]},

            #Sector 04
            prefix + '04M1'   : {'bpm' : [family_data['bpm']['index'][26]]},
            prefix + '04M2'   : {'bpm' : [family_data['bpm']['index'][27]]},
            prefix + '04C1-A' : {'bpm' : [family_data['bpm']['index'][28]]},
            prefix + '04C1-B' : {'bpm' : [family_data['bpm']['index'][29]]},
            prefix + '04C2-A' : {'bpm' : [family_data['bpm']['index'][30]]},
            prefix + '04C2-B' : {'bpm' : [family_data['bpm']['index'][31]]},
            prefix + '04C4'   : {'bpm' : [family_data['bpm']['index'][32]]},
            prefix + '04C5-A' : {'bpm' : [family_data['bpm']['index'][33]]},
            prefix + '04C5-B' : {'bpm' : [family_data['bpm']['index'][34]]},

            #Sector 05
            prefix + '05M1'   : {'bpm' : [family_data['bpm']['index'][35]]},
            prefix + '05M2'   : {'bpm' : [family_data['bpm']['index'][36]]},
            prefix + '05C1-A' : {'bpm' : [family_data['bpm']['index'][37]]},
            prefix + '05C1-B' : {'bpm' : [family_data['bpm']['index'][38]]},
            prefix + '05C2-A' : {'bpm' : [family_data['bpm']['index'][39]]},
            prefix + '05C2-B' : {'bpm' : [family_data['bpm']['index'][40]]},
            prefix + '05C4'   : {'bpm' : [family_data['bpm']['index'][41]]},
            prefix + '05C5-A' : {'bpm' : [family_data['bpm']['index'][42]]},
            prefix + '05C5-B' : {'bpm' : [family_data['bpm']['index'][43]]},

            #Sector 06
            prefix + '06M1'   : {'bpm' : [family_data['bpm']['index'][44]]},
            prefix + '06M2'   : {'bpm' : [family_data['bpm']['index'][45]]},
            prefix + '06C1-A' : {'bpm' : [family_data['bpm']['index'][46]]},
            prefix + '06C1-B' : {'bpm' : [family_data['bpm']['index'][47]]},
            prefix + '06C2-A' : {'bpm' : [family_data['bpm']['index'][48]]},
            prefix + '06C2-B' : {'bpm' : [family_data['bpm']['index'][49]]},
            prefix + '06C4'   : {'bpm' : [family_data['bpm']['index'][50]]},
            prefix + '06C5-A' : {'bpm' : [family_data['bpm']['index'][51]]},
            prefix + '06C5-B' : {'bpm' : [family_data['bpm']['index'][52]]},

            #Sector 07
            prefix + '07M1'   : {'bpm' : [family_data['bpm']['index'][53]]},
            prefix + '07M2'   : {'bpm' : [family_data['bpm']['index'][54]]},
            prefix + '07C1-A' : {'bpm' : [family_data['bpm']['index'][55]]},
            prefix + '07C1-B' : {'bpm' : [family_data['bpm']['index'][56]]},
            prefix + '07C2-A' : {'bpm' : [family_data['bpm']['index'][57]]},
            prefix + '07C2-B' : {'bpm' : [family_data['bpm']['index'][58]]},
            prefix + '07C4'   : {'bpm' : [family_data['bpm']['index'][59]]},
            prefix + '07C5-A' : {'bpm' : [family_data['bpm']['index'][60]]},
            prefix + '07C5-B' : {'bpm' : [family_data['bpm']['index'][61]]},

            #Sector 08
            prefix + '08M1'   : {'bpm' : [family_data['bpm']['index'][62]]},
            prefix + '08M2'   : {'bpm' : [family_data['bpm']['index'][63]]},
            prefix + '08C1-A' : {'bpm' : [family_data['bpm']['index'][64]]},
            prefix + '08C1-B' : {'bpm' : [family_data['bpm']['index'][65]]},
            prefix + '08C2-A' : {'bpm' : [family_data['bpm']['index'][66]]},
            prefix + '08C2-B' : {'bpm' : [family_data['bpm']['index'][67]]},
            prefix + '08C4'   : {'bpm' : [family_data['bpm']['index'][68]]},
            prefix + '08C5-A' : {'bpm' : [family_data['bpm']['index'][69]]},
            prefix + '08C5-B' : {'bpm' : [family_data['bpm']['index'][70]]},

            #Sector 09
            prefix + '09M1'   : {'bpm' : [family_data['bpm']['index'][71]]},
            prefix + '09M2'   : {'bpm' : [family_data['bpm']['index'][72]]},
            prefix + '09C1-A' : {'bpm' : [family_data['bpm']['index'][73]]},
            prefix + '09C1-B' : {'bpm' : [family_data['bpm']['index'][74]]},
            prefix + '09C2-A' : {'bpm' : [family_data['bpm']['index'][75]]},
            prefix + '09C2-B' : {'bpm' : [family_data['bpm']['index'][76]]},
            prefix + '09C4'   : {'bpm' : [family_data['bpm']['index'][77]]},
            prefix + '09C5-A' : {'bpm' : [family_data['bpm']['index'][78]]},
            prefix + '09C5-B' : {'bpm' : [family_data['bpm']['index'][79]]},

            #Sector 10
            prefix + '10M1'   : {'bpm' : [family_data['bpm']['index'][80]]},
            prefix + '10M2'   : {'bpm' : [family_data['bpm']['index'][81]]},
            prefix + '10C1-A' : {'bpm' : [family_data['bpm']['index'][82]]},
            prefix + '10C1-B' : {'bpm' : [family_data['bpm']['index'][83]]},
            prefix + '10C2-A' : {'bpm' : [family_data['bpm']['index'][84]]},
            prefix + '10C2-B' : {'bpm' : [family_data['bpm']['index'][85]]},
            prefix + '10C4'   : {'bpm' : [family_data['bpm']['index'][86]]},
            prefix + '10C5-A' : {'bpm' : [family_data['bpm']['index'][87]]},
            prefix + '10C5-B' : {'bpm' : [family_data['bpm']['index'][88]]},

            #Sector 11
            prefix + '11M1'   : {'bpm' : [family_data['bpm']['index'][89]]},
            prefix + '11M2'   : {'bpm' : [family_data['bpm']['index'][90]]},
            prefix + '11C1-A' : {'bpm' : [family_data['bpm']['index'][91]]},
            prefix + '11C1-B' : {'bpm' : [family_data['bpm']['index'][92]]},
            prefix + '11C2-A' : {'bpm' : [family_data['bpm']['index'][93]]},
            prefix + '11C2-B' : {'bpm' : [family_data['bpm']['index'][94]]},
            prefix + '11C4'   : {'bpm' : [family_data['bpm']['index'][95]]},
            prefix + '11C5-A' : {'bpm' : [family_data['bpm']['index'][96]]},
            prefix + '11C5-B' : {'bpm' : [family_data['bpm']['index'][97]]},

            #Sector 12
            prefix + '12M1'   : {'bpm' : [family_data['bpm']['index'][98]]},
            prefix + '12M2'   : {'bpm' : [family_data['bpm']['index'][99]]},
            prefix + '12C1-A' : {'bpm' : [family_data['bpm']['index'][100]]},
            prefix + '12C1-B' : {'bpm' : [family_data['bpm']['index'][101]]},
            prefix + '12C2-A' : {'bpm' : [family_data['bpm']['index'][102]]},
            prefix + '12C2-B' : {'bpm' : [family_data['bpm']['index'][103]]},
            prefix + '12C4'   : {'bpm' : [family_data['bpm']['index'][104]]},
            prefix + '12C5-A' : {'bpm' : [family_data['bpm']['index'][105]]},
            prefix + '12C5-B' : {'bpm' : [family_data['bpm']['index'][106]]},

            #Sector 13
            prefix + '13M1'   : {'bpm' : [family_data['bpm']['index'][107]]},
            prefix + '13M2'   : {'bpm' : [family_data['bpm']['index'][108]]},
            prefix + '13C1-A' : {'bpm' : [family_data['bpm']['index'][109]]},
            prefix + '13C1-B' : {'bpm' : [family_data['bpm']['index'][110]]},
            prefix + '13C2-A' : {'bpm' : [family_data['bpm']['index'][111]]},
            prefix + '13C2-B' : {'bpm' : [family_data['bpm']['index'][112]]},
            prefix + '13C4'   : {'bpm' : [family_data['bpm']['index'][113]]},
            prefix + '13C5-A' : {'bpm' : [family_data['bpm']['index'][114]]},
            prefix + '13C5-B' : {'bpm' : [family_data['bpm']['index'][115]]},

            #Sector 14
            prefix + '14M1'   : {'bpm' : [family_data['bpm']['index'][116]]},
            prefix + '14M2'   : {'bpm' : [family_data['bpm']['index'][117]]},
            prefix + '14C1-A' : {'bpm' : [family_data['bpm']['index'][118]]},
            prefix + '14C1-B' : {'bpm' : [family_data['bpm']['index'][119]]},
            prefix + '14C2-A' : {'bpm' : [family_data['bpm']['index'][120]]},
            prefix + '14C2-B' : {'bpm' : [family_data['bpm']['index'][121]]},
            prefix + '14C4'   : {'bpm' : [family_data['bpm']['index'][122]]},
            prefix + '14C5-A' : {'bpm' : [family_data['bpm']['index'][123]]},
            prefix + '14C5-B' : {'bpm' : [family_data['bpm']['index'][124]]},

            #Sector 15
            prefix + '15M1'   : {'bpm' : [family_data['bpm']['index'][125]]},
            prefix + '15M2'   : {'bpm' : [family_data['bpm']['index'][126]]},
            prefix + '15C1-A' : {'bpm' : [family_data['bpm']['index'][127]]},
            prefix + '15C1-B' : {'bpm' : [family_data['bpm']['index'][128]]},
            prefix + '15C2-A' : {'bpm' : [family_data['bpm']['index'][129]]},
            prefix + '15C2-B' : {'bpm' : [family_data['bpm']['index'][130]]},
            prefix + '15C4'   : {'bpm' : [family_data['bpm']['index'][131]]},
            prefix + '15C5-A' : {'bpm' : [family_data['bpm']['index'][132]]},
            prefix + '15C5-B' : {'bpm' : [family_data['bpm']['index'][133]]},

            #Sector 16
            prefix + '16M1'   : {'bpm' : [family_data['bpm']['index'][134]]},
            prefix + '16M2'   : {'bpm' : [family_data['bpm']['index'][135]]},
            prefix + '16C1-A' : {'bpm' : [family_data['bpm']['index'][136]]},
            prefix + '16C1-B' : {'bpm' : [family_data['bpm']['index'][137]]},
            prefix + '16C2-A' : {'bpm' : [family_data['bpm']['index'][138]]},
            prefix + '16C2-B' : {'bpm' : [family_data['bpm']['index'][139]]},
            prefix + '16C4'   : {'bpm' : [family_data['bpm']['index'][140]]},
            prefix + '16C5-A' : {'bpm' : [family_data['bpm']['index'][141]]},
            prefix + '16C5-B' : {'bpm' : [family_data['bpm']['index'][142]]},

            #Sector 17
            prefix + '17M1'   : {'bpm' : [family_data['bpm']['index'][143]]},
            prefix + '17M2'   : {'bpm' : [family_data['bpm']['index'][144]]},
            prefix + '17C1-A' : {'bpm' : [family_data['bpm']['index'][145]]},
            prefix + '17C1-B' : {'bpm' : [family_data['bpm']['index'][146]]},
            prefix + '17C2-A' : {'bpm' : [family_data['bpm']['index'][147]]},
            prefix + '17C2-B' : {'bpm' : [family_data['bpm']['index'][148]]},
            prefix + '17C4'   : {'bpm' : [family_data['bpm']['index'][149]]},
            prefix + '17C5-A' : {'bpm' : [family_data['bpm']['index'][150]]},
            prefix + '17C5-B' : {'bpm' : [family_data['bpm']['index'][151]]},

            #Sector 18
            prefix + '18M1'   : {'bpm' : [family_data['bpm']['index'][152]]},
            prefix + '18M2'   : {'bpm' : [family_data['bpm']['index'][153]]},
            prefix + '18C1-A' : {'bpm' : [family_data['bpm']['index'][154]]},
            prefix + '18C1-B' : {'bpm' : [family_data['bpm']['index'][155]]},
            prefix + '18C2-A' : {'bpm' : [family_data['bpm']['index'][156]]},
            prefix + '18C2-B' : {'bpm' : [family_data['bpm']['index'][157]]},
            prefix + '18C4'   : {'bpm' : [family_data['bpm']['index'][158]]},
            prefix + '18C5-A' : {'bpm' : [family_data['bpm']['index'][159]]},
            prefix + '18C5-B' : {'bpm' : [family_data['bpm']['index'][160]]},

            #Sector 19
            prefix + '19M1'   : {'bpm' : [family_data['bpm']['index'][161]]},
            prefix + '19M2'   : {'bpm' : [family_data['bpm']['index'][162]]},
            prefix + '19C1-A' : {'bpm' : [family_data['bpm']['index'][163]]},
            prefix + '19C1-B' : {'bpm' : [family_data['bpm']['index'][164]]},
            prefix + '19C2-A' : {'bpm' : [family_data['bpm']['index'][165]]},
            prefix + '19C2-B' : {'bpm' : [family_data['bpm']['index'][166]]},
            prefix + '19C4'   : {'bpm' : [family_data['bpm']['index'][167]]},
            prefix + '19C5-A' : {'bpm' : [family_data['bpm']['index'][168]]},
            prefix + '19C5-B' : {'bpm' : [family_data['bpm']['index'][169]]},

            #Sector 20
            prefix + '20M1'   : {'bpm' : [family_data['bpm']['index'][170]]},
            prefix + '20M2'   : {'bpm' : [family_data['bpm']['index'][171]]},
            prefix + '20C1-A' : {'bpm' : [family_data['bpm']['index'][172]]},
            prefix + '20C1-B' : {'bpm' : [family_data['bpm']['index'][173]]},
            prefix + '20C2-A' : {'bpm' : [family_data['bpm']['index'][174]]},
            prefix + '20C2-B' : {'bpm' : [family_data['bpm']['index'][175]]},
            prefix + '20C4'   : {'bpm' : [family_data['bpm']['index'][176]]},
            prefix + '20C5-A' : {'bpm' : [family_data['bpm']['index'][177]]},
            prefix + '20C5-B' : {'bpm' : [family_data['bpm']['index'][178]]},

        }
        return bpm_dict

    if family_name.lower() == 'bend-fam':
        bend_dict = { 'SIPS-BEND-FAM' :
            {'b1' : family_data['b1']['index'],
             'b2' : family_data['b2']['index'],
             'b3' : family_data['b3']['index'],
             'bc' : family_data['bc']['index'],
            }
        }
        return bend_dict

    if family_name.lower() == 'chs':
        prefix = 'SIPS-CHS-'
        chs_dict = {
            #Sector 1
            prefix + '01M1'   : {'chs' : [family_data['chs']['index'][159]]},
            prefix + '01M2'   : {'chs' : [family_data['chs']['index'][0]]},
            prefix + '01C1-A' : {'chs' : [family_data['chs']['index'][1]]},
            prefix + '01C1-B' : {'chs' : [family_data['chs']['index'][2]]},
            prefix + '01C2'   : {'chs' : [family_data['chs']['index'][3]]},
            prefix + '01C4'   : {'chs' : [family_data['chs']['index'][4]]},
            prefix + '01C5-A' : {'chs' : [family_data['chs']['index'][5]]},
            prefix + '01C5-B' : {'chs' : [family_data['chs']['index'][6]]},

            #Sector 2
            prefix + '02M1'   : {'chs' : [family_data['chs']['index'][7]]},
            prefix + '02M2'   : {'chs' : [family_data['chs']['index'][8]]},
            prefix + '02C1-A' : {'chs' : [family_data['chs']['index'][9]]},
            prefix + '02C1-B' : {'chs' : [family_data['chs']['index'][10]]},
            prefix + '02C2'   : {'chs' : [family_data['chs']['index'][11]]},
            prefix + '02C4'   : {'chs' : [family_data['chs']['index'][12]]},
            prefix + '02C5-A' : {'chs' : [family_data['chs']['index'][13]]},
            prefix + '02C5-B' : {'chs' : [family_data['chs']['index'][14]]},

            #Sector 3
            prefix + '03M1'   : {'chs' : [family_data['chs']['index'][15]]},
            prefix + '03M2'   : {'chs' : [family_data['chs']['index'][16]]},
            prefix + '03C1-A' : {'chs' : [family_data['chs']['index'][17]]},
            prefix + '03C1-B' : {'chs' : [family_data['chs']['index'][18]]},
            prefix + '03C2'   : {'chs' : [family_data['chs']['index'][19]]},
            prefix + '03C4'   : {'chs' : [family_data['chs']['index'][20]]},
            prefix + '03C5-A' : {'chs' : [family_data['chs']['index'][21]]},
            prefix + '03C5-B' : {'chs' : [family_data['chs']['index'][22]]},

            #Sector 4
            prefix + '04M1'   : {'chs' : [family_data['chs']['index'][23]]},
            prefix + '04M2'   : {'chs' : [family_data['chs']['index'][24]]},
            prefix + '04C1-A' : {'chs' : [family_data['chs']['index'][25]]},
            prefix + '04C1-B' : {'chs' : [family_data['chs']['index'][26]]},
            prefix + '04C2'   : {'chs' : [family_data['chs']['index'][27]]},
            prefix + '04C4'   : {'chs' : [family_data['chs']['index'][28]]},
            prefix + '04C5-A' : {'chs' : [family_data['chs']['index'][29]]},
            prefix + '04C5-B' : {'chs' : [family_data['chs']['index'][30]]},

            #Sector 5
            prefix + '05M1'   : {'chs' : [family_data['chs']['index'][31]]},
            prefix + '05M2'   : {'chs' : [family_data['chs']['index'][32]]},
            prefix + '05C1-A' : {'chs' : [family_data['chs']['index'][33]]},
            prefix + '05C1-B' : {'chs' : [family_data['chs']['index'][34]]},
            prefix + '05C2'   : {'chs' : [family_data['chs']['index'][35]]},
            prefix + '05C4'   : {'chs' : [family_data['chs']['index'][36]]},
            prefix + '05C5-A' : {'chs' : [family_data['chs']['index'][37]]},
            prefix + '05C5-B' : {'chs' : [family_data['chs']['index'][38]]},

            #Sector 6
            prefix + '06M1'   : {'chs' : [family_data['chs']['index'][39]]},
            prefix + '06M2'   : {'chs' : [family_data['chs']['index'][40]]},
            prefix + '06C1-A' : {'chs' : [family_data['chs']['index'][41]]},
            prefix + '06C1-B' : {'chs' : [family_data['chs']['index'][42]]},
            prefix + '06C2'   : {'chs' : [family_data['chs']['index'][43]]},
            prefix + '06C4'   : {'chs' : [family_data['chs']['index'][44]]},
            prefix + '06C5-A' : {'chs' : [family_data['chs']['index'][45]]},
            prefix + '06C5-B' : {'chs' : [family_data['chs']['index'][46]]},

            #Sector 7
            prefix + '07M1'   : {'chs' : [family_data['chs']['index'][47]]},
            prefix + '07M2'   : {'chs' : [family_data['chs']['index'][48]]},
            prefix + '07C1-A' : {'chs' : [family_data['chs']['index'][49]]},
            prefix + '07C1-B' : {'chs' : [family_data['chs']['index'][50]]},
            prefix + '07C2'   : {'chs' : [family_data['chs']['index'][51]]},
            prefix + '07C4'   : {'chs' : [family_data['chs']['index'][52]]},
            prefix + '07C5-A' : {'chs' : [family_data['chs']['index'][53]]},
            prefix + '07C5-B' : {'chs' : [family_data['chs']['index'][54]]},

            #Sector 8
            prefix + '08M1'   : {'chs' : [family_data['chs']['index'][55]]},
            prefix + '08M2'   : {'chs' : [family_data['chs']['index'][56]]},
            prefix + '08C1-A' : {'chs' : [family_data['chs']['index'][57]]},
            prefix + '08C1-B' : {'chs' : [family_data['chs']['index'][58]]},
            prefix + '08C2'   : {'chs' : [family_data['chs']['index'][59]]},
            prefix + '08C4'   : {'chs' : [family_data['chs']['index'][60]]},
            prefix + '08C5-A' : {'chs' : [family_data['chs']['index'][61]]},
            prefix + '08C5-B' : {'chs' : [family_data['chs']['index'][62]]},

            #Sector 9
            prefix + '09M1'   : {'chs' : [family_data['chs']['index'][63]]},
            prefix + '09M2'   : {'chs' : [family_data['chs']['index'][64]]},
            prefix + '09C1-A' : {'chs' : [family_data['chs']['index'][65]]},
            prefix + '09C1-B' : {'chs' : [family_data['chs']['index'][66]]},
            prefix + '09C2'   : {'chs' : [family_data['chs']['index'][67]]},
            prefix + '09C4'   : {'chs' : [family_data['chs']['index'][68]]},
            prefix + '09C5-A' : {'chs' : [family_data['chs']['index'][69]]},
            prefix + '09C5-B' : {'chs' : [family_data['chs']['index'][70]]},

            #Sector 10
            prefix + '10M1'   : {'chs' : [family_data['chs']['index'][71]]},
            prefix + '10M2'   : {'chs' : [family_data['chs']['index'][72]]},
            prefix + '10C1-A' : {'chs' : [family_data['chs']['index'][73]]},
            prefix + '10C1-B' : {'chs' : [family_data['chs']['index'][74]]},
            prefix + '10C2'   : {'chs' : [family_data['chs']['index'][75]]},
            prefix + '10C4'   : {'chs' : [family_data['chs']['index'][76]]},
            prefix + '10C5-A' : {'chs' : [family_data['chs']['index'][77]]},
            prefix + '10C5-B' : {'chs' : [family_data['chs']['index'][78]]},

            #Sector 11
            prefix + '11M1'   : {'chs' : [family_data['chs']['index'][79]]},
            prefix + '11M2'   : {'chs' : [family_data['chs']['index'][80]]},
            prefix + '11C1-A' : {'chs' : [family_data['chs']['index'][81]]},
            prefix + '11C1-B' : {'chs' : [family_data['chs']['index'][82]]},
            prefix + '11C2'   : {'chs' : [family_data['chs']['index'][83]]},
            prefix + '11C4'   : {'chs' : [family_data['chs']['index'][84]]},
            prefix + '11C5-A' : {'chs' : [family_data['chs']['index'][85]]},
            prefix + '11C5-B' : {'chs' : [family_data['chs']['index'][86]]},

            #Sector 12
            prefix + '12M1'   : {'chs' : [family_data['chs']['index'][87]]},
            prefix + '12M2'   : {'chs' : [family_data['chs']['index'][88]]},
            prefix + '12C1-A' : {'chs' : [family_data['chs']['index'][89]]},
            prefix + '12C1-B' : {'chs' : [family_data['chs']['index'][90]]},
            prefix + '12C2'   : {'chs' : [family_data['chs']['index'][91]]},
            prefix + '12C4'   : {'chs' : [family_data['chs']['index'][92]]},
            prefix + '12C5-A' : {'chs' : [family_data['chs']['index'][93]]},
            prefix + '12C5-B' : {'chs' : [family_data['chs']['index'][94]]},

            #Sector 13
            prefix + '13M1'   : {'chs' : [family_data['chs']['index'][95]]},
            prefix + '13M2'   : {'chs' : [family_data['chs']['index'][96]]},
            prefix + '13C1-A' : {'chs' : [family_data['chs']['index'][97]]},
            prefix + '13C1-B' : {'chs' : [family_data['chs']['index'][98]]},
            prefix + '13C2'   : {'chs' : [family_data['chs']['index'][99]]},
            prefix + '13C4'   : {'chs' : [family_data['chs']['index'][100]]},
            prefix + '13C5-A' : {'chs' : [family_data['chs']['index'][101]]},
            prefix + '13C5-B' : {'chs' : [family_data['chs']['index'][102]]},

            #Sector 14
            prefix + '14M1'   : {'chs' : [family_data['chs']['index'][103]]},
            prefix + '14M2'   : {'chs' : [family_data['chs']['index'][104]]},
            prefix + '14C1-A' : {'chs' : [family_data['chs']['index'][105]]},
            prefix + '14C1-B' : {'chs' : [family_data['chs']['index'][106]]},
            prefix + '14C2'   : {'chs' : [family_data['chs']['index'][107]]},
            prefix + '14C4'   : {'chs' : [family_data['chs']['index'][108]]},
            prefix + '14C5-A' : {'chs' : [family_data['chs']['index'][109]]},
            prefix + '14C5-B' : {'chs' : [family_data['chs']['index'][110]]},

            #Sector 15
            prefix + '15M1'   : {'chs' : [family_data['chs']['index'][111]]},
            prefix + '15M2'   : {'chs' : [family_data['chs']['index'][112]]},
            prefix + '15C1-A' : {'chs' : [family_data['chs']['index'][113]]},
            prefix + '15C1-B' : {'chs' : [family_data['chs']['index'][114]]},
            prefix + '15C2'   : {'chs' : [family_data['chs']['index'][115]]},
            prefix + '15C4'   : {'chs' : [family_data['chs']['index'][116]]},
            prefix + '15C5-A' : {'chs' : [family_data['chs']['index'][117]]},
            prefix + '15C5-B' : {'chs' : [family_data['chs']['index'][118]]},

            #Sector 16
            prefix + '16M1'   : {'chs' : [family_data['chs']['index'][119]]},
            prefix + '16M2'   : {'chs' : [family_data['chs']['index'][120]]},
            prefix + '16C1-A' : {'chs' : [family_data['chs']['index'][121]]},
            prefix + '16C1-B' : {'chs' : [family_data['chs']['index'][122]]},
            prefix + '16C2'   : {'chs' : [family_data['chs']['index'][123]]},
            prefix + '16C4'   : {'chs' : [family_data['chs']['index'][124]]},
            prefix + '16C5-A' : {'chs' : [family_data['chs']['index'][125]]},
            prefix + '16C5-B' : {'chs' : [family_data['chs']['index'][126]]},

            #Sector 17
            prefix + '17M1'   : {'chs' : [family_data['chs']['index'][127]]},
            prefix + '17M2'   : {'chs' : [family_data['chs']['index'][128]]},
            prefix + '17C1-A' : {'chs' : [family_data['chs']['index'][129]]},
            prefix + '17C1-B' : {'chs' : [family_data['chs']['index'][130]]},
            prefix + '17C2'   : {'chs' : [family_data['chs']['index'][131]]},
            prefix + '17C4'   : {'chs' : [family_data['chs']['index'][132]]},
            prefix + '17C5-A' : {'chs' : [family_data['chs']['index'][133]]},
            prefix + '17C5-B' : {'chs' : [family_data['chs']['index'][134]]},

            #Sector 18
            prefix + '18M1'   : {'chs' : [family_data['chs']['index'][135]]},
            prefix + '18M2'   : {'chs' : [family_data['chs']['index'][136]]},
            prefix + '18C1-A' : {'chs' : [family_data['chs']['index'][137]]},
            prefix + '18C1-B' : {'chs' : [family_data['chs']['index'][138]]},
            prefix + '18C2'   : {'chs' : [family_data['chs']['index'][139]]},
            prefix + '18C4'   : {'chs' : [family_data['chs']['index'][140]]},
            prefix + '18C5-A' : {'chs' : [family_data['chs']['index'][141]]},
            prefix + '18C5-B' : {'chs' : [family_data['chs']['index'][142]]},

            #Sector 19
            prefix + '19M1'   : {'chs' : [family_data['chs']['index'][143]]},
            prefix + '19M2'   : {'chs' : [family_data['chs']['index'][144]]},
            prefix + '19C1-A' : {'chs' : [family_data['chs']['index'][145]]},
            prefix + '19C1-B' : {'chs' : [family_data['chs']['index'][146]]},
            prefix + '19C2'   : {'chs' : [family_data['chs']['index'][147]]},
            prefix + '19C4'   : {'chs' : [family_data['chs']['index'][148]]},
            prefix + '19C5-A' : {'chs' : [family_data['chs']['index'][149]]},
            prefix + '19C5-B' : {'chs' : [family_data['chs']['index'][150]]},

            #Sector 20
            prefix + '20M1'   : {'chs' : [family_data['chs']['index'][151]]},
            prefix + '20M2'   : {'chs' : [family_data['chs']['index'][152]]},
            prefix + '20C1-A' : {'chs' : [family_data['chs']['index'][153]]},
            prefix + '20C1-B' : {'chs' : [family_data['chs']['index'][154]]},
            prefix + '20C2'   : {'chs' : [family_data['chs']['index'][155]]},
            prefix + '20C4'   : {'chs' : [family_data['chs']['index'][156]]},
            prefix + '20C5-A' : {'chs' : [family_data['chs']['index'][157]]},
            prefix + '20C5-B' : {'chs' : [family_data['chs']['index'][158]]},
        }
        return chs_dict

    if family_name.lower() == 'cvs':
        prefix = 'SIPS-CVS-'
        cvs_dict = {
            #Sector 1
            prefix + '01M1'   : {'cvs' : [family_data['cvs']['index'][119]]},
            prefix + '01M2'   : {'cvs' : [family_data['cvs']['index'][0]]},
            prefix + '01C1'   : {'cvs' : [family_data['cvs']['index'][1]]},
            prefix + '01C2'   : {'cvs' : [family_data['cvs']['index'][2]]},
            prefix + '01C4'   : {'cvs' : [family_data['cvs']['index'][3]]},
            prefix + '01C5'   : {'cvs' : [family_data['cvs']['index'][4]]},

            #Sector 2
            prefix + '02M1'   : {'cvs' : [family_data['cvs']['index'][5]]},
            prefix + '02M2'   : {'cvs' : [family_data['cvs']['index'][6]]},
            prefix + '02C1'   : {'cvs' : [family_data['cvs']['index'][7]]},
            prefix + '02C2'   : {'cvs' : [family_data['cvs']['index'][8]]},
            prefix + '02C4'   : {'cvs' : [family_data['cvs']['index'][9]]},
            prefix + '02C5'   : {'cvs' : [family_data['cvs']['index'][10]]},

            #Sector 3
            prefix + '03M1'   : {'cvs' : [family_data['cvs']['index'][11]]},
            prefix + '03M2'   : {'cvs' : [family_data['cvs']['index'][12]]},
            prefix + '03C1'   : {'cvs' : [family_data['cvs']['index'][13]]},
            prefix + '03C2'   : {'cvs' : [family_data['cvs']['index'][14]]},
            prefix + '03C4'   : {'cvs' : [family_data['cvs']['index'][15]]},
            prefix + '03C5'   : {'cvs' : [family_data['cvs']['index'][16]]},

            #Sector 4
            prefix + '04M1'   : {'cvs' : [family_data['cvs']['index'][17]]},
            prefix + '04M2'   : {'cvs' : [family_data['cvs']['index'][18]]},
            prefix + '04C1'   : {'cvs' : [family_data['cvs']['index'][19]]},
            prefix + '04C2'   : {'cvs' : [family_data['cvs']['index'][20]]},
            prefix + '04C4'   : {'cvs' : [family_data['cvs']['index'][21]]},
            prefix + '04C5'   : {'cvs' : [family_data['cvs']['index'][22]]},

            #Sector 5
            prefix + '05M1'   : {'cvs' : [family_data['cvs']['index'][23]]},
            prefix + '05M2'   : {'cvs' : [family_data['cvs']['index'][24]]},
            prefix + '05C1'   : {'cvs' : [family_data['cvs']['index'][25]]},
            prefix + '05C2'   : {'cvs' : [family_data['cvs']['index'][26]]},
            prefix + '05C4'   : {'cvs' : [family_data['cvs']['index'][27]]},
            prefix + '05C5'   : {'cvs' : [family_data['cvs']['index'][28]]},

            #Sector 6
            prefix + '06M1'   : {'cvs' : [family_data['cvs']['index'][29]]},
            prefix + '06M2'   : {'cvs' : [family_data['cvs']['index'][30]]},
            prefix + '06C1'   : {'cvs' : [family_data['cvs']['index'][31]]},
            prefix + '06C2'   : {'cvs' : [family_data['cvs']['index'][32]]},
            prefix + '06C4'   : {'cvs' : [family_data['cvs']['index'][33]]},
            prefix + '06C5'   : {'cvs' : [family_data['cvs']['index'][34]]},

            #Sector 7
            prefix + '07M1'   : {'cvs' : [family_data['cvs']['index'][35]]},
            prefix + '07M2'   : {'cvs' : [family_data['cvs']['index'][36]]},
            prefix + '07C1'   : {'cvs' : [family_data['cvs']['index'][37]]},
            prefix + '07C2'   : {'cvs' : [family_data['cvs']['index'][38]]},
            prefix + '07C4'   : {'cvs' : [family_data['cvs']['index'][39]]},
            prefix + '07C5'   : {'cvs' : [family_data['cvs']['index'][40]]},

            #Sector 8
            prefix + '08M1'   : {'cvs' : [family_data['cvs']['index'][41]]},
            prefix + '08M2'   : {'cvs' : [family_data['cvs']['index'][42]]},
            prefix + '08C1'   : {'cvs' : [family_data['cvs']['index'][43]]},
            prefix + '08C2'   : {'cvs' : [family_data['cvs']['index'][44]]},
            prefix + '08C4'   : {'cvs' : [family_data['cvs']['index'][45]]},
            prefix + '08C5'   : {'cvs' : [family_data['cvs']['index'][46]]},

            #Sector 9
            prefix + '09M1'   : {'cvs' : [family_data['cvs']['index'][47]]},
            prefix + '09M2'   : {'cvs' : [family_data['cvs']['index'][48]]},
            prefix + '09C1'   : {'cvs' : [family_data['cvs']['index'][49]]},
            prefix + '09C2'   : {'cvs' : [family_data['cvs']['index'][50]]},
            prefix + '09C4'   : {'cvs' : [family_data['cvs']['index'][51]]},
            prefix + '09C5'   : {'cvs' : [family_data['cvs']['index'][52]]},

            #Sector 10
            prefix + '10M1'   : {'cvs' : [family_data['cvs']['index'][53]]},
            prefix + '10M2'   : {'cvs' : [family_data['cvs']['index'][54]]},
            prefix + '10C1'   : {'cvs' : [family_data['cvs']['index'][55]]},
            prefix + '10C2'   : {'cvs' : [family_data['cvs']['index'][56]]},
            prefix + '10C4'   : {'cvs' : [family_data['cvs']['index'][57]]},
            prefix + '10C5'   : {'cvs' : [family_data['cvs']['index'][58]]},

            #Sector 11
            prefix + '11M1'   : {'cvs' : [family_data['cvs']['index'][59]]},
            prefix + '11M2'   : {'cvs' : [family_data['cvs']['index'][60]]},
            prefix + '11C1'   : {'cvs' : [family_data['cvs']['index'][61]]},
            prefix + '11C2'   : {'cvs' : [family_data['cvs']['index'][62]]},
            prefix + '11C4'   : {'cvs' : [family_data['cvs']['index'][63]]},
            prefix + '11C5'   : {'cvs' : [family_data['cvs']['index'][64]]},

            #Sector 12
            prefix + '12M1'   : {'cvs' : [family_data['cvs']['index'][65]]},
            prefix + '12M2'   : {'cvs' : [family_data['cvs']['index'][66]]},
            prefix + '12C1'   : {'cvs' : [family_data['cvs']['index'][67]]},
            prefix + '12C2'   : {'cvs' : [family_data['cvs']['index'][68]]},
            prefix + '12C4'   : {'cvs' : [family_data['cvs']['index'][69]]},
            prefix + '12C5'   : {'cvs' : [family_data['cvs']['index'][70]]},

            #Sector 13
            prefix + '13M1'   : {'cvs' : [family_data['cvs']['index'][71]]},
            prefix + '13M2'   : {'cvs' : [family_data['cvs']['index'][72]]},
            prefix + '13C1'   : {'cvs' : [family_data['cvs']['index'][73]]},
            prefix + '13C2'   : {'cvs' : [family_data['cvs']['index'][74]]},
            prefix + '13C4'   : {'cvs' : [family_data['cvs']['index'][75]]},
            prefix + '13C5'   : {'cvs' : [family_data['cvs']['index'][76]]},

            #Sector 14
            prefix + '14M1'   : {'cvs' : [family_data['cvs']['index'][77]]},
            prefix + '14M2'   : {'cvs' : [family_data['cvs']['index'][78]]},
            prefix + '14C1'   : {'cvs' : [family_data['cvs']['index'][79]]},
            prefix + '14C2'   : {'cvs' : [family_data['cvs']['index'][80]]},
            prefix + '14C4'   : {'cvs' : [family_data['cvs']['index'][81]]},
            prefix + '14C5'   : {'cvs' : [family_data['cvs']['index'][82]]},

            #Sector 15
            prefix + '15M1'   : {'cvs' : [family_data['cvs']['index'][83]]},
            prefix + '15M2'   : {'cvs' : [family_data['cvs']['index'][84]]},
            prefix + '15C1'   : {'cvs' : [family_data['cvs']['index'][85]]},
            prefix + '15C2'   : {'cvs' : [family_data['cvs']['index'][86]]},
            prefix + '15C4'   : {'cvs' : [family_data['cvs']['index'][87]]},
            prefix + '15C5'   : {'cvs' : [family_data['cvs']['index'][88]]},

            #Sector 16
            prefix + '16M1'   : {'cvs' : [family_data['cvs']['index'][89]]},
            prefix + '16M2'   : {'cvs' : [family_data['cvs']['index'][90]]},
            prefix + '16C1'   : {'cvs' : [family_data['cvs']['index'][91]]},
            prefix + '16C2'   : {'cvs' : [family_data['cvs']['index'][92]]},
            prefix + '16C4'   : {'cvs' : [family_data['cvs']['index'][93]]},
            prefix + '16C5'   : {'cvs' : [family_data['cvs']['index'][94]]},

            #Sector 17
            prefix + '17M1'   : {'cvs' : [family_data['cvs']['index'][95]]},
            prefix + '17M2'   : {'cvs' : [family_data['cvs']['index'][96]]},
            prefix + '17C1'   : {'cvs' : [family_data['cvs']['index'][97]]},
            prefix + '17C2'   : {'cvs' : [family_data['cvs']['index'][98]]},
            prefix + '17C4'   : {'cvs' : [family_data['cvs']['index'][99]]},
            prefix + '17C5'   : {'cvs' : [family_data['cvs']['index'][100]]},

            #Sector 18
            prefix + '18M1'   : {'cvs' : [family_data['cvs']['index'][101]]},
            prefix + '18M2'   : {'cvs' : [family_data['cvs']['index'][102]]},
            prefix + '18C1'   : {'cvs' : [family_data['cvs']['index'][103]]},
            prefix + '18C2'   : {'cvs' : [family_data['cvs']['index'][104]]},
            prefix + '18C4'   : {'cvs' : [family_data['cvs']['index'][105]]},
            prefix + '18C5'   : {'cvs' : [family_data['cvs']['index'][106]]},

            #Sector 19
            prefix + '19M1'   : {'cvs' : [family_data['cvs']['index'][107]]},
            prefix + '19M2'   : {'cvs' : [family_data['cvs']['index'][108]]},
            prefix + '19C1'   : {'cvs' : [family_data['cvs']['index'][109]]},
            prefix + '19C2'   : {'cvs' : [family_data['cvs']['index'][110]]},
            prefix + '19C4'   : {'cvs' : [family_data['cvs']['index'][111]]},
            prefix + '19C5'   : {'cvs' : [family_data['cvs']['index'][112]]},

            #Sector 20
            prefix + '20M1'   : {'cvs' : [family_data['cvs']['index'][113]]},
            prefix + '20M2'   : {'cvs' : [family_data['cvs']['index'][114]]},
            prefix + '20C1'   : {'cvs' : [family_data['cvs']['index'][115]]},
            prefix + '20C2'   : {'cvs' : [family_data['cvs']['index'][116]]},
            prefix + '20C4'   : {'cvs' : [family_data['cvs']['index'][117]]},
            prefix + '20C5'   : {'cvs' : [family_data['cvs']['index'][118]]},
        }
        return cvs_dict

    if family_name.lower() == 'chf':
        prefix = 'SIPS-CHF-'
        chf_dict = {
            #Sector 1
            prefix + '01M1'   : {'chf' : [family_data['chf']['index'][79]]},
            prefix + '01M2'   : {'chf' : [family_data['chf']['index'][0]]},
            prefix + '01C2'   : {'chf' : [family_data['chf']['index'][1]]},
            prefix + '01C4'   : {'chf' : [family_data['chf']['index'][2]]},

            #Sector 2
            prefix + '02M1'   : {'chf' : [family_data['chf']['index'][3]]},
            prefix + '02M2'   : {'chf' : [family_data['chf']['index'][4]]},
            prefix + '02C2'   : {'chf' : [family_data['chf']['index'][5]]},
            prefix + '02C4'   : {'chf' : [family_data['chf']['index'][6]]},

            #Sector 3
            prefix + '03M1'   : {'chf' : [family_data['chf']['index'][7]]},
            prefix + '03M2'   : {'chf' : [family_data['chf']['index'][8]]},
            prefix + '03C2'   : {'chf' : [family_data['chf']['index'][9]]},
            prefix + '03C4'   : {'chf' : [family_data['chf']['index'][10]]},

            #Sector 4
            prefix + '04M1'   : {'chf' : [family_data['chf']['index'][11]]},
            prefix + '04M2'   : {'chf' : [family_data['chf']['index'][12]]},
            prefix + '04C2'   : {'chf' : [family_data['chf']['index'][13]]},
            prefix + '04C4'   : {'chf' : [family_data['chf']['index'][14]]},

            #Sector 5
            prefix + '05M1'   : {'chf' : [family_data['chf']['index'][15]]},
            prefix + '05M2'   : {'chf' : [family_data['chf']['index'][16]]},
            prefix + '05C2'   : {'chf' : [family_data['chf']['index'][17]]},
            prefix + '05C4'   : {'chf' : [family_data['chf']['index'][18]]},

            #Sector 6
            prefix + '06M1'   : {'chf' : [family_data['chf']['index'][19]]},
            prefix + '06M2'   : {'chf' : [family_data['chf']['index'][20]]},
            prefix + '06C2'   : {'chf' : [family_data['chf']['index'][21]]},
            prefix + '06C4'   : {'chf' : [family_data['chf']['index'][22]]},

            #Sector 7
            prefix + '07M1'   : {'chf' : [family_data['chf']['index'][23]]},
            prefix + '07M2'   : {'chf' : [family_data['chf']['index'][24]]},
            prefix + '07C2'   : {'chf' : [family_data['chf']['index'][25]]},
            prefix + '07C4'   : {'chf' : [family_data['chf']['index'][26]]},

            #Sector 8
            prefix + '08M1'   : {'chf' : [family_data['chf']['index'][27]]},
            prefix + '08M2'   : {'chf' : [family_data['chf']['index'][28]]},
            prefix + '08C2'   : {'chf' : [family_data['chf']['index'][29]]},
            prefix + '08C4'   : {'chf' : [family_data['chf']['index'][30]]},

            #Sector 9
            prefix + '09M1'   : {'chf' : [family_data['chf']['index'][31]]},
            prefix + '09M2'   : {'chf' : [family_data['chf']['index'][32]]},
            prefix + '09C2'   : {'chf' : [family_data['chf']['index'][33]]},
            prefix + '09C4'   : {'chf' : [family_data['chf']['index'][34]]},

            #Sector 10
            prefix + '10M1'   : {'chf' : [family_data['chf']['index'][35]]},
            prefix + '10M2'   : {'chf' : [family_data['chf']['index'][36]]},
            prefix + '10C2'   : {'chf' : [family_data['chf']['index'][37]]},
            prefix + '10C4'   : {'chf' : [family_data['chf']['index'][38]]},

            #Sector 11
            prefix + '11M1'   : {'chf' : [family_data['chf']['index'][39]]},
            prefix + '11M2'   : {'chf' : [family_data['chf']['index'][40]]},
            prefix + '11C2'   : {'chf' : [family_data['chf']['index'][41]]},
            prefix + '11C4'   : {'chf' : [family_data['chf']['index'][42]]},

            #Sector 12
            prefix + '12M1'   : {'chf' : [family_data['chf']['index'][43]]},
            prefix + '12M2'   : {'chf' : [family_data['chf']['index'][44]]},
            prefix + '12C2'   : {'chf' : [family_data['chf']['index'][45]]},
            prefix + '12C4'   : {'chf' : [family_data['chf']['index'][46]]},

            #Sector 13
            prefix + '13M1'   : {'chf' : [family_data['chf']['index'][47]]},
            prefix + '13M2'   : {'chf' : [family_data['chf']['index'][48]]},
            prefix + '13C2'   : {'chf' : [family_data['chf']['index'][49]]},
            prefix + '13C4'   : {'chf' : [family_data['chf']['index'][50]]},

            #Sector 14
            prefix + '14M1'   : {'chf' : [family_data['chf']['index'][51]]},
            prefix + '14M2'   : {'chf' : [family_data['chf']['index'][52]]},
            prefix + '14C2'   : {'chf' : [family_data['chf']['index'][53]]},
            prefix + '14C4'   : {'chf' : [family_data['chf']['index'][54]]},

            #Sector 15
            prefix + '15M1'   : {'chf' : [family_data['chf']['index'][55]]},
            prefix + '15M2'   : {'chf' : [family_data['chf']['index'][56]]},
            prefix + '15C2'   : {'chf' : [family_data['chf']['index'][57]]},
            prefix + '15C4'   : {'chf' : [family_data['chf']['index'][58]]},

            #Sector 16
            prefix + '16M1'   : {'chf' : [family_data['chf']['index'][59]]},
            prefix + '16M2'   : {'chf' : [family_data['chf']['index'][60]]},
            prefix + '16C2'   : {'chf' : [family_data['chf']['index'][61]]},
            prefix + '16C4'   : {'chf' : [family_data['chf']['index'][62]]},

            #Sector 17
            prefix + '17M1'   : {'chf' : [family_data['chf']['index'][63]]},
            prefix + '17M2'   : {'chf' : [family_data['chf']['index'][64]]},
            prefix + '17C2'   : {'chf' : [family_data['chf']['index'][65]]},
            prefix + '17C4'   : {'chf' : [family_data['chf']['index'][66]]},

            #Sector 18
            prefix + '18M1'   : {'chf' : [family_data['chf']['index'][67]]},
            prefix + '18M2'   : {'chf' : [family_data['chf']['index'][68]]},
            prefix + '18C2'   : {'chf' : [family_data['chf']['index'][69]]},
            prefix + '18C4'   : {'chf' : [family_data['chf']['index'][70]]},

            #Sector 19
            prefix + '19M1'   : {'chf' : [family_data['chf']['index'][71]]},
            prefix + '19M2'   : {'chf' : [family_data['chf']['index'][72]]},
            prefix + '19C2'   : {'chf' : [family_data['chf']['index'][73]]},
            prefix + '19C4'   : {'chf' : [family_data['chf']['index'][74]]},

            #Sector 20
            prefix + '20M1'   : {'chf' : [family_data['chf']['index'][75]]},
            prefix + '20M2'   : {'chf' : [family_data['chf']['index'][76]]},
            prefix + '20C2'   : {'chf' : [family_data['chf']['index'][77]]},
            prefix + '20C4'   : {'chf' : [family_data['chf']['index'][78]]},
        }
        return chf_dict

    if family_name.lower() == 'cvf':
        prefix = 'SIPS-CVF-'
        cvf_dict = {
            #Sector 1
            prefix + '01M1'   : {'cvf' : [family_data['cvf']['index'][79]]},
            prefix + '01M2'   : {'cvf' : [family_data['cvf']['index'][0]]},
            prefix + '01C2'   : {'cvf' : [family_data['cvf']['index'][1]]},
            prefix + '01C4'   : {'cvf' : [family_data['cvf']['index'][2]]},

            #Sector 2
            prefix + '02M1'   : {'cvf' : [family_data['cvf']['index'][3]]},
            prefix + '02M2'   : {'cvf' : [family_data['cvf']['index'][4]]},
            prefix + '02C2'   : {'cvf' : [family_data['cvf']['index'][5]]},
            prefix + '02C4'   : {'cvf' : [family_data['cvf']['index'][6]]},

            #Sector 3
            prefix + '03M1'   : {'cvf' : [family_data['cvf']['index'][7]]},
            prefix + '03M2'   : {'cvf' : [family_data['cvf']['index'][8]]},
            prefix + '03C2'   : {'cvf' : [family_data['cvf']['index'][9]]},
            prefix + '03C4'   : {'cvf' : [family_data['cvf']['index'][10]]},

            #Sector 4
            prefix + '04M1'   : {'cvf' : [family_data['cvf']['index'][11]]},
            prefix + '04M2'   : {'cvf' : [family_data['cvf']['index'][12]]},
            prefix + '04C2'   : {'cvf' : [family_data['cvf']['index'][13]]},
            prefix + '04C4'   : {'cvf' : [family_data['cvf']['index'][14]]},

            #Sector 5
            prefix + '05M1'   : {'cvf' : [family_data['cvf']['index'][15]]},
            prefix + '05M2'   : {'cvf' : [family_data['cvf']['index'][16]]},
            prefix + '05C2'   : {'cvf' : [family_data['cvf']['index'][17]]},
            prefix + '05C4'   : {'cvf' : [family_data['cvf']['index'][18]]},

            #Sector 6
            prefix + '06M1'   : {'cvf' : [family_data['cvf']['index'][19]]},
            prefix + '06M2'   : {'cvf' : [family_data['cvf']['index'][20]]},
            prefix + '06C2'   : {'cvf' : [family_data['cvf']['index'][21]]},
            prefix + '06C4'   : {'cvf' : [family_data['cvf']['index'][22]]},

            #Sector 7
            prefix + '07M1'   : {'cvf' : [family_data['cvf']['index'][23]]},
            prefix + '07M2'   : {'cvf' : [family_data['cvf']['index'][24]]},
            prefix + '07C2'   : {'cvf' : [family_data['cvf']['index'][25]]},
            prefix + '07C4'   : {'cvf' : [family_data['cvf']['index'][26]]},

            #Sector 8
            prefix + '08M1'   : {'cvf' : [family_data['cvf']['index'][27]]},
            prefix + '08M2'   : {'cvf' : [family_data['cvf']['index'][28]]},
            prefix + '08C2'   : {'cvf' : [family_data['cvf']['index'][29]]},
            prefix + '08C4'   : {'cvf' : [family_data['cvf']['index'][30]]},

            #Sector 9
            prefix + '09M1'   : {'cvf' : [family_data['cvf']['index'][31]]},
            prefix + '09M2'   : {'cvf' : [family_data['cvf']['index'][32]]},
            prefix + '09C2'   : {'cvf' : [family_data['cvf']['index'][33]]},
            prefix + '09C4'   : {'cvf' : [family_data['cvf']['index'][34]]},

            #Sector 10
            prefix + '10M1'   : {'cvf' : [family_data['cvf']['index'][35]]},
            prefix + '10M2'   : {'cvf' : [family_data['cvf']['index'][36]]},
            prefix + '10C2'   : {'cvf' : [family_data['cvf']['index'][37]]},
            prefix + '10C4'   : {'cvf' : [family_data['cvf']['index'][38]]},

            #Sector 11
            prefix + '11M1'   : {'cvf' : [family_data['cvf']['index'][39]]},
            prefix + '11M2'   : {'cvf' : [family_data['cvf']['index'][40]]},
            prefix + '11C2'   : {'cvf' : [family_data['cvf']['index'][41]]},
            prefix + '11C4'   : {'cvf' : [family_data['cvf']['index'][42]]},

            #Sector 12
            prefix + '12M1'   : {'cvf' : [family_data['cvf']['index'][43]]},
            prefix + '12M2'   : {'cvf' : [family_data['cvf']['index'][44]]},
            prefix + '12C2'   : {'cvf' : [family_data['cvf']['index'][45]]},
            prefix + '12C4'   : {'cvf' : [family_data['cvf']['index'][46]]},

            #Sector 13
            prefix + '13M1'   : {'cvf' : [family_data['cvf']['index'][47]]},
            prefix + '13M2'   : {'cvf' : [family_data['cvf']['index'][48]]},
            prefix + '13C2'   : {'cvf' : [family_data['cvf']['index'][49]]},
            prefix + '13C4'   : {'cvf' : [family_data['cvf']['index'][50]]},

            #Sector 14
            prefix + '14M1'   : {'cvf' : [family_data['cvf']['index'][51]]},
            prefix + '14M2'   : {'cvf' : [family_data['cvf']['index'][52]]},
            prefix + '14C2'   : {'cvf' : [family_data['cvf']['index'][53]]},
            prefix + '14C4'   : {'cvf' : [family_data['cvf']['index'][54]]},

            #Sector 15
            prefix + '15M1'   : {'cvf' : [family_data['cvf']['index'][55]]},
            prefix + '15M2'   : {'cvf' : [family_data['cvf']['index'][56]]},
            prefix + '15C2'   : {'cvf' : [family_data['cvf']['index'][57]]},
            prefix + '15C4'   : {'cvf' : [family_data['cvf']['index'][58]]},

            #Sector 16
            prefix + '16M1'   : {'cvf' : [family_data['cvf']['index'][59]]},
            prefix + '16M2'   : {'cvf' : [family_data['cvf']['index'][60]]},
            prefix + '16C2'   : {'cvf' : [family_data['cvf']['index'][61]]},
            prefix + '16C4'   : {'cvf' : [family_data['cvf']['index'][62]]},

            #Sector 17
            prefix + '17M1'   : {'cvf' : [family_data['cvf']['index'][63]]},
            prefix + '17M2'   : {'cvf' : [family_data['cvf']['index'][64]]},
            prefix + '17C2'   : {'cvf' : [family_data['cvf']['index'][65]]},
            prefix + '17C4'   : {'cvf' : [family_data['cvf']['index'][66]]},

            #Sector 18
            prefix + '18M1'   : {'cvf' : [family_data['cvf']['index'][67]]},
            prefix + '18M2'   : {'cvf' : [family_data['cvf']['index'][68]]},
            prefix + '18C2'   : {'cvf' : [family_data['cvf']['index'][69]]},
            prefix + '18C4'   : {'cvf' : [family_data['cvf']['index'][70]]},

            #Sector 19
            prefix + '19M1'   : {'cvf' : [family_data['cvf']['index'][71]]},
            prefix + '19M2'   : {'cvf' : [family_data['cvf']['index'][72]]},
            prefix + '19C2'   : {'cvf' : [family_data['cvf']['index'][73]]},
            prefix + '19C4'   : {'cvf' : [family_data['cvf']['index'][74]]},

            #Sector 20
            prefix + '20M1'   : {'cvf' : [family_data['cvf']['index'][75]]},
            prefix + '20M2'   : {'cvf' : [family_data['cvf']['index'][76]]},
            prefix + '20C2'   : {'cvf' : [family_data['cvf']['index'][77]]},
            prefix + '20C4'   : {'cvf' : [family_data['cvf']['index'][78]]},
        }
        return cvf_dict

    if family_name.lower() == 'qs':
        prefix = 'SIPS-QS-'
        qs_dict = {
            #Sector 1
            prefix + '01M1'   : {'qs' : [family_data['qs']['index'][79]]},
            prefix + '01M2'   : {'qs' : [family_data['qs']['index'][0]]},
            prefix + '01C1'   : {'qs' : [family_data['qs']['index'][1]]},
            prefix + '01C5'   : {'qs' : [family_data['qs']['index'][2]]},

            #Sector 2
            prefix + '02M1'   : {'qs' : [family_data['qs']['index'][3]]},
            prefix + '02M2'   : {'qs' : [family_data['qs']['index'][4]]},
            prefix + '02C1'   : {'qs' : [family_data['qs']['index'][5]]},
            prefix + '02C5'   : {'qs' : [family_data['qs']['index'][6]]},

            #Sector 3
            prefix + '03M1'   : {'qs' : [family_data['qs']['index'][7]]},
            prefix + '03M2'   : {'qs' : [family_data['qs']['index'][8]]},
            prefix + '03C1'   : {'qs' : [family_data['qs']['index'][9]]},
            prefix + '03C5'   : {'qs' : [family_data['qs']['index'][10]]},

            #Sector 4
            prefix + '04M1'   : {'qs' : [family_data['qs']['index'][11]]},
            prefix + '04M2'   : {'qs' : [family_data['qs']['index'][12]]},
            prefix + '04C1'   : {'qs' : [family_data['qs']['index'][13]]},
            prefix + '04C5'   : {'qs' : [family_data['qs']['index'][14]]},

            #Sector 5
            prefix + '05M1'   : {'qs' : [family_data['qs']['index'][15]]},
            prefix + '05M2'   : {'qs' : [family_data['qs']['index'][16]]},
            prefix + '05C1'   : {'qs' : [family_data['qs']['index'][17]]},
            prefix + '05C5'   : {'qs' : [family_data['qs']['index'][18]]},

            #Sector 6
            prefix + '06M1'   : {'qs' : [family_data['qs']['index'][19]]},
            prefix + '06M2'   : {'qs' : [family_data['qs']['index'][20]]},
            prefix + '06C1'   : {'qs' : [family_data['qs']['index'][21]]},
            prefix + '06C5'   : {'qs' : [family_data['qs']['index'][22]]},

            #Sector 7
            prefix + '07M1'   : {'qs' : [family_data['qs']['index'][23]]},
            prefix + '07M2'   : {'qs' : [family_data['qs']['index'][24]]},
            prefix + '07C1'   : {'qs' : [family_data['qs']['index'][25]]},
            prefix + '07C5'   : {'qs' : [family_data['qs']['index'][26]]},

            #Sector 8
            prefix + '08M1'   : {'qs' : [family_data['qs']['index'][27]]},
            prefix + '08M2'   : {'qs' : [family_data['qs']['index'][28]]},
            prefix + '08C1'   : {'qs' : [family_data['qs']['index'][29]]},
            prefix + '08C5'   : {'qs' : [family_data['qs']['index'][30]]},

            #Sector 9
            prefix + '09M1'   : {'qs' : [family_data['qs']['index'][31]]},
            prefix + '09M2'   : {'qs' : [family_data['qs']['index'][32]]},
            prefix + '09C1'   : {'qs' : [family_data['qs']['index'][33]]},
            prefix + '09C5'   : {'qs' : [family_data['qs']['index'][34]]},

            #Sector 10
            prefix + '10M1'   : {'qs' : [family_data['qs']['index'][35]]},
            prefix + '10M2'   : {'qs' : [family_data['qs']['index'][36]]},
            prefix + '10C1'   : {'qs' : [family_data['qs']['index'][37]]},
            prefix + '10C5'   : {'qs' : [family_data['qs']['index'][38]]},

            #Sector 11
            prefix + '11M1'   : {'qs' : [family_data['qs']['index'][39]]},
            prefix + '11M2'   : {'qs' : [family_data['qs']['index'][40]]},
            prefix + '11C1'   : {'qs' : [family_data['qs']['index'][41]]},
            prefix + '11C5'   : {'qs' : [family_data['qs']['index'][42]]},

            #Sector 12
            prefix + '12M1'   : {'qs' : [family_data['qs']['index'][43]]},
            prefix + '12M2'   : {'qs' : [family_data['qs']['index'][44]]},
            prefix + '12C1'   : {'qs' : [family_data['qs']['index'][45]]},
            prefix + '12C5'   : {'qs' : [family_data['qs']['index'][46]]},

            #Sector 13
            prefix + '13M1'   : {'qs' : [family_data['qs']['index'][47]]},
            prefix + '13M2'   : {'qs' : [family_data['qs']['index'][48]]},
            prefix + '13C1'   : {'qs' : [family_data['qs']['index'][49]]},
            prefix + '13C5'   : {'qs' : [family_data['qs']['index'][50]]},

            #Sector 14
            prefix + '14M1'   : {'qs' : [family_data['qs']['index'][51]]},
            prefix + '14M2'   : {'qs' : [family_data['qs']['index'][52]]},
            prefix + '14C1'   : {'qs' : [family_data['qs']['index'][53]]},
            prefix + '14C5'   : {'qs' : [family_data['qs']['index'][54]]},

            #Sector 15
            prefix + '15M1'   : {'qs' : [family_data['qs']['index'][55]]},
            prefix + '15M2'   : {'qs' : [family_data['qs']['index'][56]]},
            prefix + '15C1'   : {'qs' : [family_data['qs']['index'][57]]},
            prefix + '15C5'   : {'qs' : [family_data['qs']['index'][58]]},

            #Sector 16
            prefix + '16M1'   : {'qs' : [family_data['qs']['index'][59]]},
            prefix + '16M2'   : {'qs' : [family_data['qs']['index'][60]]},
            prefix + '16C1'   : {'qs' : [family_data['qs']['index'][61]]},
            prefix + '16C5'   : {'qs' : [family_data['qs']['index'][62]]},

            #Sector 17
            prefix + '17M1'   : {'qs' : [family_data['qs']['index'][63]]},
            prefix + '17M2'   : {'qs' : [family_data['qs']['index'][64]]},
            prefix + '17C1'   : {'qs' : [family_data['qs']['index'][65]]},
            prefix + '17C5'   : {'qs' : [family_data['qs']['index'][66]]},

            #Sector 18
            prefix + '18M1'   : {'qs' : [family_data['qs']['index'][67]]},
            prefix + '18M2'   : {'qs' : [family_data['qs']['index'][68]]},
            prefix + '18C1'   : {'qs' : [family_data['qs']['index'][69]]},
            prefix + '18C5'   : {'qs' : [family_data['qs']['index'][70]]},

            #Sector 19
            prefix + '19M1'   : {'qs' : [family_data['qs']['index'][71]]},
            prefix + '19M2'   : {'qs' : [family_data['qs']['index'][72]]},
            prefix + '19C1'   : {'qs' : [family_data['qs']['index'][73]]},
            prefix + '19C5'   : {'qs' : [family_data['qs']['index'][74]]},

            #Sector 20
            prefix + '20M1'   : {'qs' : [family_data['qs']['index'][75]]},
            prefix + '20M2'   : {'qs' : [family_data['qs']['index'][76]]},
            prefix + '20C1'   : {'qs' : [family_data['qs']['index'][77]]},
            prefix + '20C5'   : {'qs' : [family_data['qs']['index'][78]]},
        }
        return qs_dict

    if family_name.lower() == 'sfa':
        prefix = 'SIPS-SFA-'
        sfa_dict = {
            prefix + '01M2'   : {'sfa' : [family_data['sfa']['index'][19]]},
            prefix + '02M2'   : {'sfa' : [family_data['sfa']['index'][0]]},
            prefix + '03M2'   : {'sfa' : [family_data['sfa']['index'][1]]},
            prefix + '04M2'   : {'sfa' : [family_data['sfa']['index'][2]]},
            prefix + '05M2'   : {'sfa' : [family_data['sfa']['index'][3]]},
            prefix + '06M2'   : {'sfa' : [family_data['sfa']['index'][4]]},
            prefix + '07M2'   : {'sfa' : [family_data['sfa']['index'][5]]},
            prefix + '08M2'   : {'sfa' : [family_data['sfa']['index'][6]]},
            prefix + '09M2'   : {'sfa' : [family_data['sfa']['index'][7]]},
            prefix + '10M2'   : {'sfa' : [family_data['sfa']['index'][8]]},
            prefix + '11M2'   : {'sfa' : [family_data['sfa']['index'][9]]},
            prefix + '12M2'   : {'sfa' : [family_data['sfa']['index'][10]]},
            prefix + '13M2'   : {'sfa' : [family_data['sfa']['index'][11]]},
            prefix + '14M2'   : {'sfa' : [family_data['sfa']['index'][12]]},
            prefix + '15M2'   : {'sfa' : [family_data['sfa']['index'][13]]},
            prefix + '16M2'   : {'sfa' : [family_data['sfa']['index'][14]]},
            prefix + '17M2'   : {'sfa' : [family_data['sfa']['index'][15]]},
            prefix + '18M2'   : {'sfa' : [family_data['sfa']['index'][16]]},
            prefix + '19M2'   : {'sfa' : [family_data['sfa']['index'][17]]},
            prefix + '20M2'   : {'sfa' : [family_data['sfa']['index'][18]]},
        }
        return sfa_dict


    if family_name.lower() == 'qfa':
        indices = family_data['qfa']['index']
        qfa_dict = {
            'SIPS-QFA-01M2'   : {'qfa' : [indices[19]]},
            'SIPS-QFA-02M2'   : {'qfa' : [indices[0]]},
            'SIPS-QFA-03M2'   : {'qfa' : [indices[1]]},
            'SIPS-QFA-04M2'   : {'qfa' : [indices[2]]},
            'SIPS-QFA-05M2'   : {'qfa' : [indices[3]]},
            'SIPS-QFA-06M2'   : {'qfa' : [indices[4]]},
            'SIPS-QFA-07M2'   : {'qfa' : [indices[5]]},
            'SIPS-QFA-08M2'   : {'qfa' : [indices[6]]},
            'SIPS-QFA-09M2'   : {'qfa' : [indices[7]]},
            'SIPS-QFA-10M2'   : {'qfa' : [indices[8]]},
            'SIPS-QFA-11M2'   : {'qfa' : [indices[9]]},
            'SIPS-QFA-12M2'   : {'qfa' : [indices[10]]},
            'SIPS-QFA-13M2'   : {'qfa' : [indices[11]]},
            'SIPS-QFA-14M2'   : {'qfa' : [indices[12]]},
            'SIPS-QFA-15M2'   : {'qfa' : [indices[13]]},
            'SIPS-QFA-16M2'   : {'qfa' : [indices[14]]},
            'SIPS-QFA-17M2'   : {'qfa' : [indices[15]]},
            'SIPS-QFA-18M2'   : {'qfa' : [indices[16]]},
            'SIPS-QFA-19M2'   : {'qfa' : [indices[17]]},
            'SIPS-QFA-20M2'   : {'qfa' : [indices[18]]},
        }
        return qfa_dict

    if family_name.lower() == 'qda':
        prefix = 'SIPS-QDA-'
        qda_dict = {
            prefix + '01M2'   : {'qda' : [family_data['qda']['index'][19]]},
            prefix + '02M2'   : {'qda' : [family_data['qda']['index'][0]]},
            prefix + '03M2'   : {'qda' : [family_data['qda']['index'][1]]},
            prefix + '04M2'   : {'qda' : [family_data['qda']['index'][2]]},
            prefix + '05M2'   : {'qda' : [family_data['qda']['index'][3]]},
            prefix + '06M2'   : {'qda' : [family_data['qda']['index'][4]]},
            prefix + '07M2'   : {'qda' : [family_data['qda']['index'][5]]},
            prefix + '08M2'   : {'qda' : [family_data['qda']['index'][6]]},
            prefix + '09M2'   : {'qda' : [family_data['qda']['index'][7]]},
            prefix + '10M2'   : {'qda' : [family_data['qda']['index'][8]]},
            prefix + '11M2'   : {'qda' : [family_data['qda']['index'][9]]},
            prefix + '12M2'   : {'qda' : [family_data['qda']['index'][10]]},
            prefix + '13M2'   : {'qda' : [family_data['qda']['index'][11]]},
            prefix + '14M2'   : {'qda' : [family_data['qda']['index'][12]]},
            prefix + '15M2'   : {'qda' : [family_data['qda']['index'][13]]},
            prefix + '16M2'   : {'qda' : [family_data['qda']['index'][14]]},
            prefix + '17M2'   : {'qda' : [family_data['qda']['index'][15]]},
            prefix + '18M2'   : {'qda' : [family_data['qda']['index'][16]]},
            prefix + '19M2'   : {'qda' : [family_data['qda']['index'][17]]},
            prefix + '20M2'   : {'qda' : [family_data['qda']['index'][18]]},
        }
        return qda_dict

    if family_name.lower() == 'sda':
        prefix = 'SIPS-SDA-'
        sda_dict = {
            prefix + '01M2'   : {'sda' : [family_data['sda']['index'][19]]},
            prefix + '02M2'   : {'sda' : [family_data['sda']['index'][0]]},
            prefix + '03M2'   : {'sda' : [family_data['sda']['index'][1]]},
            prefix + '04M2'   : {'sda' : [family_data['sda']['index'][2]]},
            prefix + '05M2'   : {'sda' : [family_data['sda']['index'][3]]},
            prefix + '06M2'   : {'sda' : [family_data['sda']['index'][4]]},
            prefix + '07M2'   : {'sda' : [family_data['sda']['index'][5]]},
            prefix + '08M2'   : {'sda' : [family_data['sda']['index'][6]]},
            prefix + '09M2'   : {'sda' : [family_data['sda']['index'][7]]},
            prefix + '10M2'   : {'sda' : [family_data['sda']['index'][8]]},
            prefix + '11M2'   : {'sda' : [family_data['sda']['index'][9]]},
            prefix + '12M2'   : {'sda' : [family_data['sda']['index'][10]]},
            prefix + '13M2'   : {'sda' : [family_data['sda']['index'][11]]},
            prefix + '14M2'   : {'sda' : [family_data['sda']['index'][12]]},
            prefix + '15M2'   : {'sda' : [family_data['sda']['index'][13]]},
            prefix + '16M2'   : {'sda' : [family_data['sda']['index'][14]]},
            prefix + '17M2'   : {'sda' : [family_data['sda']['index'][15]]},
            prefix + '18M2'   : {'sda' : [family_data['sda']['index'][16]]},
            prefix + '19M2'   : {'sda' : [family_data['sda']['index'][17]]},
            prefix + '20M2'   : {'sda' : [family_data['sda']['index'][18]]},
        }
        return sda_dict

    if family_name.lower() == 'sd1':
        prefix = 'SIPS-SD1-'
        sd1_dict = {
            prefix + '01C1'   : {'sd1' : [family_data['sd1']['index'][19]]},
            prefix + '02C1'   : {'sd1' : [family_data['sd1']['index'][0]]},
            prefix + '03C1'   : {'sd1' : [family_data['sd1']['index'][1]]},
            prefix + '04C1'   : {'sd1' : [family_data['sd1']['index'][2]]},
            prefix + '05C1'   : {'sd1' : [family_data['sd1']['index'][3]]},
            prefix + '06C1'   : {'sd1' : [family_data['sd1']['index'][4]]},
            prefix + '07C1'   : {'sd1' : [family_data['sd1']['index'][5]]},
            prefix + '08C1'   : {'sd1' : [family_data['sd1']['index'][6]]},
            prefix + '09C1'   : {'sd1' : [family_data['sd1']['index'][7]]},
            prefix + '10C1'   : {'sd1' : [family_data['sd1']['index'][8]]},
            prefix + '11C1'   : {'sd1' : [family_data['sd1']['index'][9]]},
            prefix + '12C1'   : {'sd1' : [family_data['sd1']['index'][10]]},
            prefix + '13C1'   : {'sd1' : [family_data['sd1']['index'][11]]},
            prefix + '14C1'   : {'sd1' : [family_data['sd1']['index'][12]]},
            prefix + '15C1'   : {'sd1' : [family_data['sd1']['index'][13]]},
            prefix + '16C1'   : {'sd1' : [family_data['sd1']['index'][14]]},
            prefix + '17C1'   : {'sd1' : [family_data['sd1']['index'][15]]},
            prefix + '18C1'   : {'sd1' : [family_data['sd1']['index'][16]]},
            prefix + '19C1'   : {'sd1' : [family_data['sd1']['index'][17]]},
            prefix + '20C1'   : {'sd1' : [family_data['sd1']['index'][18]]},
        }
        return sd1_dict

    if family_name.lower() == 'qf1':
        prefix = 'SIPS-QF1-'
        qf1_dict = {
            prefix + '01C1'   : {'qf1' : [family_data['qf1']['index'][39]]},
            prefix + '01C5'   : {'qf1' : [family_data['qf1']['index'][0]]},
            prefix + '02C1'   : {'qf1' : [family_data['qf1']['index'][1]]},
            prefix + '02C5'   : {'qf1' : [family_data['qf1']['index'][2]]},
            prefix + '03C1'   : {'qf1' : [family_data['qf1']['index'][3]]},
            prefix + '03C5'   : {'qf1' : [family_data['qf1']['index'][4]]},
            prefix + '04C1'   : {'qf1' : [family_data['qf1']['index'][5]]},
            prefix + '04C5'   : {'qf1' : [family_data['qf1']['index'][6]]},
            prefix + '05C1'   : {'qf1' : [family_data['qf1']['index'][7]]},
            prefix + '05C5'   : {'qf1' : [family_data['qf1']['index'][8]]},
            prefix + '06C1'   : {'qf1' : [family_data['qf1']['index'][9]]},
            prefix + '06C5'   : {'qf1' : [family_data['qf1']['index'][10]]},
            prefix + '07C1'   : {'qf1' : [family_data['qf1']['index'][11]]},
            prefix + '07C5'   : {'qf1' : [family_data['qf1']['index'][12]]},
            prefix + '08C1'   : {'qf1' : [family_data['qf1']['index'][13]]},
            prefix + '08C5'   : {'qf1' : [family_data['qf1']['index'][14]]},
            prefix + '09C1'   : {'qf1' : [family_data['qf1']['index'][15]]},
            prefix + '09C5'   : {'qf1' : [family_data['qf1']['index'][16]]},
            prefix + '10C1'   : {'qf1' : [family_data['qf1']['index'][17]]},
            prefix + '10C5'   : {'qf1' : [family_data['qf1']['index'][18]]},
            prefix + '11C1'   : {'qf1' : [family_data['qf1']['index'][19]]},
            prefix + '11C5'   : {'qf1' : [family_data['qf1']['index'][20]]},
            prefix + '12C1'   : {'qf1' : [family_data['qf1']['index'][21]]},
            prefix + '12C5'   : {'qf1' : [family_data['qf1']['index'][22]]},
            prefix + '13C1'   : {'qf1' : [family_data['qf1']['index'][23]]},
            prefix + '13C5'   : {'qf1' : [family_data['qf1']['index'][24]]},
            prefix + '14C1'   : {'qf1' : [family_data['qf1']['index'][25]]},
            prefix + '14C5'   : {'qf1' : [family_data['qf1']['index'][26]]},
            prefix + '15C1'   : {'qf1' : [family_data['qf1']['index'][27]]},
            prefix + '15C5'   : {'qf1' : [family_data['qf1']['index'][28]]},
            prefix + '16C1'   : {'qf1' : [family_data['qf1']['index'][29]]},
            prefix + '16C5'   : {'qf1' : [family_data['qf1']['index'][30]]},
            prefix + '17C1'   : {'qf1' : [family_data['qf1']['index'][31]]},
            prefix + '17C5'   : {'qf1' : [family_data['qf1']['index'][32]]},
            prefix + '18C1'   : {'qf1' : [family_data['qf1']['index'][33]]},
            prefix + '18C5'   : {'qf1' : [family_data['qf1']['index'][34]]},
            prefix + '19C1'   : {'qf1' : [family_data['qf1']['index'][35]]},
            prefix + '19C5'   : {'qf1' : [family_data['qf1']['index'][36]]},
            prefix + '20C1'   : {'qf1' : [family_data['qf1']['index'][37]]},
            prefix + '20C5'   : {'qf1' : [family_data['qf1']['index'][38]]},
        }
        return qf1_dict

    if family_name.lower() == 'sf1':
        prefix = 'SIPS-SF1-'
        sf1_dict = {
            prefix + '01C1'   : {'sf1' : [family_data['sf1']['index'][19]]},
            prefix + '02C1'   : {'sf1' : [family_data['sf1']['index'][0]]},
            prefix + '03C1'   : {'sf1' : [family_data['sf1']['index'][1]]},
            prefix + '04C1'   : {'sf1' : [family_data['sf1']['index'][2]]},
            prefix + '05C1'   : {'sf1' : [family_data['sf1']['index'][3]]},
            prefix + '06C1'   : {'sf1' : [family_data['sf1']['index'][4]]},
            prefix + '07C1'   : {'sf1' : [family_data['sf1']['index'][5]]},
            prefix + '08C1'   : {'sf1' : [family_data['sf1']['index'][6]]},
            prefix + '09C1'   : {'sf1' : [family_data['sf1']['index'][7]]},
            prefix + '10C1'   : {'sf1' : [family_data['sf1']['index'][8]]},
            prefix + '11C1'   : {'sf1' : [family_data['sf1']['index'][9]]},
            prefix + '12C1'   : {'sf1' : [family_data['sf1']['index'][10]]},
            prefix + '13C1'   : {'sf1' : [family_data['sf1']['index'][11]]},
            prefix + '14C1'   : {'sf1' : [family_data['sf1']['index'][12]]},
            prefix + '15C1'   : {'sf1' : [family_data['sf1']['index'][13]]},
            prefix + '16C1'   : {'sf1' : [family_data['sf1']['index'][14]]},
            prefix + '17C1'   : {'sf1' : [family_data['sf1']['index'][15]]},
            prefix + '18C1'   : {'sf1' : [family_data['sf1']['index'][16]]},
            prefix + '19C1'   : {'sf1' : [family_data['sf1']['index'][17]]},
            prefix + '20C1'   : {'sf1' : [family_data['sf1']['index'][18]]},
        }
        return sf1_dict

    if family_name.lower() == 'qf2':
        prefix = 'SIPS-QF2-'
        qf2_dict = {
            prefix + '01C1'   : {'qf2' : [family_data['qf2']['index'][39]]},
            prefix + '01C5'   : {'qf2' : [family_data['qf2']['index'][0]]},
            prefix + '02C1'   : {'qf2' : [family_data['qf2']['index'][1]]},
            prefix + '02C5'   : {'qf2' : [family_data['qf2']['index'][2]]},
            prefix + '03C1'   : {'qf2' : [family_data['qf2']['index'][3]]},
            prefix + '03C5'   : {'qf2' : [family_data['qf2']['index'][4]]},
            prefix + '04C1'   : {'qf2' : [family_data['qf2']['index'][5]]},
            prefix + '04C5'   : {'qf2' : [family_data['qf2']['index'][6]]},
            prefix + '05C1'   : {'qf2' : [family_data['qf2']['index'][7]]},
            prefix + '05C5'   : {'qf2' : [family_data['qf2']['index'][8]]},
            prefix + '06C1'   : {'qf2' : [family_data['qf2']['index'][9]]},
            prefix + '06C5'   : {'qf2' : [family_data['qf2']['index'][10]]},
            prefix + '07C1'   : {'qf2' : [family_data['qf2']['index'][11]]},
            prefix + '07C5'   : {'qf2' : [family_data['qf2']['index'][12]]},
            prefix + '08C1'   : {'qf2' : [family_data['qf2']['index'][13]]},
            prefix + '08C5'   : {'qf2' : [family_data['qf2']['index'][14]]},
            prefix + '09C1'   : {'qf2' : [family_data['qf2']['index'][15]]},
            prefix + '09C5'   : {'qf2' : [family_data['qf2']['index'][16]]},
            prefix + '10C1'   : {'qf2' : [family_data['qf2']['index'][17]]},
            prefix + '10C5'   : {'qf2' : [family_data['qf2']['index'][18]]},
            prefix + '11C1'   : {'qf2' : [family_data['qf2']['index'][19]]},
            prefix + '11C5'   : {'qf2' : [family_data['qf2']['index'][20]]},
            prefix + '12C1'   : {'qf2' : [family_data['qf2']['index'][21]]},
            prefix + '12C5'   : {'qf2' : [family_data['qf2']['index'][22]]},
            prefix + '13C1'   : {'qf2' : [family_data['qf2']['index'][23]]},
            prefix + '13C5'   : {'qf2' : [family_data['qf2']['index'][24]]},
            prefix + '14C1'   : {'qf2' : [family_data['qf2']['index'][25]]},
            prefix + '14C5'   : {'qf2' : [family_data['qf2']['index'][26]]},
            prefix + '15C1'   : {'qf2' : [family_data['qf2']['index'][27]]},
            prefix + '15C5'   : {'qf2' : [family_data['qf2']['index'][28]]},
            prefix + '16C1'   : {'qf2' : [family_data['qf2']['index'][29]]},
            prefix + '16C5'   : {'qf2' : [family_data['qf2']['index'][30]]},
            prefix + '17C1'   : {'qf2' : [family_data['qf2']['index'][31]]},
            prefix + '17C5'   : {'qf2' : [family_data['qf2']['index'][32]]},
            prefix + '18C1'   : {'qf2' : [family_data['qf2']['index'][33]]},
            prefix + '18C5'   : {'qf2' : [family_data['qf2']['index'][34]]},
            prefix + '19C1'   : {'qf2' : [family_data['qf2']['index'][35]]},
            prefix + '19C5'   : {'qf2' : [family_data['qf2']['index'][36]]},
            prefix + '20C1'   : {'qf2' : [family_data['qf2']['index'][37]]},
            prefix + '20C5'   : {'qf2' : [family_data['qf2']['index'][38]]},
        }
        return qf2_dict

    if family_name.lower() == 'sd2':
        prefix = 'SIPS-SD2-'
        sd2_dict = {
            prefix + '01C1'   : {'sd2' : [family_data['sd2']['index'][19]]},
            prefix + '02C1'   : {'sd2' : [family_data['sd2']['index'][0]]},
            prefix + '03C1'   : {'sd2' : [family_data['sd2']['index'][1]]},
            prefix + '04C1'   : {'sd2' : [family_data['sd2']['index'][2]]},
            prefix + '05C1'   : {'sd2' : [family_data['sd2']['index'][3]]},
            prefix + '06C1'   : {'sd2' : [family_data['sd2']['index'][4]]},
            prefix + '07C1'   : {'sd2' : [family_data['sd2']['index'][5]]},
            prefix + '08C1'   : {'sd2' : [family_data['sd2']['index'][6]]},
            prefix + '09C1'   : {'sd2' : [family_data['sd2']['index'][7]]},
            prefix + '10C1'   : {'sd2' : [family_data['sd2']['index'][8]]},
            prefix + '11C1'   : {'sd2' : [family_data['sd2']['index'][9]]},
            prefix + '12C1'   : {'sd2' : [family_data['sd2']['index'][10]]},
            prefix + '13C1'   : {'sd2' : [family_data['sd2']['index'][11]]},
            prefix + '14C1'   : {'sd2' : [family_data['sd2']['index'][12]]},
            prefix + '15C1'   : {'sd2' : [family_data['sd2']['index'][13]]},
            prefix + '16C1'   : {'sd2' : [family_data['sd2']['index'][14]]},
            prefix + '17C1'   : {'sd2' : [family_data['sd2']['index'][15]]},
            prefix + '18C1'   : {'sd2' : [family_data['sd2']['index'][16]]},
            prefix + '19C1'   : {'sd2' : [family_data['sd2']['index'][17]]},
            prefix + '20C1'   : {'sd2' : [family_data['sd2']['index'][18]]},
        }
        return sd2_dict

    if family_name.lower() == 'sd3':
        prefix = 'SIPS-SD3-'
        sd3_dict = {
            prefix + '01C2'   : {'sd3' : [family_data['sd3']['index'][19]]},
            prefix + '02C2'   : {'sd3' : [family_data['sd3']['index'][0]]},
            prefix + '03C2'   : {'sd3' : [family_data['sd3']['index'][1]]},
            prefix + '04C2'   : {'sd3' : [family_data['sd3']['index'][2]]},
            prefix + '05C2'   : {'sd3' : [family_data['sd3']['index'][3]]},
            prefix + '06C2'   : {'sd3' : [family_data['sd3']['index'][4]]},
            prefix + '07C2'   : {'sd3' : [family_data['sd3']['index'][5]]},
            prefix + '08C2'   : {'sd3' : [family_data['sd3']['index'][6]]},
            prefix + '09C2'   : {'sd3' : [family_data['sd3']['index'][7]]},
            prefix + '10C2'   : {'sd3' : [family_data['sd3']['index'][8]]},
            prefix + '11C2'   : {'sd3' : [family_data['sd3']['index'][9]]},
            prefix + '12C2'   : {'sd3' : [family_data['sd3']['index'][10]]},
            prefix + '13C2'   : {'sd3' : [family_data['sd3']['index'][11]]},
            prefix + '14C2'   : {'sd3' : [family_data['sd3']['index'][12]]},
            prefix + '15C2'   : {'sd3' : [family_data['sd3']['index'][13]]},
            prefix + '16C2'   : {'sd3' : [family_data['sd3']['index'][14]]},
            prefix + '17C2'   : {'sd3' : [family_data['sd3']['index'][15]]},
            prefix + '18C2'   : {'sd3' : [family_data['sd3']['index'][16]]},
            prefix + '19C2'   : {'sd3' : [family_data['sd3']['index'][17]]},
            prefix + '20C2'   : {'sd3' : [family_data['sd3']['index'][18]]},
        }
        return sd3_dict

    if family_name.lower() == 'qf3':
        prefix = 'SIPS-QF3-'
        qf3_dict = {
            prefix + '01C2'   : {'qf3' : [family_data['qf3']['index'][39]]},
            prefix + '01C4'   : {'qf3' : [family_data['qf3']['index'][0]]},
            prefix + '02C2'   : {'qf3' : [family_data['qf3']['index'][1]]},
            prefix + '02C4'   : {'qf3' : [family_data['qf3']['index'][2]]},
            prefix + '03C2'   : {'qf3' : [family_data['qf3']['index'][3]]},
            prefix + '03C4'   : {'qf3' : [family_data['qf3']['index'][4]]},
            prefix + '04C2'   : {'qf3' : [family_data['qf3']['index'][5]]},
            prefix + '04C4'   : {'qf3' : [family_data['qf3']['index'][6]]},
            prefix + '05C2'   : {'qf3' : [family_data['qf3']['index'][7]]},
            prefix + '05C4'   : {'qf3' : [family_data['qf3']['index'][8]]},
            prefix + '06C2'   : {'qf3' : [family_data['qf3']['index'][9]]},
            prefix + '06C4'   : {'qf3' : [family_data['qf3']['index'][10]]},
            prefix + '07C2'   : {'qf3' : [family_data['qf3']['index'][11]]},
            prefix + '07C4'   : {'qf3' : [family_data['qf3']['index'][12]]},
            prefix + '08C2'   : {'qf3' : [family_data['qf3']['index'][13]]},
            prefix + '08C4'   : {'qf3' : [family_data['qf3']['index'][14]]},
            prefix + '09C2'   : {'qf3' : [family_data['qf3']['index'][15]]},
            prefix + '09C4'   : {'qf3' : [family_data['qf3']['index'][16]]},
            prefix + '10C2'   : {'qf3' : [family_data['qf3']['index'][17]]},
            prefix + '10C4'   : {'qf3' : [family_data['qf3']['index'][18]]},
            prefix + '11C2'   : {'qf3' : [family_data['qf3']['index'][19]]},
            prefix + '11C4'   : {'qf3' : [family_data['qf3']['index'][20]]},
            prefix + '12C2'   : {'qf3' : [family_data['qf3']['index'][21]]},
            prefix + '12C4'   : {'qf3' : [family_data['qf3']['index'][22]]},
            prefix + '13C2'   : {'qf3' : [family_data['qf3']['index'][23]]},
            prefix + '13C4'   : {'qf3' : [family_data['qf3']['index'][24]]},
            prefix + '14C2'   : {'qf3' : [family_data['qf3']['index'][25]]},
            prefix + '14C4'   : {'qf3' : [family_data['qf3']['index'][26]]},
            prefix + '15C2'   : {'qf3' : [family_data['qf3']['index'][27]]},
            prefix + '15C4'   : {'qf3' : [family_data['qf3']['index'][28]]},
            prefix + '16C2'   : {'qf3' : [family_data['qf3']['index'][29]]},
            prefix + '16C4'   : {'qf3' : [family_data['qf3']['index'][30]]},
            prefix + '17C2'   : {'qf3' : [family_data['qf3']['index'][31]]},
            prefix + '17C4'   : {'qf3' : [family_data['qf3']['index'][32]]},
            prefix + '18C2'   : {'qf3' : [family_data['qf3']['index'][33]]},
            prefix + '18C4'   : {'qf3' : [family_data['qf3']['index'][34]]},
            prefix + '19C2'   : {'qf3' : [family_data['qf3']['index'][35]]},
            prefix + '19C4'   : {'qf3' : [family_data['qf3']['index'][36]]},
            prefix + '20C2'   : {'qf3' : [family_data['qf3']['index'][37]]},
            prefix + '20C4'   : {'qf3' : [family_data['qf3']['index'][38]]},
        }
        return qf3_dict

    if family_name.lower() == 'sf2':
        prefix = 'SIPS-SF2-'
        sf2_dict = {
            prefix + '01C2'   : {'sf2' : [family_data['sf2']['index'][19]]},
            prefix + '02C2'   : {'sf2' : [family_data['sf2']['index'][0]]},
            prefix + '03C2'   : {'sf2' : [family_data['sf2']['index'][1]]},
            prefix + '04C2'   : {'sf2' : [family_data['sf2']['index'][2]]},
            prefix + '05C2'   : {'sf2' : [family_data['sf2']['index'][3]]},
            prefix + '06C2'   : {'sf2' : [family_data['sf2']['index'][4]]},
            prefix + '07C2'   : {'sf2' : [family_data['sf2']['index'][5]]},
            prefix + '08C2'   : {'sf2' : [family_data['sf2']['index'][6]]},
            prefix + '09C2'   : {'sf2' : [family_data['sf2']['index'][7]]},
            prefix + '10C2'   : {'sf2' : [family_data['sf2']['index'][8]]},
            prefix + '11C2'   : {'sf2' : [family_data['sf2']['index'][9]]},
            prefix + '12C2'   : {'sf2' : [family_data['sf2']['index'][10]]},
            prefix + '13C2'   : {'sf2' : [family_data['sf2']['index'][11]]},
            prefix + '14C2'   : {'sf2' : [family_data['sf2']['index'][12]]},
            prefix + '15C2'   : {'sf2' : [family_data['sf2']['index'][13]]},
            prefix + '16C2'   : {'sf2' : [family_data['sf2']['index'][14]]},
            prefix + '17C2'   : {'sf2' : [family_data['sf2']['index'][15]]},
            prefix + '18C2'   : {'sf2' : [family_data['sf2']['index'][16]]},
            prefix + '19C2'   : {'sf2' : [family_data['sf2']['index'][17]]},
            prefix + '20C2'   : {'sf2' : [family_data['sf2']['index'][18]]},
        }
        return sf2_dict

    if family_name.lower() == 'qf4':
        prefix = 'SIPS-QF4-'
        qf4_dict = {
            prefix + '01C2'   : {'qf4' : [family_data['qf4']['index'][39]]},
            prefix + '01C4'   : {'qf4' : [family_data['qf4']['index'][0]]},
            prefix + '02C2'   : {'qf4' : [family_data['qf4']['index'][1]]},
            prefix + '02C4'   : {'qf4' : [family_data['qf4']['index'][2]]},
            prefix + '03C2'   : {'qf4' : [family_data['qf4']['index'][3]]},
            prefix + '03C4'   : {'qf4' : [family_data['qf4']['index'][4]]},
            prefix + '04C2'   : {'qf4' : [family_data['qf4']['index'][5]]},
            prefix + '04C4'   : {'qf4' : [family_data['qf4']['index'][6]]},
            prefix + '05C2'   : {'qf4' : [family_data['qf4']['index'][7]]},
            prefix + '05C4'   : {'qf4' : [family_data['qf4']['index'][8]]},
            prefix + '06C2'   : {'qf4' : [family_data['qf4']['index'][9]]},
            prefix + '06C4'   : {'qf4' : [family_data['qf4']['index'][10]]},
            prefix + '07C2'   : {'qf4' : [family_data['qf4']['index'][11]]},
            prefix + '07C4'   : {'qf4' : [family_data['qf4']['index'][12]]},
            prefix + '08C2'   : {'qf4' : [family_data['qf4']['index'][13]]},
            prefix + '08C4'   : {'qf4' : [family_data['qf4']['index'][14]]},
            prefix + '09C2'   : {'qf4' : [family_data['qf4']['index'][15]]},
            prefix + '09C4'   : {'qf4' : [family_data['qf4']['index'][16]]},
            prefix + '10C2'   : {'qf4' : [family_data['qf4']['index'][17]]},
            prefix + '10C4'   : {'qf4' : [family_data['qf4']['index'][18]]},
            prefix + '11C2'   : {'qf4' : [family_data['qf4']['index'][19]]},
            prefix + '11C4'   : {'qf4' : [family_data['qf4']['index'][20]]},
            prefix + '12C2'   : {'qf4' : [family_data['qf4']['index'][21]]},
            prefix + '12C4'   : {'qf4' : [family_data['qf4']['index'][22]]},
            prefix + '13C2'   : {'qf4' : [family_data['qf4']['index'][23]]},
            prefix + '13C4'   : {'qf4' : [family_data['qf4']['index'][24]]},
            prefix + '14C2'   : {'qf4' : [family_data['qf4']['index'][25]]},
            prefix + '14C4'   : {'qf4' : [family_data['qf4']['index'][26]]},
            prefix + '15C2'   : {'qf4' : [family_data['qf4']['index'][27]]},
            prefix + '15C4'   : {'qf4' : [family_data['qf4']['index'][28]]},
            prefix + '16C2'   : {'qf4' : [family_data['qf4']['index'][29]]},
            prefix + '16C4'   : {'qf4' : [family_data['qf4']['index'][30]]},
            prefix + '17C2'   : {'qf4' : [family_data['qf4']['index'][31]]},
            prefix + '17C4'   : {'qf4' : [family_data['qf4']['index'][32]]},
            prefix + '18C2'   : {'qf4' : [family_data['qf4']['index'][33]]},
            prefix + '18C4'   : {'qf4' : [family_data['qf4']['index'][34]]},
            prefix + '19C2'   : {'qf4' : [family_data['qf4']['index'][35]]},
            prefix + '19C4'   : {'qf4' : [family_data['qf4']['index'][36]]},
            prefix + '20C2'   : {'qf4' : [family_data['qf4']['index'][37]]},
            prefix + '20C4'   : {'qf4' : [family_data['qf4']['index'][38]]},
        }
        return qf4_dict

    if family_name.lower() == 'sf3':
        prefix = 'SIPS-SF3-'
        sf3_dict = {
            prefix + '01C4'   : {'sf3' : [family_data['sf3']['index'][19]]},
            prefix + '02C4'   : {'sf3' : [family_data['sf3']['index'][0]]},
            prefix + '03C4'   : {'sf3' : [family_data['sf3']['index'][1]]},
            prefix + '04C4'   : {'sf3' : [family_data['sf3']['index'][2]]},
            prefix + '05C4'   : {'sf3' : [family_data['sf3']['index'][3]]},
            prefix + '06C4'   : {'sf3' : [family_data['sf3']['index'][4]]},
            prefix + '07C4'   : {'sf3' : [family_data['sf3']['index'][5]]},
            prefix + '08C4'   : {'sf3' : [family_data['sf3']['index'][6]]},
            prefix + '09C4'   : {'sf3' : [family_data['sf3']['index'][7]]},
            prefix + '10C4'   : {'sf3' : [family_data['sf3']['index'][8]]},
            prefix + '11C4'   : {'sf3' : [family_data['sf3']['index'][9]]},
            prefix + '12C4'   : {'sf3' : [family_data['sf3']['index'][10]]},
            prefix + '13C4'   : {'sf3' : [family_data['sf3']['index'][11]]},
            prefix + '14C4'   : {'sf3' : [family_data['sf3']['index'][12]]},
            prefix + '15C4'   : {'sf3' : [family_data['sf3']['index'][13]]},
            prefix + '16C4'   : {'sf3' : [family_data['sf3']['index'][14]]},
            prefix + '17C4'   : {'sf3' : [family_data['sf3']['index'][15]]},
            prefix + '18C4'   : {'sf3' : [family_data['sf3']['index'][16]]},
            prefix + '19C4'   : {'sf3' : [family_data['sf3']['index'][17]]},
            prefix + '20C4'   : {'sf3' : [family_data['sf3']['index'][18]]},
        }
        return sf3_dict

    if family_name.lower() == 'sd4':
        prefix = 'SIPS-SD4-'
        sd4_dict = {
            prefix + '01C4'   : {'sd4' : [family_data['sd4']['index'][19]]},
            prefix + '02C4'   : {'sd4' : [family_data['sd4']['index'][0]]},
            prefix + '03C4'   : {'sd4' : [family_data['sd4']['index'][1]]},
            prefix + '04C4'   : {'sd4' : [family_data['sd4']['index'][2]]},
            prefix + '05C4'   : {'sd4' : [family_data['sd4']['index'][3]]},
            prefix + '06C4'   : {'sd4' : [family_data['sd4']['index'][4]]},
            prefix + '07C4'   : {'sd4' : [family_data['sd4']['index'][5]]},
            prefix + '08C4'   : {'sd4' : [family_data['sd4']['index'][6]]},
            prefix + '09C4'   : {'sd4' : [family_data['sd4']['index'][7]]},
            prefix + '10C4'   : {'sd4' : [family_data['sd4']['index'][8]]},
            prefix + '11C4'   : {'sd4' : [family_data['sd4']['index'][9]]},
            prefix + '12C4'   : {'sd4' : [family_data['sd4']['index'][10]]},
            prefix + '13C4'   : {'sd4' : [family_data['sd4']['index'][11]]},
            prefix + '14C4'   : {'sd4' : [family_data['sd4']['index'][12]]},
            prefix + '15C4'   : {'sd4' : [family_data['sd4']['index'][13]]},
            prefix + '16C4'   : {'sd4' : [family_data['sd4']['index'][14]]},
            prefix + '17C4'   : {'sd4' : [family_data['sd4']['index'][15]]},
            prefix + '18C4'   : {'sd4' : [family_data['sd4']['index'][16]]},
            prefix + '19C4'   : {'sd4' : [family_data['sd4']['index'][17]]},
            prefix + '20C4'   : {'sd4' : [family_data['sd4']['index'][18]]},
        }
        return sd4_dict

    if family_name.lower() == 'sd5':
        prefix = 'SIPS-SD5-'
        sd5_dict = {
            prefix + '01C5'   : {'sd5' : [family_data['sd5']['index'][19]]},
            prefix + '02C5'   : {'sd5' : [family_data['sd5']['index'][0]]},
            prefix + '03C5'   : {'sd5' : [family_data['sd5']['index'][1]]},
            prefix + '04C5'   : {'sd5' : [family_data['sd5']['index'][2]]},
            prefix + '05C5'   : {'sd5' : [family_data['sd5']['index'][3]]},
            prefix + '06C5'   : {'sd5' : [family_data['sd5']['index'][4]]},
            prefix + '07C5'   : {'sd5' : [family_data['sd5']['index'][5]]},
            prefix + '08C5'   : {'sd5' : [family_data['sd5']['index'][6]]},
            prefix + '09C5'   : {'sd5' : [family_data['sd5']['index'][7]]},
            prefix + '10C5'   : {'sd5' : [family_data['sd5']['index'][8]]},
            prefix + '11C5'   : {'sd5' : [family_data['sd5']['index'][9]]},
            prefix + '12C5'   : {'sd5' : [family_data['sd5']['index'][10]]},
            prefix + '13C5'   : {'sd5' : [family_data['sd5']['index'][11]]},
            prefix + '14C5'   : {'sd5' : [family_data['sd5']['index'][12]]},
            prefix + '15C5'   : {'sd5' : [family_data['sd5']['index'][13]]},
            prefix + '16C5'   : {'sd5' : [family_data['sd5']['index'][14]]},
            prefix + '17C5'   : {'sd5' : [family_data['sd5']['index'][15]]},
            prefix + '18C5'   : {'sd5' : [family_data['sd5']['index'][16]]},
            prefix + '19C5'   : {'sd5' : [family_data['sd5']['index'][17]]},
            prefix + '20C5'   : {'sd5' : [family_data['sd5']['index'][18]]},        }
        return sd5_dict

    if family_name.lower() == 'sf4':
        prefix = 'SIPS-SF4-'
        sf4_dict = {
            prefix + '01C5'   : {'sf4' : [family_data['sf4']['index'][19]]},
            prefix + '02C5'   : {'sf4' : [family_data['sf4']['index'][0]]},
            prefix + '03C5'   : {'sf4' : [family_data['sf4']['index'][1]]},
            prefix + '04C5'   : {'sf4' : [family_data['sf4']['index'][2]]},
            prefix + '05C5'   : {'sf4' : [family_data['sf4']['index'][3]]},
            prefix + '06C5'   : {'sf4' : [family_data['sf4']['index'][4]]},
            prefix + '07C5'   : {'sf4' : [family_data['sf4']['index'][5]]},
            prefix + '08C5'   : {'sf4' : [family_data['sf4']['index'][6]]},
            prefix + '09C5'   : {'sf4' : [family_data['sf4']['index'][7]]},
            prefix + '10C5'   : {'sf4' : [family_data['sf4']['index'][8]]},
            prefix + '11C5'   : {'sf4' : [family_data['sf4']['index'][9]]},
            prefix + '12C5'   : {'sf4' : [family_data['sf4']['index'][10]]},
            prefix + '13C5'   : {'sf4' : [family_data['sf4']['index'][11]]},
            prefix + '14C5'   : {'sf4' : [family_data['sf4']['index'][12]]},
            prefix + '15C5'   : {'sf4' : [family_data['sf4']['index'][13]]},
            prefix + '16C5'   : {'sf4' : [family_data['sf4']['index'][14]]},
            prefix + '17C5'   : {'sf4' : [family_data['sf4']['index'][15]]},
            prefix + '18C5'   : {'sf4' : [family_data['sf4']['index'][16]]},
            prefix + '19C5'   : {'sf4' : [family_data['sf4']['index'][17]]},
            prefix + '20C5'   : {'sf4' : [family_data['sf4']['index'][18]]},
        }
        return sf4_dict

    if family_name.lower() == 'sd6':
        prefix = 'SIPS-SD6-'
        sd6_dict = {
            prefix + '01C5'   : {'sd6' : [family_data['sd6']['index'][19]]},
            prefix + '02C5'   : {'sd6' : [family_data['sd6']['index'][0]]},
            prefix + '03C5'   : {'sd6' : [family_data['sd6']['index'][1]]},
            prefix + '04C5'   : {'sd6' : [family_data['sd6']['index'][2]]},
            prefix + '05C5'   : {'sd6' : [family_data['sd6']['index'][3]]},
            prefix + '06C5'   : {'sd6' : [family_data['sd6']['index'][4]]},
            prefix + '07C5'   : {'sd6' : [family_data['sd6']['index'][5]]},
            prefix + '08C5'   : {'sd6' : [family_data['sd6']['index'][6]]},
            prefix + '09C5'   : {'sd6' : [family_data['sd6']['index'][7]]},
            prefix + '10C5'   : {'sd6' : [family_data['sd6']['index'][8]]},
            prefix + '11C5'   : {'sd6' : [family_data['sd6']['index'][9]]},
            prefix + '12C5'   : {'sd6' : [family_data['sd6']['index'][10]]},
            prefix + '13C5'   : {'sd6' : [family_data['sd6']['index'][11]]},
            prefix + '14C5'   : {'sd6' : [family_data['sd6']['index'][12]]},
            prefix + '15C5'   : {'sd6' : [family_data['sd6']['index'][13]]},
            prefix + '16C5'   : {'sd6' : [family_data['sd6']['index'][14]]},
            prefix + '17C5'   : {'sd6' : [family_data['sd6']['index'][15]]},
            prefix + '18C5'   : {'sd6' : [family_data['sd6']['index'][16]]},
            prefix + '19C5'   : {'sd6' : [family_data['sd6']['index'][17]]},
            prefix + '20C5'   : {'sd6' : [family_data['sd6']['index'][18]]},
        }
        return sd6_dict

    if family_name.lower() == 'sdb':
        prefix = 'SIPS-SDB-'
        sdb_dict = {
            prefix + '01M1'   : {'sdb' : [family_data['sdb']['index'][19]]},
            prefix + '02M1'   : {'sdb' : [family_data['sdb']['index'][0]]},
            prefix + '03M1'   : {'sdb' : [family_data['sdb']['index'][1]]},
            prefix + '04M1'   : {'sdb' : [family_data['sdb']['index'][2]]},
            prefix + '05M1'   : {'sdb' : [family_data['sdb']['index'][3]]},
            prefix + '06M1'   : {'sdb' : [family_data['sdb']['index'][4]]},
            prefix + '07M1'   : {'sdb' : [family_data['sdb']['index'][5]]},
            prefix + '08M1'   : {'sdb' : [family_data['sdb']['index'][6]]},
            prefix + '09M1'   : {'sdb' : [family_data['sdb']['index'][7]]},
            prefix + '10M1'   : {'sdb' : [family_data['sdb']['index'][8]]},
            prefix + '11M1'   : {'sdb' : [family_data['sdb']['index'][9]]},
            prefix + '12M1'   : {'sdb' : [family_data['sdb']['index'][10]]},
            prefix + '13M1'   : {'sdb' : [family_data['sdb']['index'][11]]},
            prefix + '14M1'   : {'sdb' : [family_data['sdb']['index'][12]]},
            prefix + '15M1'   : {'sdb' : [family_data['sdb']['index'][13]]},
            prefix + '16M1'   : {'sdb' : [family_data['sdb']['index'][14]]},
            prefix + '17M1'   : {'sdb' : [family_data['sdb']['index'][15]]},
            prefix + '18M1'   : {'sdb' : [family_data['sdb']['index'][16]]},
            prefix + '19M1'   : {'sdb' : [family_data['sdb']['index'][17]]},
            prefix + '20M1'   : {'sdb' : [family_data['sdb']['index'][18]]},
        }
        return sdb_dict

    if family_name.lower() == 'qdb1':
        prefix = 'SIPS-QDB1-'
        qdb1_dict = {
            prefix + '01M1'   : {'qdb1' : [family_data['qdb1']['index'][19]]},
            prefix + '02M1'   : {'qdb1' : [family_data['qdb1']['index'][0]]},
            prefix + '03M1'   : {'qdb1' : [family_data['qdb1']['index'][1]]},
            prefix + '04M1'   : {'qdb1' : [family_data['qdb1']['index'][2]]},
            prefix + '05M1'   : {'qdb1' : [family_data['qdb1']['index'][3]]},
            prefix + '06M1'   : {'qdb1' : [family_data['qdb1']['index'][4]]},
            prefix + '07M1'   : {'qdb1' : [family_data['qdb1']['index'][5]]},
            prefix + '08M1'   : {'qdb1' : [family_data['qdb1']['index'][6]]},
            prefix + '09M1'   : {'qdb1' : [family_data['qdb1']['index'][7]]},
            prefix + '10M1'   : {'qdb1' : [family_data['qdb1']['index'][8]]},
            prefix + '11M1'   : {'qdb1' : [family_data['qdb1']['index'][9]]},
            prefix + '12M1'   : {'qdb1' : [family_data['qdb1']['index'][10]]},
            prefix + '13M1'   : {'qdb1' : [family_data['qdb1']['index'][11]]},
            prefix + '14M1'   : {'qdb1' : [family_data['qdb1']['index'][12]]},
            prefix + '15M1'   : {'qdb1' : [family_data['qdb1']['index'][13]]},
            prefix + '16M1'   : {'qdb1' : [family_data['qdb1']['index'][14]]},
            prefix + '17M1'   : {'qdb1' : [family_data['qdb1']['index'][15]]},
            prefix + '18M1'   : {'qdb1' : [family_data['qdb1']['index'][16]]},
            prefix + '19M1'   : {'qdb1' : [family_data['qdb1']['index'][17]]},
            prefix + '20M1'   : {'qdb1' : [family_data['qdb1']['index'][18]]},
        }
        return qdb1_dict

    if family_name.lower() == 'qfb':
        prefix = 'SIPS-QFB-'
        qfb_dict = {
            prefix + '01M1'   : {'qfb' : [family_data['qfb']['index'][19]]},
            prefix + '02M1'   : {'qfb' : [family_data['qfb']['index'][0]]},
            prefix + '03M1'   : {'qfb' : [family_data['qfb']['index'][1]]},
            prefix + '04M1'   : {'qfb' : [family_data['qfb']['index'][2]]},
            prefix + '05M1'   : {'qfb' : [family_data['qfb']['index'][3]]},
            prefix + '06M1'   : {'qfb' : [family_data['qfb']['index'][4]]},
            prefix + '07M1'   : {'qfb' : [family_data['qfb']['index'][5]]},
            prefix + '08M1'   : {'qfb' : [family_data['qfb']['index'][6]]},
            prefix + '09M1'   : {'qfb' : [family_data['qfb']['index'][7]]},
            prefix + '10M1'   : {'qfb' : [family_data['qfb']['index'][8]]},
            prefix + '11M1'   : {'qfb' : [family_data['qfb']['index'][9]]},
            prefix + '12M1'   : {'qfb' : [family_data['qfb']['index'][10]]},
            prefix + '13M1'   : {'qfb' : [family_data['qfb']['index'][11]]},
            prefix + '14M1'   : {'qfb' : [family_data['qfb']['index'][12]]},
            prefix + '15M1'   : {'qfb' : [family_data['qfb']['index'][13]]},
            prefix + '16M1'   : {'qfb' : [family_data['qfb']['index'][14]]},
            prefix + '17M1'   : {'qfb' : [family_data['qfb']['index'][15]]},
            prefix + '18M1'   : {'qfb' : [family_data['qfb']['index'][16]]},
            prefix + '19M1'   : {'qfb' : [family_data['qfb']['index'][17]]},
            prefix + '20M1'   : {'qfb' : [family_data['qfb']['index'][18]]},
        }
        return qfb_dict

    if family_name.lower() == 'sfb':
        prefix = 'SIPS-SFB-'
        sfb_dict = {
            prefix + '01M1'   : {'sfb' : [family_data['sfb']['index'][19]]},
            prefix + '02M1'   : {'sfb' : [family_data['sfb']['index'][0]]},
            prefix + '03M1'   : {'sfb' : [family_data['sfb']['index'][1]]},
            prefix + '04M1'   : {'sfb' : [family_data['sfb']['index'][2]]},
            prefix + '05M1'   : {'sfb' : [family_data['sfb']['index'][3]]},
            prefix + '06M1'   : {'sfb' : [family_data['sfb']['index'][4]]},
            prefix + '07M1'   : {'sfb' : [family_data['sfb']['index'][5]]},
            prefix + '08M1'   : {'sfb' : [family_data['sfb']['index'][6]]},
            prefix + '09M1'   : {'sfb' : [family_data['sfb']['index'][7]]},
            prefix + '10M1'   : {'sfb' : [family_data['sfb']['index'][8]]},
            prefix + '11M1'   : {'sfb' : [family_data['sfb']['index'][9]]},
            prefix + '12M1'   : {'sfb' : [family_data['sfb']['index'][10]]},
            prefix + '13M1'   : {'sfb' : [family_data['sfb']['index'][11]]},
            prefix + '14M1'   : {'sfb' : [family_data['sfb']['index'][12]]},
            prefix + '15M1'   : {'sfb' : [family_data['sfb']['index'][13]]},
            prefix + '16M1'   : {'sfb' : [family_data['sfb']['index'][14]]},
            prefix + '17M1'   : {'sfb' : [family_data['sfb']['index'][15]]},
            prefix + '18M1'   : {'sfb' : [family_data['sfb']['index'][16]]},
            prefix + '19M1'   : {'sfb' : [family_data['sfb']['index'][17]]},
            prefix + '20M1'   : {'sfb' : [family_data['sfb']['index'][18]]},
        }
        return sfb_dict

    if family_name.lower() == 'qdb2':
        prefix = 'SIPS-QDB2-'
        qdb2_dict = {
            prefix + '01M1'   : {'qdb2' : [family_data['qdb2']['index'][19]]},
            prefix + '02M1'   : {'qdb2' : [family_data['qdb2']['index'][0]]},
            prefix + '03M1'   : {'qdb2' : [family_data['qdb2']['index'][1]]},
            prefix + '04M1'   : {'qdb2' : [family_data['qdb2']['index'][2]]},
            prefix + '05M1'   : {'qdb2' : [family_data['qdb2']['index'][3]]},
            prefix + '06M1'   : {'qdb2' : [family_data['qdb2']['index'][4]]},
            prefix + '07M1'   : {'qdb2' : [family_data['qdb2']['index'][5]]},
            prefix + '08M1'   : {'qdb2' : [family_data['qdb2']['index'][6]]},
            prefix + '09M1'   : {'qdb2' : [family_data['qdb2']['index'][7]]},
            prefix + '10M1'   : {'qdb2' : [family_data['qdb2']['index'][8]]},
            prefix + '11M1'   : {'qdb2' : [family_data['qdb2']['index'][9]]},
            prefix + '12M1'   : {'qdb2' : [family_data['qdb2']['index'][10]]},
            prefix + '13M1'   : {'qdb2' : [family_data['qdb2']['index'][11]]},
            prefix + '14M1'   : {'qdb2' : [family_data['qdb2']['index'][12]]},
            prefix + '15M1'   : {'qdb2' : [family_data['qdb2']['index'][13]]},
            prefix + '16M1'   : {'qdb2' : [family_data['qdb2']['index'][14]]},
            prefix + '17M1'   : {'qdb2' : [family_data['qdb2']['index'][15]]},
            prefix + '18M1'   : {'qdb2' : [family_data['qdb2']['index'][16]]},
            prefix + '19M1'   : {'qdb2' : [family_data['qdb2']['index'][17]]},
            prefix + '20M1'   : {'qdb2' : [family_data['qdb2']['index'][18]]},
        }
        return qdb2_dict

    else:
        raise Exception('Family name %s not found'%family_name)