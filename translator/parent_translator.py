
class ParentTranslator:
    custom_R = False
    custom_XX = False
    custom_YY = False
    custom_ZZ = False
    custom_XY = False
    custom_iSWAP = False
    custom_fSWAP = False
    custom_HalfDeutsch = False
    custom_RootPhase = False
    custom_gates = {}

    def __init__(self):
        self.qbit_reg_name = "q"
        self.cbit_reg_name = "c"
        