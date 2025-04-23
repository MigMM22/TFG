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
        
        
        self.gate_translator = GateTranslator(self.code_openQASM)
        
    def to_openqasm(self, qc):
        translation = ""
        self.start_code_openQASM(qc.get_num_qubits(), qc.get_num_bits())
        
  
        for operation in qc.get_operations():
            if(operation == "BARRIER"):
                self.code_openQASM.append(self.gate_translator.translate_BARRIER())  
                continue
            
            match(str(operation["gate"])):
                case "H":
                    self.code_openQASM.append(self.gate_translator.translate_H(operation))
                case "Y":
                    self.code_openQASM.append(self.gate_translator.translate_Y(operation))
                case "X":
                    self.code_openQASM.append(self.gate_translator.translate_X(operation))
                case "Z":
                    self.code_openQASM.append(self.gate_translator.translate_Z(operation))
                # case gate if gate.startswith("R("):
                #     self.code_openQASM.append(self.gate_translator.translate_R(operation))
                case gate if gate.startswith("U("):
                    self.code_openQASM.append(self.gate_translator.translate_U(operation))
                case gate if gate.startswith("P("):
                    self.code_openQASM.append(self.gate_translator.translate_P(operation))
                # case "XY":
                #     gate_translator.translate_XY(operation)
                case gate if gate.startswith("RY("):
                    self.code_openQASM.append(self.gate_translator.translate_RY(operation))
                case gate if gate.startswith("RX("):
                    self.code_openQASM.append(self.gate_translator.translate_RX(operation))
                case gate if gate.startswith("RZ("):
                    self.code_openQASM.append(self.gate_translator.translate_RZ(operation))
                case gate if gate.startswith("ZZ("):
                    self.code_openQASM.append(self.gate_translator.translate_ZZ(operation))                
                case gate if gate.startswith("U1("):
                    self.code_openQASM.append(self.gate_translator.translate_U1(operation))
                case gate if gate.startswith("U2("):
                    self.code_openQASM.append(self.gate_translator.translate_U2(operation))
                case gate if gate.startswith("U3("):
                    self.code_openQASM.append(self.gate_translator.translate_U3(operation))
                case gate if gate.startswith("YY("):
                    self.code_openQASM.append(self.gate_translator.translate_YY(operation))
                case gate if gate.startswith("XX("):
                    self.code_openQASM.append(self.gate_translator.translate_XX(operation))
                # case "RootPhase":
                #     gate_translator.translate_RootPhase(operation)
                case "SWAP":
                    self.code_openQASM.append(self.gate_translator.translate_SWAP(operation))
                case "SqrtSWAP":
                    self.code_openQASM.append(self.gate_translator.translate_SqrtSWAP(operation))
                case "iSWAP":
                    self.code_openQASM.append(self.gate_translator.translate_iSWAP(operation))
                case gate if gate.startswith("HalfDeutsch("):
                    self.code_openQASM.append(self.gate_translator.translate_HalfDeutsch(operation))
                case "fSWAP":
                    self.code_openQASM.append(self.gate_translator.translate_fSWAP(operation))
                case "SqrtX":
                    self.code_openQASM.append(self.gate_translator.translate_SqrtX(operation))
                case "MEASURE":
                    self.code_openQASM.append(self.gate_translator.translate_MEASURE(operation))                     
                case _:
                    custom_gate_translation, custom_call = self.gate_translator.translate_custom_gate(operation)
                    self.code_openQASM.append(custom_gate_translation)
                    # self.code_openQASM.append(custom_call)

        for line in self.code_openQASM:
            translation += line + "\n" 

        ParentTranslator.custom_XX = False
        ParentTranslator.custom_YY = False
        ParentTranslator.custom_ZZ = False
        ParentTranslator.custom_XY = False
        ParentTranslator.custom_iSWAP = False
        ParentTranslator.custom_fSWAP = False
        ParentTranslator.custom_HalfDeutsch = False
        return translation

    def start_code_openQASM(self, qbit = 0, cbit = 0):
        self.code_openQASM.append("OPENQASM 3;")
        self.code_openQASM.append('include "stdgates.inc";')    
        self.code_openQASM.append(f"qubit[{qbit}] {self.qbit_reg_name};")
        self.code_openQASM.append(f"bit[{cbit}] {self.cbit_reg_name};")        
       





    