"""Lattice module.

In this module the lattice of the corresponding accelerator is defined.
"""

import math as _math

import lnls as _lnls
import mathphys as _mp
from pyaccel import lattice as _pyacc_lat, elements as _pyacc_ele, \
    accelerator as _pyacc_acc

from . import segmented_models as _segmented_models

default_optics_mode = 'S05.01'
lattice_symmetry = 5
harmonic_number = 864
energy = 3e9  # [eV]


def create_lattice(
        optics_mode=default_optics_mode, simplified=False, ids=None,
        ids_vchamber=True):
    """Return lattice object."""
    # -- selection of optics mode --
    strengths = get_optics_mode(optics_mode=optics_mode)

    # -- shortcut symbols --
    marker = _pyacc_ele.marker
    drift = _pyacc_ele.drift
    sextupole = _pyacc_ele.sextupole
    rfcavity = _pyacc_ele.rfcavity
    corrector = _pyacc_ele.corrector

    # -- lattice markers --
    m_accep_fam_name = 'calc_mom_accep'

    dcircum = 518.3899 - 518.3960

    # -- drifts --
    LIA = drift('lia', 1.5179)
    LIB = drift('lib', 1.0879)
    LIP = drift('lip', 1.0879)
    LPMU = drift('lpmu', 0.0600)
    LPMD = drift('lpmd', 0.4929)
    LID3 = drift('lid3', 1.8679)
    L500p = drift('L500p', 0.5000 + dcircum/5/2)
    LKKp = drift('lkkp', 1.9150 + dcircum/5/2)
    L011 = drift('l011', 0.011)
    L049 = drift('l049', 0.049)
    L052 = drift('l052', 0.052)
    L056 = drift('l056', 0.056)
    L074 = drift('l074', 0.074)
    L075 = drift('l075', 0.075)
    L081 = drift('l081', 0.081)
    L082 = drift('l082', 0.082)
    L090 = drift('l090', 0.090)
    L100 = drift('l100', 0.100)
    L112 = drift('l112', 0.112)
    L119 = drift('l119', 0.119)
    L120 = drift('l120', 0.120)
    L125 = drift('l125', 0.125)
    L127 = drift('l127', 0.127)
    L133 = drift('l133', 0.133)
    L134 = drift('l134', 0.134)
    L135 = drift('l135', 0.135)
    L140 = drift('l140', 0.140)
    L150 = drift('l150', 0.150)
    L170 = drift('l170', 0.170)
    L200 = drift('l200', 0.200)
    L201 = drift('l201', 0.201)
    L205 = drift('l205', 0.205)
    L216 = drift('l216', 0.216)
    L230 = drift('l230', 0.230)
    L237 = drift('l237', 0.237)
    L240 = drift('l240', 0.240)
    L260 = drift('l260', 0.260)
    L325 = drift('l325', 0.325)
    L336 = drift('l336', 0.336)
    L350 = drift('l350', 0.350)
    L419 = drift('l419', 0.419)
    L474 = drift('l474', 0.474)
    L500 = drift('l500', 0.500)
    L600 = drift('l600', 0.600)
    L665 = drift('l665', 0.665)
    L715 = drift('l715', 0.715)

    # -- dipoles --
    BC = _segmented_models.dipole_bc(m_accep_fam_name, simplified)
    B1 = _segmented_models.dipole_b1(m_accep_fam_name, simplified)
    B2 = _segmented_models.dipole_b2(m_accep_fam_name, simplified)

    # -- quadrupoles --
    QFA = _segmented_models.quadrupole_q20('QFA', strengths['QFA'], simplified)
    QDA = _segmented_models.quadrupole_q14('QDA', strengths['QDA'], simplified)
    QDB2 = _segmented_models.quadrupole_q14(
        'QDB2', strengths['QDB2'], simplified)
    QFB = _segmented_models.quadrupole_q30('QFB', strengths['QFB'], simplified)
    QDB1 = _segmented_models.quadrupole_q14(
        'QDB1', strengths['QDB1'], simplified)
    QDP2 = _segmented_models.quadrupole_q14(
        'QDP2', strengths['QDP2'], simplified)
    QFP = _segmented_models.quadrupole_q30('QFP', strengths['QFP'], simplified)
    QDP1 = _segmented_models.quadrupole_q14(
        'QDP1', strengths['QDP1'], simplified)
    Q1 = _segmented_models.quadrupole_q20('Q1', strengths['Q1'], simplified)
    Q2 = _segmented_models.quadrupole_q20('Q2', strengths['Q2'], simplified)
    Q3 = _segmented_models.quadrupole_q20('Q3', strengths['Q3'], simplified)
    Q4 = _segmented_models.quadrupole_q20('Q4', strengths['Q4'], simplified)

    # -- sextupoles --
    SDA0 = sextupole('SDA0', 0.150, strengths['SDA0'])  # CH-CV
    SDB0 = sextupole('SDB0', 0.150, strengths['SDB0'])  # CH-CV
    SDP0 = sextupole('SDP0', 0.150, strengths['SDP0'])  # CH-CV
    SDA1 = sextupole('SDA1', 0.150, strengths['SDA1'])  # QS
    SDB1 = sextupole('SDB1', 0.150, strengths['SDB1'])  # QS
    SDP1 = sextupole('SDP1', 0.150, strengths['SDP1'])  # QS
    SDA2 = sextupole('SDA2', 0.150, strengths['SDA2'])  # CH-CV
    SDB2 = sextupole('SDB2', 0.150, strengths['SDB2'])  # CH-CV
    SDP2 = sextupole('SDP2', 0.150, strengths['SDP2'])  # CH-CV
    SDA3 = sextupole('SDA3', 0.150, strengths['SDA3'])  # --
    SDB3 = sextupole('SDB3', 0.150, strengths['SDB3'])  # --
    SDP3 = sextupole('SDP3', 0.150, strengths['SDP3'])  # --
    SFA0 = sextupole('SFA0', 0.150, strengths['SFA0'])  # CV
    SFB0 = sextupole('SFB0', 0.150, strengths['SFB0'])  # CV
    SFP0 = sextupole('SFP0', 0.150, strengths['SFP0'])  # CV
    SFA1 = sextupole('SFA1', 0.150, strengths['SFA1'])  # QS
    SFB1 = sextupole('SFB1', 0.150, strengths['SFB1'])  # QS
    SFP1 = sextupole('SFP1', 0.150, strengths['SFP1'])  # QS
    SFA2 = sextupole('SFA2', 0.150, strengths['SFA2'])  # CH
    SFB2 = sextupole('SFB2', 0.150, strengths['SFB2'])  # CH-CV
    SFP2 = sextupole('SFP2', 0.150, strengths['SFP2'])  # CH-CV

    # -- slow vertical corrector --
    CV = sextupole('CV', 0.150, 0.0)  # same model as BO correctors

    # -- pulsed magnets --
    InjDpKckr = sextupole('InjDpKckr', 0.400, S=0.0)  # injection kicker
    InjNLKckr = sextupole('InjNLKckr', 0.450, S=0.0)  # pulsed multipole magnet
    PingV = marker('PingV')  # Vertical Pinger

    # -- fast correctors --
    # 60 magnets: normal quad poles (CH+CV and CH+CV+QS):
    FC1 = sextupole('FC1', 0.084, S=0.0)
    # 20 magnets: skew quad poles (CH+CV and CH+CV+QS):
    FC2 = sextupole('FC2', 0.082, S=0.0)

    # -- rf cavities --
    RFC = rfcavity('SRFCav', 0, 3.0e6, 500e6)
    HCav = marker('H3Cav')

    # -- lattice markers --
    START = marker('start')  # start of the model
    END = marker('end')  # end of the model
    MIA = marker('mia')  # center of long straight sections (even-numbered)
    MIB = marker('mib')  # center of short straight sections (odd-numbered)
    MIP = marker('mip')  # center of short straight sections (odd-numbered)
    # marker used to delimitate girders.
    # one marker at begin and another at end of girder:
    GIR = marker('girder')
    # marker for the extremities of IDs in long straight sections
    MIDA = marker('id_enda')
    # marker for the extremities of IDs in short straight sections
    MIDB = marker('id_endb')
    # marker for the extremities of IDs in short straight sections
    MIDP = marker('id_endp')
    # end of injection septum
    InjSeptF = marker('InjSeptF')

    # --- diagnostic components ---
    BPM = marker('BPM')
    DCCT = marker('DCCT')  # dcct to measure beam current
    ScrapH = marker('ScrapH')  # horizontal scraper
    ScrapV = marker('ScrapV')  # vertical scraper
    GSL15 = marker('GSL15')  # Generic Stripline (lambda/4)
    GSL07 = marker('GSL07')  # Generic Stripline (lambda/8)
    GBPM = marker('GBPM')  # General BPM
    BbBPkup = marker('BbBPkup')  # Bunch-by-Bunch Pickup
    BbBKckrH = marker('BbBKckrH')  # Horizontal Bunch-by-Bunch Shaker
    BbBKckrV = marker('BbBKckrV')  # Vertical Bunch-by-Bunch Shaker
    BbBKckL = marker('BbBKckrL')  # Longitudinal Bunch-by-Bunch Shaker
    TuneShkrH = marker('TuneShkrH')  # Horizontal Tune Shaker
    TuneShkrV = marker('TuneShkrV')  # Vertical Tune Shaker
    TunePkup = marker('TunePkup')  # Tune Pickup

    # --- insertion devices (half devices) ---
    kickmaps = create_id_kickmaps_dict(ids)
    ID06H = kickmaps['ID06SB']  # CARNAUBA  'SI-06SB:ID-APU22'
    ID07H = kickmaps['ID07SP']  # CATERETE  'SI-07SP:ID-APU22'
    ID08H = kickmaps['ID08SB']  # EMA       'SI-08SB:ID-APU22'
    ID09H = kickmaps['ID09SA']  # MANACA    'SI-09SA:ID-APU22'
    ID10H = kickmaps['ID10SB']  # SABIA     'SI-10SB:ID-Delta52'
    ID11H = kickmaps['ID11SP']  # IPE       'SI-11SP:ID-APU58'

    IDC = sextupole('IDC', 0.1, S=0)  # ID corrector

    # -- sectors --
    M1A = [
        L134, QDA, L150, SDA0, GIR, L074, GIR, FC1, L082, QFA, L150, SFA0,
        L135, BPM, GIR]  # high beta xxM1 girder (with fasc corrector)
    M1B = [
        L134, QDB1, L150, SDB0, GIR, L240, GIR, QFB, L150, SFB0, L049, FC1,
        L052, QDB2, L140, BPM, GIR]  # low beta xxM1 girder
    M1P = [
        L134, QDP1, L150, SDP0, GIR, L240, GIR, QFP, L150, SFP0, L049, FC1,
        L052, QDP2, L140, BPM, GIR]  # low beta xxM1 girder
    M2A = M1A[::-1]  # high beta xxM2 girder (with fast correctors)
    M2B = M1B[::-1]  # low beta xxM2 girder
    M2P = M1P[::-1]  # low beta xxM2 girder

    M1B_BbBPkup = [
        L134, QDB1, L150, SDB0, GIR, L120, BbBPkup, L120, GIR, QFB, L150, SFB0,
        L049, FC1, L052, QDB2, L140, BPM, GIR]

    # arc sector in between B1-B2 (high beta odd-numbered straight sections):
    C1A = [
        GIR, L474, GIR, SDA1, L170, Q1, L135, BPM, L125, SFA1, L230, Q2, L170,
        SDA2, GIR, L205, GIR, BPM, L011]
    # arc sector in between B1-B2 (low beta  even-numbered straight sections):
    C1B = [
        GIR, L474, GIR, SDB1, L170, Q1, L135, BPM, L125, SFB1, L230, Q2,
        L170, SDB2, GIR, L205, GIR, BPM, L011]
    # arc sector in between B1-B2 (low beta even-numbered straight sections):
    C1P = [
        GIR, L474, GIR, SDP1, L170, Q1, L135, BPM, L125, SFP1, L230, Q2, L170,
        SDP2, GIR, L205, GIR, BPM, L011]

    # arc sector in between B2-BC (high beta odd-numbered straight sections):
    C2A = [
        GIR, L336, GIR, SDA3, L170, Q3, L230, SFA2, L260, Q4, L200, CV, GIR,
        L201, GIR, FC2, L119, BPM, L075]
    # arc sector in between B2-BC (low beta even-numbered straight sections):
    C2B = [
        GIR, L336, GIR, SDB3, L170, Q3, L230, SFB2, L260, Q4, L200, CV, GIR,
        L201, GIR, FC2, L119, BPM, L075]
    # arc sector in between B2-BC (low beta even-numbered straight sections):
    C2P = [
        GIR, L336, GIR, SDP3, L170, Q3, L230, SFP2, L260, Q4, L200, CV, GIR,
        L201, GIR, FC2, L119, BPM, L075]

    # arc sector in between BC-B2 (high beta odd-numbered straight sections):
    C3A = [
        GIR, L715, GIR, L112, Q4, L133, BPM, L127, SFA2, L056, FC1, L090, Q3,
        L170, SDA3, GIR, L325, GIR, BPM, L011]
    # arc sector in between BC-B2 (low beta even-numbered straight sections):
    C3B = [
        GIR, L715, GIR, L112, Q4, L133, BPM, L127, SFB2, L056, FC1, L090, Q3,
        L170, SDB3, GIR, L325, GIR, BPM, L011]
    # arc sector in between BC-B2 (low beta even-numbered straight sections):
    C3P = [
        GIR, L715, GIR, L112, Q4, L133, BPM, L127, SFP2, L056, FC1, L090, Q3,
        L170, SDP3, GIR, L325, GIR, BPM, L011]

    # arc sector in between B2-B1 (high beta odd-numbered straight sections):
    C4A = [
        GIR, L216, GIR, SDA2, L170, Q2, L230, SFA1, L125, BPM, L135, Q1, L170,
        SDA1, GIR, L474, GIR]
    # arc sector in between B2-B1 (high beta odd-numbered straight sections):
    C4A_BbBKckrV = [
        GIR, L216, GIR, SDA2, L170, Q2, L230, SFA1, L125, BPM, L135, Q1, L170,
        SDA1, L237, BbBKckrV, GIR, L237, GIR]

    # arc sector in between B2-B1 (low beta even-numbered straight sections):
    C4B = [
        GIR, L216, GIR, SDB2, L170, Q2, L230, SFB1, L125, BPM, L135, Q1, L170,
        SDB1, GIR, L474, GIR]
    # arc sector in between B2-B1 (low beta even-numbered straight sections):
    C4B_GBPM = [
        GIR, L216, GIR, SDB2, L170, Q2, L230, SFB1, L125, BPM, L135, Q1, L170,
        SDB1, GBPM, GIR, L474, GIR]
    # arc sector in between B2-B1 (low beta even-numbered straight sections):
    C4B_DCCT = [
        GIR, L216, GIR, SDB2, L170, Q2, L230, SFB1, L125, BPM, L135, Q1, L170,
        SDB1, L237, DCCT, GIR, L237, GIR]
    # arc sector in between B2-B1 (low beta even-numbered straight sections):
    C4B_TunePkup = [
        GIR, L216, GIR, SDB2, L170, Q2, L230, SFB1, L125, BPM, L135, Q1, L170,
        SDB1, L237, TunePkup, GIR, L237, GIR]
    # arc sector in between B2-B1 (low beta even-numbered straight sections)
    C4B_PingV = [
        GIR, L216, GIR, SDB2, L170, Q2, L230, SFB1, L125, BPM, L135, Q1, L170,
        SDB1, L237, PingV, GIR, L237, GIR]

    # arc sector in between B2-B1 (low beta even-numbered straight sections):
    C4P = [
        GIR, L216, GIR, SDP2, L170, Q2, L230, SFP1, L125, BPM, L135, Q1, L170,
        SDP1, GIR, L474, GIR]
    # arc sector in between B2-B1 (low beta even-numbered straight sections):
    C4P_DCCT = [
        GIR, L216, GIR, SDP2, L170, Q2, L230, SFP1, L125, BPM, L135, Q1, L170,
        SDP1, L237, DCCT, GIR, L237, GIR]
    # arc sector in between B2-B1 (low beta even-numbered straight sections):
    C4P_TuneShkrV = [
        GIR, L216, GIR, SDP2, L170, Q2, L230, SFP1, L125, BPM, L135, Q1, L170,
        SDP1, L237, TuneShkrV, GIR, L237, GIR]

    # --- IDA insertion sectors ---

    IDA_INJ = [
        L500, TuneShkrH, LIA, L419, InjSeptF, L081, L500, L500p, END, START,
        MIA, LKKp, InjDpKckr, LPMU, ScrapV, L100, ScrapV, L100,
        InjNLKckr, LPMD]  # high beta INJ straight section and Scrapers

    IDA_BbBKckrH = [
        L500, BbBKckrH, LIA, L500, MIDA, L500, L500p, MIA, L500p, L500, MIDA,
        L500, LIA, L500]  # high beta ID straight section

    IDA_ScrapH = [
        L500, LIA, L500, MIDA, L500, L500p, MIA, L500p, L500, MIDA, L500,
        ScrapH, LIA, L500]  # high beta ID straight section

    IDA_09 = [
        L500, LID3, L500p,
        MIDA, ID09H, MIA, ID09H, MIDA,
        L500p, LID3, L500]  # high beta ID straight section (MANACA)

    IDA_17 = [
        L500, LIA, L500,
        MIDA, L500, L500p, MIA, L500p, L500, MIDA,
        L500, BbBKckrH, LIA, L500]  # high beta ID straight section (SAPUCAIA)

    # --- IDB insertion sectors ---

    IDB = [
        L500, LIB, L500, MIDB, L500, L500, MIB, L500, L500, MIDB, L500, LIB,
        L500]  # low beta ID straight section

    IDB_GSL07 = [
        L500, GSL07, LIB, L500,
        MIDB, L500, L500, MIB, L500, L500, MIDB,
        L500, LIB, L500]  # low beta ID straight section

    IDB_TunePkup = [
        L500, LIB, L500,
        MIDB, L500, L500, MIB, L500, L500, MIDB,
        L500, TunePkup, LIB, L500]  # low beta ID straight section

    IDB_02 = [
        L500, LIB, L500,
        MIDB, L500, L500, MIB, L500, L500, MIDB,
        L500, HCav, LIB, L500]  # low beta ID straight section

    IDB_06 = [
        L500, LIB, L500,
        L350, MIDB, ID06H, MIB, ID06H, MIDB,
        L350, L500, LIB, L500]  # low beta ID straight section (CARNAUBA)

    IDB_08 = [
        L500, LIB, L500, L350,
        MIDB, ID08H, MIB, ID08H, MIDB,
        L350, L500, LIB, L500]  # low beta ID straight section (EMA)

    IDB_10 = [
        L500, LIB, L665, IDC, L135,
        MIDB, ID10H, MIB, ID10H, MIDB,
        L135, IDC, L665, LIB, L500]  # low beta ID straight section (SABIA)

    IDB_12 = [
        L500, LIB, L665, L100, L135,
        MIDB, L600, MIB, L600, MIDB,
        L135, L100, L665, LIB, L500]  # low beta ID straight section

    IDB_16 = [
        L500, LIB, L500,
        MIDB, L500, L500, MIB, L500, L500, MIDB,
        L500, BbBKckL, LIB, L500]  # low beta ID straight section

    # --- IDP insertion sectors ---

    IDP = [
        L500, LIP, L500,
        MIDP, L500, L500, MIP, L500, L500, MIDP,
        L500, LIP, L500]  # low beta ID straight section

    IDP_CAV = [
        L500, LIP, L500, L500, L500, MIP, RFC, L500, L500, L500,
        LIP, L500]  # low beta RF cavity straight section

    IDP_07 = [
        L500, LIP, L500, L350,
        MIDP, ID07H, MIP, ID07H, MIDP,
        L350, L500, LIP, L500]  # low beta ID straight section (CATERETE)

    IDP_11 = [
        L500, LIP, L500, L350,
        MIDP, ID11H, MIP, ID11H, MIDP,
        L350, L500, LIP, L500]  # low beta ID straight section (IPE)

    IDP_GSL15 = [
        L500, GSL15, LIP, L500,
        MIDP, L500, L500, MIP, L500, L500, MIDP,
        L500, LIP, L500]  # low beta ID straight section

    # -- girders --

    # straight sections
    SS_S01 = IDA_INJ  # INJECTION
    SS_S02 = IDB_02
    SS_S03 = IDP_CAV
    SS_S04 = IDB
    SS_S05 = IDA_ScrapH
    SS_S06 = IDB_06  # CARNAUBA
    SS_S07 = IDP_07  # CATERETE
    SS_S08 = IDB_08  # EMA
    SS_S09 = IDA_09  # MANACA
    SS_S10 = IDB_10  # SABIA
    SS_S11 = IDP_11  # IPE
    SS_S12 = IDB_12
    SS_S13 = IDA_BbBKckrH
    SS_S14 = IDB  # PAINEIRA
    SS_S15 = IDP
    SS_S16 = IDB_16  # INGA
    SS_S17 = IDA_17  # SAPUCAIA
    SS_S18 = IDB_TunePkup
    SS_S19 = IDP_GSL15
    SS_S20 = IDB_GSL07

    # down and upstream straight sections
    M1_S01 = M1A
    M2_S01 = M2A
    M1_S02 = M1B
    M2_S02 = M2B
    M1_S03 = M1P
    M2_S03 = M2P
    M1_S04 = M1B
    M2_S04 = M2B
    M1_S05 = M1A
    M2_S05 = M2A
    M1_S06 = M1B
    M2_S06 = M2B
    M1_S07 = M1P
    M2_S07 = M2P
    M1_S08 = M1B
    M2_S08 = M2B
    M1_S09 = M1A
    M2_S09 = M2A
    M1_S10 = M1B
    M2_S10 = M2B
    M1_S11 = M1P
    M2_S11 = M2P
    M1_S12 = M1B_BbBPkup
    M2_S12 = M2B
    M1_S13 = M1A
    M2_S13 = M2A
    M1_S14 = M1B
    M2_S14 = M2B
    M1_S15 = M1P
    M2_S15 = M2P
    M1_S16 = M1B
    M2_S16 = M2B
    M1_S17 = M1A
    M2_S17 = M2A
    M1_S18 = M1B
    M2_S18 = M2B
    M1_S19 = M1P
    M2_S19 = M2P
    M1_S20 = M1B
    M2_S20 = M2B

    # dispersive arcs
    C1_S01 = C1A
    C2_S01 = C2A
    C3_S01 = C3B
    C4_S01 = C4B
    C1_S02 = C1B
    C2_S02 = C2B
    C3_S02 = C3P
    C4_S02 = C4P
    C1_S03 = C1P
    C2_S03 = C2P
    C3_S03 = C3B
    C4_S03 = C4B
    C1_S04 = C1B
    C2_S04 = C2B
    C3_S04 = C3A
    C4_S04 = C4A
    C1_S05 = C1A
    C2_S05 = C2A
    C3_S05 = C3B
    C4_S05 = C4B
    C1_S06 = C1B
    C2_S06 = C2B
    C3_S06 = C3P
    C4_S06 = C4P
    C1_S07 = C1P
    C2_S07 = C2P
    C3_S07 = C3B
    C4_S07 = C4B
    C1_S08 = C1B
    C2_S08 = C2B
    C3_S08 = C3A
    C4_S08 = C4A
    C1_S09 = C1A
    C2_S09 = C2A
    C3_S09 = C3B
    C4_S09 = C4B
    C1_S10 = C1B
    C2_S10 = C2B
    C3_S10 = C3P
    C4_S10 = C4P
    C1_S11 = C1P
    C2_S11 = C2P
    C3_S11 = C3B
    C4_S11 = C4B
    C1_S12 = C1B
    C2_S12 = C2B
    C3_S12 = C3A
    C4_S12 = C4A
    C1_S13 = C1A
    C2_S13 = C2A
    C3_S13 = C3B
    C4_S13 = C4B_DCCT
    C1_S14 = C1B
    C2_S14 = C2B
    C3_S14 = C3P
    C4_S14 = C4P_DCCT
    C1_S15 = C1P
    C2_S15 = C2P
    C3_S15 = C3B
    C4_S15 = C4B_GBPM
    C1_S16 = C1B
    C2_S16 = C2B
    C3_S16 = C3A
    C4_S16 = C4A_BbBKckrV
    C1_S17 = C1A
    C2_S17 = C2A
    C3_S17 = C3B
    C4_S17 = C4B_TunePkup
    C1_S18 = C1B
    C2_S18 = C2B
    C3_S18 = C3P
    C4_S18 = C4P_TuneShkrV
    C1_S19 = C1P
    C2_S19 = C2P
    C3_S19 = C3B
    C4_S19 = C4B_PingV
    C1_S20 = C1B
    C2_S20 = C2B
    C3_S20 = C3A
    C4_S20 = C4A

    # SECTORS # 01..20
    S01 = [
        M1_S01, SS_S01, M2_S01, B1, C1_S01, B2, C2_S01, BC,
        C3_S01, B2, C4_S01, B1]
    S02 = [
        M1_S02, SS_S02, M2_S02, B1, C1_S02, B2, C2_S02, BC,
        C3_S02, B2, C4_S02, B1]
    S03 = [
        M1_S03, SS_S03, M2_S03, B1, C1_S03, B2, C2_S03, BC,
        C3_S03, B2, C4_S03, B1]
    S04 = [
        M1_S04, SS_S04, M2_S04, B1, C1_S04, B2, C2_S04, BC,
        C3_S04, B2, C4_S04, B1]
    S05 = [
        M1_S05, SS_S05, M2_S05, B1, C1_S05, B2, C2_S05, BC,
        C3_S05, B2, C4_S05, B1]
    S06 = [
        M1_S06, SS_S06, M2_S06, B1, C1_S06, B2, C2_S06, BC,
        C3_S06, B2, C4_S06, B1]
    S07 = [
        M1_S07, SS_S07, M2_S07, B1, C1_S07, B2, C2_S07, BC,
        C3_S07, B2, C4_S07, B1]
    S08 = [
        M1_S08, SS_S08, M2_S08, B1, C1_S08, B2, C2_S08, BC,
        C3_S08, B2, C4_S08, B1]
    S09 = [
        M1_S09, SS_S09, M2_S09, B1, C1_S09, B2, C2_S09, BC,
        C3_S09, B2, C4_S09, B1]
    S10 = [
        M1_S10, SS_S10, M2_S10, B1, C1_S10, B2, C2_S10, BC,
        C3_S10, B2, C4_S10, B1]
    S11 = [
        M1_S11, SS_S11, M2_S11, B1, C1_S11, B2, C2_S11, BC,
        C3_S11, B2, C4_S11, B1]
    S12 = [
        M1_S12, SS_S12, M2_S12, B1, C1_S12, B2, C2_S12, BC,
        C3_S12, B2, C4_S12, B1]
    S13 = [
        M1_S13, SS_S13, M2_S13, B1, C1_S13, B2, C2_S13, BC,
        C3_S13, B2, C4_S13, B1]
    S14 = [
        M1_S14, SS_S14, M2_S14, B1, C1_S14, B2, C2_S14, BC,
        C3_S14, B2, C4_S14, B1]
    S15 = [
        M1_S15, SS_S15, M2_S15, B1, C1_S15, B2, C2_S15, BC,
        C3_S15, B2, C4_S15, B1]
    S16 = [
        M1_S16, SS_S16, M2_S16, B1, C1_S16, B2, C2_S16, BC,
        C3_S16, B2, C4_S16, B1]
    S17 = [
        M1_S17, SS_S17, M2_S17, B1, C1_S17, B2, C2_S17, BC,
        C3_S17, B2, C4_S17, B1]
    S18 = [
        M1_S18, SS_S18, M2_S18, B1, C1_S18, B2, C2_S18, BC,
        C3_S18, B2, C4_S18, B1]
    S19 = [
        M1_S19, SS_S19, M2_S19, B1, C1_S19, B2, C2_S19, BC,
        C3_S19, B2, C4_S19, B1]
    S20 = [
        M1_S20, SS_S20, M2_S20, B1, C1_S20, B2, C2_S20, BC,
        C3_S20, B2, C4_S20, B1]

    anel = [S01, S02, S03, S04, S05, S06, S07, S08, S09, S10,
            S11, S12, S13, S14, S15, S16, S17, S18, S19, S20]
    anel = _lnls.utils.flatten(anel)

    the_ring = _pyacc_lat.build(anel)

    # -- shifts model to marker 'start'
    idx = _pyacc_lat.find_indices(the_ring, 'fam_name', 'start')
    the_ring = _pyacc_lat.shift(the_ring, idx[0])

    # -- sets rf frequency
    set_rf_frequency(the_ring)

    # -- sets number of integration steps
    set_num_integ_steps(the_ring)

    # -- define vacuum chamber for all elements
    set_vacuum_chamber(the_ring, ids_vchamber=ids_vchamber)

    return the_ring


