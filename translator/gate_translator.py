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

        translation = f"{gate_name} q{target};"
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
        gate_name = "x "

        if(len(c_control) == 1):
            
            c_control_value = c_control.pop()
            
            return "if(" + "c" + "[" + str(c_control_value) + "] == 1) " + "{ " + gate_name + "q" + str(target) + "; }" 
            # operation_list.append[c_control]
        elif(len(c_control) > 1):
            pass

        if(len(c_targets) > 0):
            operation_list.append[c_targets]
        
        if(len(output) > 0):
            operation_list.append[output]

        if(len(control) > 0):
            if(len(control) == 1):
                gate_name = "cx "
            else:
                control = list(control)
                control_value = ""
                for value in control:
                    control_value = "q[" + str(control[value]) + "], " + control_value
                ctrl = "ctrl(" + str(len(control)) + ") @ "
                return ctrl + gate_name + control_value + "q" + str(target) + ";"
            # operation_list.append[control]            

        if(len(anticontrol) > 0):
            anticontrol = list(control)
            anticontrol_value = ""
            for value in anticontrol:
                anticontrol_value = "q[" + str(anticontrol[value]) + "], " + anticontrol_value
            negctrl = "negctrl(" + str(len(anticontrol)) + ") @ "
            return negctrl + gate_name + control_value + "q" + str(target) + ";"
           

        
        if(len(c_anticontrol) > 0):
            operation_list.append[c_anticontrol]

        return gate_name + "q" + str(target) + ";"

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
        
        openqasm_code = ""

        for value in target:
            openqasm_code = openqasm_code + "c[" + str(target[value]) + "] = measure q[" +  str(output[value]) + "];\n" 
        
        openqasm_code = openqasm_code.rstrip('\n')
        return openqasm_code

    def translate_BARRIER(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        self.code_openQASM.append()
