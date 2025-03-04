# import sys
# import os

# # This line will add to the python list of paths to look for modules the path to the project root
# MAIN_PARENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# if MAIN_PARENT_PATH not in sys.path:
#     sys.path.append(MAIN_PARENT_PATH)

from translator.parent_translator import ParentTranslator
from translator.gate_translator import GateTranslator

class MainTranslator(ParentTranslator):
    def __init__(self):
        super().__init__()
        self.code_openQASM = []
        
        self.gate_translator = GateTranslator()
        
    def to_openqasm(self, qc):
        translation = ""
        self.start_code_openQASM(qc.get_num_qubits(), qc.get_num_bits())
        
  
        for operation in qc.get_operations():
            match(str(operation["gate"])):
                case "H":
                    self.code_openQASM.append(self.gate_translator.translate_H(operation))
                case "Y":
                    self.code_openQASM.append(self.gate_translator.translate_Y(operation))
                case "X":
                    self.code_openQASM.append(self.gate_translator.translate_X(operation))
                case "Z":
                    self.code_openQASM.append(self.gate_translator.translate_Z(operation))
                # case "R":
                #     gate_translator.translate_R(operation)
                case gate if gate.startswith("U("):
                    self.code_openQASM.append(self.gate_translator.translate_U(operation))
                # case "P":
                #     gate_translator.translate_P(operation)
                # case "XY":
                #     gate_translator.translate_XY(operation)
                case gate if gate.startswith("RY("):
                    self.code_openQASM.append(self.gate_translator.translate_RY(operation))
                case gate if gate.startswith("RX("):
                    self.code_openQASM.append(self.gate_translator.translate_RX(operation))
                case gate if gate.startswith("RZ("):
                    self.code_openQASM.append(self.gate_translator.translate_RZ(operation))
                # case "ZZ":
                #     gate_translator.translate_ZZ(operation)                
                # case "U1":
                #     gate_translator.translate_U1(operation)
                # case "U2":
                #     gate_translator.translate_U2(operation)
                # case "U3":
                #     gate_translator.translate_U3(operation)
                # case "YY":
                #     gate_translator.translate_YY(operation)
                # case "XX":
                #     gate_translator.translate_XX(operation)
                # case "RootPhase":
                #     gate_translator.translate_RoothPhase(operation)
                case "SWAP":
                    self.code_openQASM.append(self.gate_translator.translate_SWAP(operation))
                # case "SqrtSWAP":
                #     gate_translator.translate_SqrtSWAP(operation)
                # case "iSWAP":
                #     gate_translator.translate_iSWAP(operation)
                # case "HalfDeutsch":
                #     gate_translator.translate_HalfDeutsch(operation)
                # case "fSWAP":
                #     gate_translator.translate_fSWAP(operation)
                # case "SqrtX":
                #     gate_translator.translate_SqrtX(operation)
                case "MEASURE":
                    self.code_openQASM.append(self.gate_translator.translate_MEASURE(operation))                    
                # case "BARRIER":
                #     gate_translator.translate_BARRIER(operation)
                case _:
                    continue

        for line in self.code_openQASM:
            translation += line + "\n" 
        return translation

    def start_code_openQASM(self, qbit = 0, cbit = 0):
        self.code_openQASM.append("OPENQASM 3;")
        self.code_openQASM.append('include "stadgates.inc";')    
        self.code_openQASM.append(f"qubit[{qbit}] {self.qbit_reg_name};")
        self.code_openQASM.append(f"bit[{cbit}] {self.cbit_reg_name};")        
       





    