def set_rf_frequency(the_ring):
    """Set RF frequency of the lattice."""
    circumference = _pyacc_lat.length(the_ring)
    # _, beam_velocity, _, _, _ = _mp.beam_optics.beam_rigidity(energy=energy)
    # velocity = beam_velocity
    velocity = _mp.constants.light_speed
    rev_frequency = velocity / circumference
    rf_frequency = harmonic_number * rev_frequency
    idx = _pyacc_lat.find_indices(the_ring, 'fam_name', 'SRFCav')
    for i in idx:
        the_ring[i].frequency = rf_frequency


def set_num_integ_steps(the_ring):
    """Set number of integration steps in each lattice element."""
    len_bends = 0.050
    len_quads = 0.015
    len_sexts = 0.015
    for i in range(len(the_ring)):
        if the_ring[i].angle:
            nr_steps = int(_math.ceil(the_ring[i].length/len_bends))
            the_ring[i].nr_steps = nr_steps
        elif the_ring[i].polynom_b[2]:
            nr_steps = int(_math.ceil(the_ring[i].length/len_sexts))
            the_ring[i].nr_steps = nr_steps
        elif the_ring[i].polynom_b[1] or the_ring[i].fam_name in \
                ['FC1', 'FC2', 'InjDpKckr', 'InjNLKckr']:
            nr_steps = int(_math.ceil(the_ring[i].length/len_quads))
            the_ring[i].nr_steps = nr_steps


