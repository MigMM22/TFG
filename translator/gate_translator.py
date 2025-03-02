from translator.parent_translator import ParentTranslator
class GateTranslator(ParentTranslator):
    def __init__(self):
        super().__init__()
    
    def translate_H(self, operation):
        target = operation["targets"]
        operation_list = []
        gate_name = "h"
        

        if(len(operation["c_targets"]) > 0):
            operation_list.append[operation["c_targets"]]
        
        if(len(operation["outputs"]) > 0):
            operation_list.append[operation["outputs"]]

        if(len(operation["controls"]) > 0):
            operation_list.append[operation["controls"]]

        if(len(operation["anticontrols"]) > 0):
            operation_list.append[operation["anticontrols"]]

        if(len(operation["c_controls"]) > 0):
            operation_list.append[operation["c_controls"]]

        if(len(operation["c_anticontrols"]) > 0):
            operation_list.append[operation["c_anticontrols"]]

        translation = f"{gate_name} {self.qbit_reg_name}{target};"
        return translation


    def translate_Y(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_X(self, operation): # TODO mejor uso del set(), pasarlo a lista?
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        operation_list = []
        gate_name = "x"

        if(len(c_control) == 1):
            
            c_control_value = c_control.pop()
            translation = f"if({self.cbit_reg_name}[{c_control_value}] == 1) {{ {gate_name} {self.qbit_reg_name}{target}; }}"
            return translation
            
        elif(len(c_control) > 1):
            translation = ""
            c_control = list(c_control)
            for value in c_control:
                translation = translation + f"({self.cbit_reg_name}[{value}] == 1) && "
            
            translation = translation.rstrip(' && ')
            translation = f"if({translation}) {{ {gate_name} {self.qbit_reg_name}{target}; }}"
            return translation

        if(len(c_targets) > 0):
            operation_list.append[c_targets]
        
        if(len(output) > 0):
            operation_list.append[output]

        if(len(control) > 0):
            if(len(control) == 1):
                gate_name = "cx"
            else:
                control = list(control)
                control_value = ""
                for value in control:
                    control_value = f"{self.qbit_reg_name}[{value}], {control_value}"
                    # control_value = "q[" + str(control[value]) + "], " + control_value
                ctrl = f"ctrl({len(control)}) @"
                # ctrl = "ctrl(" + str(len(control)) + ") @ "
                translation = f"{ctrl} {gate_name} {control_value}{self.qbit_reg_name}{target};"
                return translation
                # return ctrl + gate_name + control_value + "q" + str(target) + ";"
            # operation_list.append[control]            

        if(len(anticontrol) > 0):
            gate_name = "x"
            anticontrol = list(anticontrol)
            anticontrol_value = ""
            for value in anticontrol:
                anticontrol_value = f"{self.qbit_reg_name}[{value}], {anticontrol_value}"
            negctrl = f"negctrl({len(anticontrol)}) @"
            translation = f"{negctrl} {gate_name} {anticontrol_value}{self.qbit_reg_name}{target};"
            return translation
           

        
        if(len(c_anticontrol) > 0):
                
            c_anticontrol_value = c_anticontrol.pop()
            translation = f"if({self.cbit_reg_name}[{c_anticontrol_value}] == 0) {{ {gate_name} {self.qbit_reg_name}{target}; }}"
            return translation
            # operation_list.append[c_control]
        elif(len(c_anticontrol) > 1):
            translation = ""
            c_control = list(c_control)
            for value in c_control:
                translation = translation + f"({self.cbit_reg_name}[{value}] == 0) && "
            
            translation = translation.rstrip(' && ')
            translation = f"if({translation}) {{ {gate_name} {self.qbit_reg_name}{target}; }}"
            return translation

        translation = f"{gate_name} {self.qbit_reg_name}{target};"
        return translation

    def translate_Z(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = "z "

        if(len(c_control) > 0):
            c_control_value = c_control.pop()
            
            return "if(" + "c" + "[" + str(c_control_value) + "] == 1) " + "{ " + gate_name + "q" + str(target) + "; }" 
            # operation_list.append[c_control]

    def translate_R(self, operation):
        ptarget = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_U(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_P(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_XY(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_RY(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_RX(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_ZZ(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_RZ(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_U1(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_U2(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_U3(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_YY(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_XX(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_RoothPhase(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_SWAP(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_SqrtSWAP(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_iSWAP(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_HalfDeutsch(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_fSWAP(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_SqrtX(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()

    def translate_MEASURE(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]
        
        translation = ""

        for value in target:
            translation = f"{translation}{self.cbit_reg_name}[{target[value]}] = measure {self.qbit_reg_name}[{output[value]}];\n" 
            # openqasm_code = openqasm_code + "c[" + str(target[value]) + "] = measure q[" +  str(output[value]) + "];\n" 
        
        translation = translation.rstrip('\n')
        return translation
    
    def translate_BARRIER(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()
