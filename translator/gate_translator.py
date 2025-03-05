from translator.parent_translator import ParentTranslator
class GateTranslator(ParentTranslator):
    def __init__(self):
        super().__init__()

    def translate(self, gate_name, target, control, anticontrol, c_control, c_anticontrol):
        c_translation = ""
        end_translation = ""
        translation = ""        
        q_translation = ""
        ctrls_amount = 0
        antictrls_amount = 0

        for qbit in control:
            q_translation += f"{self.qbit_reg_name}[{qbit}], "
            ctrls_amount += 1

        for qbit in anticontrol:
            q_translation += f"{self.qbit_reg_name}[{qbit}], "
            antictrls_amount += 1
        
        q_translation = f"{gate_name} {q_translation}"
        q_translation += f"{self.qbit_reg_name}{target};"

        if(antictrls_amount > 0):
            q_translation = f"negctrl({antictrls_amount}) @ " + q_translation
        
        if(ctrls_amount > 0):
            q_translation = f"ctrl({ctrls_amount}) @ " + q_translation
                
        c_translation = ""
                
        for cbit in c_control: 
            c_translation +=  f"({self.cbit_reg_name}[{cbit}] == 1) && "
        for cbit in c_anticontrol:
            c_translation += f"({self.cbit_reg_name}[{cbit}] == 0) && " 
        c_translation = c_translation.rstrip(' && ')

        if len(c_translation) > 0:
            end_translation = "}"
            c_translation = f"if({c_translation}) {{ "
                  
            
        translation =  f"{c_translation}{q_translation} {end_translation}"   
        return translation

    def translate_H(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = "h"
        
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol)   
        return translation

    def translate_Y(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = "y"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol)  
        return translation

    def translate_X(self, operation): 
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]
        
        gate_name = "x"

        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol)   
        return translation
          
    def translate_Z(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = "z"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol)  
        return translation

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

        angles = str(operation["gate"]).replace("U(", "").replace(")", "")
        # angles_part will now be "45,60,90"

        # 2. Split the string by the comma "," delimiter:
        angle_strings = angles.split(',')
        # angle_strings will be a list: ['45', '60', '90']

        # 3. Convert each angle string to an integer (or float if needed):
        
        gate_name = f"U({angle_strings[0]}, {angle_strings[1]}, {angle_strings[2]})"
        
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol)  
        return translation     

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

        angle = str(operation["gate"]).replace("RX(", "").replace(")", "")

        gate_name = f"ry({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol)   
        return translation

    def translate_RX(self, operation):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angle = str(operation["gate"]).replace("RX(", "").replace(")", "")

        gate_name = f"rx({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol) 
        return translation

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

        angle = str(operation["gate"]).replace("RX(", "").replace(")", "")

        gate_name = f"rz({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol)  
        return translation

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

        gate_name = f"swap"
        target = f"{self.qbit_reg_name}[{target[0]}], {self.qbit_reg_name}[{target[1]}]"
        q_translation = f"{gate_name} {target};"
        c_translation = ""
        end_translation = ""
        translation = ""  

        if((len(control) > 0) | (len(anticontrol) > 0)):
            q_translation = ""
            control_value = ""
            ctrl = ""
            anticontrol_value = ""
            negctrl = ""

            if(len(control) > 0):            
                control = list(control)
                for value in control:
                    control_value = f"{self.qbit_reg_name}[{value}], {control_value}"               
                ctrl = f"ctrl({len(control)}) @ "
               
            if(len(anticontrol) > 0):
                anticontrol = list(anticontrol)
                for value in anticontrol:
                    anticontrol_value = f"{self.qbit_reg_name}[{value}], {anticontrol_value}"
                negctrl = f"negctrl({len(anticontrol)}) @ "
                # translation = f"{negctrl} {gate_name} {anticontrol_value}{self.qbit_reg_name}{target};"
            
            q_translation = f"{negctrl}{ctrl}{gate_name} {anticontrol_value}{control_value}{target};"
            # return q_translation

        if((len(c_control) > 0) | (len(c_anticontrol) > 0)):
            c_control_translation = ""
            c_anticontrol_translation = ""

            if(len(c_control) == 1):            
                c_control_value = c_control.pop()
                c_control_translation = f"({self.cbit_reg_name}[{c_control_value}] == 1)"
                
            elif(len(c_control) > 1):                
                c_control = list(c_control)
                for value in c_control:
                    c_control_translation = c_control_translation + f"({self.cbit_reg_name}[{value}] == 1) && "                
                c_control_translation = c_control_translation.rstrip(' && ')
                c_control_translation = f"({c_control_translation})"
            
            if(len(c_anticontrol) == 1):                    
                c_anticontrol_value = c_anticontrol.pop()
                c_anticontrol_translation = f"({self.cbit_reg_name}[{c_anticontrol_value}] == 0)" 

            elif(len(c_anticontrol) > 1):                
                c_control = list(c_control)
                for value in c_control:
                    c_anticontrol_translation = c_anticontrol_translation + f"({self.cbit_reg_name}[{value}] == 0) && "                
                c_anticontrol_translation = c_anticontrol_translation.rstrip(' && ')
                c_anticontrol_translation = f"({c_anticontrol_translation})"                
            c_translation = f"{c_control_translation} && {c_anticontrol_translation}"
            c_translation = c_translation.rstrip(' && ')
            end_translation = f"}}"
            c_translation = f"if({c_translation}) {{ " 
            
        translation =  f"{c_translation}{q_translation} {end_translation}"   
        return translation

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
        output = operation["outputs"]
        
        
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