def set_vacuum_chamber(
        the_ring, optics_mode=default_optics_mode, ids_vchamber=True):
    """Set vacuum chamber for all elements."""
    # vchamber = [hmin, hmax, vmin, vmax] (meter)
    other_vchamber = [-0.012, 0.012, -0.012, 0.012]
    bc_hfield_vchamber = [-0.004, 0.004, -0.004, 0.004]
    inj_vchamber = [-0.030, 0.012, -0.012, 0.012]

    ida_vchamber = [-0.012, 0.012, -0.004, 0.004]
    idb_vchamber = [-0.004, 0.004, -0.00225, 0.00225]
    idp_vchamber = ida_vchamber
    if optics_mode.startswith('S05'):
        idp_vchamber = idb_vchamber

    # Set ordinary Vacuum Chamber
    for i in range(len(the_ring)):
        e = the_ring[i]
        e.hmin, e.hmax, e.vmin, e.vmax = other_vchamber

    # Set injection vacuum chamber
    sept_in = _pyacc_lat.find_indices(the_ring, 'fam_name', 'InjSeptF')[-1]
    kick_in = _pyacc_lat.find_indices(the_ring, 'fam_name', 'InjDpKckr')[0]
    inj_list = list(range(sept_in, len(the_ring))) + list(range(kick_in+1))
    for i in inj_list:
        e = the_ring[i]
        e.hmin, e.hmax, e.vmin, e.vmax = inj_vchamber

    # Set high field BC vacuum chamber
    # NOTE: segments with bending radius smaller than this value
    # are supposed to have reduced vacuum chamber. This should be
    # replaced by specification of the vacuum chamber
    rho0 = 5.0  # [m]
    indices = _pyacc_lat.find_indices(the_ring, 'fam_name', 'BC')
    for i in indices:
        e = the_ring[i]
        ang, lng = e.angle, e.length
        rho = lng/ang
        if rho < rho0:
            e.hmin, e.hmax, e.vmin, e.vmax = bc_hfield_vchamber
    indices = _pyacc_lat.find_indices(the_ring, 'fam_name', 'mc')
    for i in indices:
        e = the_ring[i]
        e.hmin, e.hmax, e.vmin, e.vmax = bc_hfield_vchamber
        e = the_ring[i + 1]
        e.hmin, e.hmax, e.vmin, e.vmax = bc_hfield_vchamber

    if not ids_vchamber:
        return

    # Set ids vacuum chamber in straight section of type B
    idb = _pyacc_lat.find_indices(the_ring, 'fam_name', 'id_endb')
    idb_list = []
    for i in range(len(idb)//2):
        idb_list.extend(range(idb[2*i], idb[2*i+1]+1))
    for i in idb_list:
        e = the_ring[i]
        e.hmin, e.hmax, e.vmin, e.vmax = idb_vchamber

    # Set ids vacuum chamber in straight section of type A
    ida = _pyacc_lat.find_indices(the_ring, 'fam_name', 'id_enda')
    ida_list = []
    for i in range(len(ida)//2):
        ida_list.extend(range(ida[2*i], ida[2*i+1]+1))
    for i in ida_list:
        e = the_ring[i]
        e.hmin, e.hmax, e.vmin, e.vmax = ida_vchamber

    # Set ids vacuum chamber in straight section of type P
    idp = _pyacc_lat.find_indices(the_ring, 'fam_name', 'id_endp')
    idp_list = []
    for i in range(len(idp)//2):
        idp_list.extend(range(idp[2*i], idp[2*i+1]+1))
    for i in idp_list:
        e = the_ring[i]
        e.hmin, e.hmax, e.vmin, e.vmax = idp_vchamber


def get_optics_mode(optics_mode=default_optics_mode):
    """Return magnet strengths for a given optics mode."""
    mode, version = optics_mode.split('.')

    if mode == 'S05':
        if version == '01':
            strengths = {
                #  QUADRUPOLES
                #  ===========
                'Q1': +2.818370601288,
                'Q2': +4.340329381668,
                'Q3': +3.218430939674,
                'Q4': +3.950686823494,

                # NOTE: these values need updating after optics
                # resimetrization with MAD
                'QDA': -1.619540412181686,
                'QFA': +3.5731777226094446,
                'QFB': +4.115082809275146,
                'QFP': +4.115082809275146,
                'QDB1': -2.00677456404202,
                'QDB2': -3.420574744932221,
                'QDP1': -2.00677456404202,
                'QDP2': -3.420574744932221,

                #  SEXTUPOLES
                #  ===========
                'SDA0': -80.8337,
                'SDB0': -64.9422,
                'SDP0': -64.9422,
                'SFA0': +52.5696,
                'SFB0': +73.7401,
                'SFP0': +73.7401,

                'SDA1': -163.0062328090773,
                'SDA2': -88.88255991288263,
                'SDA3': -139.94153649641189,
                'SFA1': +191.76738248436368,
                'SFA2': +150.74610044115283,
                'SDB1': -141.68687364847958,
                'SDB2': -122.31573949946443,
                'SDB3': -173.8347917755106,
                'SFB1': +227.7404567527413,
                'SFB2': +197.7495405020359,
                'SDP1': -142.31415019209263,
                'SDP2': -122.28457189976633,
                'SDP3': -174.1745194336169,
                'SFP1': +229.17648360831797,
                'SFP2': +198.4525009917773,
            }
        else:
            raise _pyacc_acc.AcceleratorException('Version not Implemented')
    else:
        raise _pyacc_acc.AcceleratorException('Mode not Implemented.')

    return strengths


def create_id_kickmaps_dict(ids):
    """Return dict with half insertion device kickmaps."""
    drift = _pyacc_ele.drift

    idsdict = dict()
    if ids:
        idsdict = {id.subsec: id for id in ids}

    # NOTE: see IDs already defined in
    # https://wiki-sirius.lnls.br/mediawiki/index.php/Machine:Insertion_Devices
    ids_subsec_drift_lens = {
        # subsec   idtype   idlen    beamline
        'ID06SB': ('APU22', 1.3),    # CARNAUBA
        'ID07SP': ('APU22', 1.3),    # CATERETE
        'ID08SB': ('APU22', 1.3),    # EMA
        'ID09SA': ('APU22', 1.3),    # MANACA
        'ID10SB': ('DELTA52', 1.2),  # SABIA
        'ID11SP': ('APU58', 1.3),    # IPE
    }

    # build kickmap dict
    kickmaps = dict()
    for subsec, (idtype, idlen) in ids_subsec_drift_lens.items():
        if subsec not in idsdict:
            # ID not in passed ID dictionary, return drift for half ID.
            kickmaps[subsec] = drift(idtype, idlen/2)
        else:
            # return Kickmap for half ID.
            kickmaps[subsec] = idsdict[subsec].get_half_kickmap()

    return kickmaps
