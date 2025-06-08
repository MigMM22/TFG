from translator.parent_translator import ParentTranslator
import numpy as np
class GateTranslator(ParentTranslator):
    def __init__(self, code_openQASM):
        super().__init__()
        self.code_openQASM = code_openQASM

    def translate(self, gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom = False):
        c_translation = ""
        end_translation = ""
        translation = ""        
        q_translation = ""
        ctrls_amount = 0
        antictrls_amount = 0

        if not isCustom:
            
            for qbit in control:
                q_translation += f"{self.qbit_reg_name}[{qbit}], "
                ctrls_amount += 1

            for qbit in anticontrol:
                q_translation += f"{self.qbit_reg_name}[{qbit}], "
                antictrls_amount += 1
            
            q_translation = f"{gate_name} {q_translation}"
            for tg in target:  
                q_translation += f"{self.qbit_reg_name}[{tg}], "
            q_translation = q_translation.rstrip(", ")
            q_translation += ";"

        else:            
            for qbit in control:
                q_translation += f"{self.qbit_reg_name}{qbit}, "
                ctrls_amount += 1

            for qbit in anticontrol:
                q_translation += f"{self.qbit_reg_name}{qbit}, "
                antictrls_amount += 1
            
            q_translation = f"{gate_name} {q_translation}"
            for tg in target:
                    
                q_translation += f"{self.qbit_reg_name}{tg}, "
            q_translation = q_translation.rstrip(", ")
            q_translation += ";"
        

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

    def translate_H(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = "h"
        
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)   
        return translation

    def translate_Y(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = "y"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)  
        return translation

    def translate_X(self, operation, isCustom = False): 
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]
        
        gate_name = "x"

        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)   
        return translation
          
    def translate_Z(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = "z"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)  
        return translation

    def translate_R(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angle = str(operation["gate"]).replace("R(", "").replace(")", "")
        angle = angle.split(',')
        

        if not ParentTranslator.custom_R:
            custom_R_gate = f'''gate r(theta, phi) q0 {{
    U(theta, phi - π/2, -phi + π/2) q0; 
}}
'''

            self.code_openQASM.insert(5,custom_R_gate)
            ParentTranslator.custom_R = True
        
        gate_name = f"r({angle[0]}, {angle[1]})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation

        # gate_name = f"p({angle})"
        # translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        # return translation

    def translate_P(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angle = str(operation["gate"]).replace("P(", "").replace(")", "")

        gate_name = f"p({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation   

    def translate_U(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angles = str(operation["gate"]).replace("U(", "").replace(")", "")
                
        angle_strings = angles.split(',')
             
        gate_name = f"U({angle_strings[0]}, {angle_strings[1]}, {angle_strings[2]})"
        
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)  
        return translation     

    def translate_XY(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        translation = ""
        custom_XY_gate = ""
        angle = str(operation["gate"]).replace("XY(", "").replace(")", "")

        if not ParentTranslator.custom_XY:
            custom_XY_gate = f'''gate XY(theta, beta) q0, q1 {{
            rz(beta) q1;
            rz(-pi/2) q0;
            sx q0;
            rz(pi/2) q0;
            s q1;
            cx q0, q1;
            ry(theta/2) q0;
            ry(theta/2) q1;
            cx q0, q1;
            sdg q1;
            rz(-pi/2) q0;
            sdg q0;
            rz(pi/2) q0;
            rz(-beta) q1;
}}'''

            self.code_openQASM.insert(5,custom_XY_gate)
            ParentTranslator.custom_XY = True
        
        gate_name = f"XY({angle},0)"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation

    def translate_RY(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angle = str(operation["gate"]).replace("RY(", "").replace(")", "")

        gate_name = f"ry({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)   
        return translation

    def translate_RX(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angle = str(operation["gate"]).replace("RX(", "").replace(")", "")

        gate_name = f"rx({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom) 
        return translation

    def translate_ZZ(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        translation = ""
        custom_ZZ_gate = ""
        angle = str(operation["gate"]).replace("ZZ(", "").replace(")", "")

        if not ParentTranslator.custom_ZZ:
            custom_ZZ_gate = f'''gate ZZ(theta) q0, q1 {{
    cx q0, q1;
    rz(theta) q1;
    cx q0, q1;
}}'''

            self.code_openQASM.insert(5,custom_ZZ_gate)
            ParentTranslator.custom_ZZ = True
        
        gate_name = f"ZZ({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation

    def translate_RZ(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angle = str(operation["gate"]).replace("RZ(", "").replace(")", "")

        gate_name = f"rz({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)  
        return translation

    def translate_U1(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angles = str(operation["gate"]).replace("U1(", "").replace(")", "")
    
        angle_strings = angles.split(',')
   
        gate_name = f"u1({angle_strings[0]})"
        
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)  

        return translation

    def translate_U2(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angles = str(operation["gate"]).replace("U2(", "").replace(")", "")
        # angles_part will now be "45,60,90"

        # 2. Split the string by the comma "," delimiter:
        angle_strings = angles.split(',')
        # angle_strings will be a list: ['45', '60', '90']

        # 3. Convert each angle string to an integer (or float if needed):
        
        gate_name = f"u2({angle_strings[0]}, {angle_strings[1]})"
        
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)  

        return translation

    def translate_U3(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        angles = str(operation["gate"]).replace("U3(", "").replace(")", "")

        angle_strings = angles.split(',')

        gate_name = f"U({angle_strings[0]}, {angle_strings[1]}, {angle_strings[2]})"
        
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom) 

        return translation 

    def translate_YY(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        translation = ""
        custom_YY_gate = ""
        angle = str(operation["gate"]).replace("YY(", "").replace(")", "")

        if not ParentTranslator.custom_YY:
            custom_YY_gate = f'''gate YY(theta) q0, q1 {{
    sdg q0;
    sdg q1;
    h q0;
    h q1;
    cx q0, q1;
    rz(theta) q1;
    cx q0, q1;
    h q0;
    h q1;
    s q0;
    s q1;
}}'''

            self.code_openQASM.insert(5,custom_YY_gate)
            ParentTranslator.custom_YY = True
        
        gate_name = f"YY({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation

    def translate_XX(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        translation = ""
        custom_XX_gate = ""
        angle = str(operation["gate"]).replace("XX(", "").replace(")", "")

        if not ParentTranslator.custom_XX:
            custom_XX_gate = f'''gate XX(theta) q0, q1 {{
    h q0;
    h q1;
    cx q0, q1;
    rz(theta) q1;
    cx q0, q1;
    h q0;
    h q1;
}}
'''

            self.code_openQASM.insert(5,custom_XX_gate)
            ParentTranslator.custom_XX = True
        
        gate_name = f"XX({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation
      
    def translate_RootPhase(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        translation = ""
        custom_RootPhase_gate = ""
        angle = str(operation["gate"]).replace("RootPhase(", "").replace(")", "")

        if not ParentTranslator.custom_RootPhase:
            custom_RootPhase_gate = f'''gate RootPhase(theta) q0 {{
    rz(theta) q0;
}}'''

            self.code_openQASM.insert(5,custom_RootPhase_gate)
            ParentTranslator.custom_RootPhase = True
            
        #Calculate the final angle
        angle = 2 * np.pi / 2**int(angle)
        gate_name = f"RootPhase({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation

    def translate_SWAP(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = f"swap"

        
        # target = f"[{target[0]}], {self.qbit_reg_name}[{target[1]}]"

        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)

        return translation

    def translate_SqrtSWAP(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = f"pow(0.5) @ swap"
        # target = f"[{target[0]}], {self.qbit_reg_name}[{target[1]}]"

        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)

        return translation

    def translate_iSWAP(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        translation = ""
        custom_iSWAP_gate = ""

        if not ParentTranslator.custom_iSWAP:
            custom_iSWAP_gate = f'''gate iSWAP q0, q1 {{
    s q0;
    s q1;
    h q0;
    cx q0, q1;
    cx q1, q0;
    h q1;
}}'''

            self.code_openQASM.insert(5,custom_iSWAP_gate)
            ParentTranslator.custom_iSWAP = True
        
        gate_name = f"iSWAP"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation

    def translate_HalfDeutsch(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        translation = ""
        custom_HalfDeutsch_gate = ""
        angle = str(operation["gate"]).replace("HalfDeutsch(", "").replace(")", "")

        if not ParentTranslator.custom_HalfDeutsch:
            custom_HalfDeutsch_gate = f'''gate HalfDeutsch(phi) q0 {{
    rz(-pi/4) q0;
    ry(2 * phi) q0;
    rz(-pi/4) q0;
}}'''

            self.code_openQASM.insert(5,custom_HalfDeutsch_gate)
            ParentTranslator.custom_HalfDeutsch = True
        
        gate_name = f"HalfDeutsch({angle})"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation

    def translate_fSWAP(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        translation = ""
        custom_fSWAP_gate = ""

        if not ParentTranslator.custom_fSWAP:
            custom_fSWAP_gate = f'''gate fSWAP q0, q1 {{
    swap q0, q1;   
    cz q0, q1;   
}}'''

            self.code_openQASM.insert(5,custom_fSWAP_gate)
            ParentTranslator.custom_fSWAP = True
        
        gate_name = f"fSWAP"
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)
        return translation

    def translate_SqrtX(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]

        gate_name = f"pow(0.5) @ x"
        
        translation = self.translate(gate_name, target, control, anticontrol, c_control, c_anticontrol, isCustom)

        return translation

    def translate_MEASURE(self, operation, isCustom = False):
        target = operation["targets"]
        output = operation["outputs"]
        
        translation = ""

        # translation = f"{translation}{self.cbit_reg_name}{[*output]} = measure {self.qbit_reg_name}{[*target]};\n"
        for i in range(len(target)):
            translation = f"{translation}{self.cbit_reg_name}{[output[i]]} = measure {self.qbit_reg_name}{[target[i]]};\n"
        

        translation = translation.rstrip('\n')
        return translation
    
    def translate_BARRIER(self, isCustom = False):
        
        translation = "barrier " + self.qbit_reg_name + ";"
        return translation

    def translate_custom_gate(self, operation, isCustom = False):
        target = operation["targets"]
        c_targets = operation["c_targets"]
        output = operation["outputs"]
        control = operation["controls"]
        anticontrol = operation["anticontrols"]
        c_control = operation["c_controls"]
        c_anticontrol = operation["c_anticontrols"]


        gate = operation["gate"]
        translation = ""

        if gate not in ParentTranslator.custom_gates:

            translation = f"gate {gate} "

            if(len(c_targets) > 0):
                error = "OpenQASM does not support c_targets for custom gates: \n"
                error += f"{operation}"
                raise NotImplementedError(error)
                
            
            for qbit in range(len(target)):
                translation += f"{self.qbit_reg_name}{qbit}, "

            translation = translation.rstrip(', ')
            
            translation += "{\n"

            for op in gate.get_operations():
                if(op == "BARRIER"):
                    error = "OpenQASM does not support BARRIER for custom gates: \n"
                    error += f"{operation}"
                    raise NotImplementedError(error)
                    
                match(str(op["gate"])):
                    case "H":                    
                        translation += "    " + self.translate_H(op, True) + "\n"
                    case "Y":                   
                        translation += "    " + self.translate_Y(op, True) + "\n"
                    case "X":           
                        translation += "    " + self.translate_X(op, True) + "\n"
                    case "Z":                    
                        translation += "    " + self.translate_Z(op, True) + "\n"
                    case gate if gate.startswith("R("): 
                        translation += "    " + self.translate_R(op, True) + "\n"
                    case gate if gate.startswith("U("):                    
                        translation += "    " + self.translate_U(op, True) + "\n"
                    case gate if gate.startswith("P("):                    
                        translation += "    " + self.translate_P(op, True) + "\n"
                    case gate if gate.startswith("XY("):                    
                        translation += "    " + self.translate_XY(op, True) + "\n"
                    case gate if gate.startswith("RY("):                    
                        translation += "    " + self.translate_RY(op, True) + "\n"
                    case gate if gate.startswith("RX("):                    
                        translation += "    " + self.translate_RX(op, True) + "\n"
                    case gate if gate.startswith("RZ("):                    
                        translation += "    " + self.translate_RZ(op, True) + "\n"
                    case gate if gate.startswith("ZZ("):
                        translation += "    " + self.translate_ZZ(op, True) + "\n"                
                    case gate if gate.startswith("U1("):                    
                        translation += "    " + self.translate_U1(op, True) + "\n"
                    case gate if gate.startswith("U2("):                    
                        translation += "    " + self.translate_U2(op, True) + "\n"
                    case gate if gate.startswith("U3("):                    
                        translation += "    " + self.translate_U3(op, True) + "\n"
                    case gate if gate.startswith("XX("):
                        translation += "    " + self.translate_XX(op, True) + "\n"
                    case gate if gate.startswith("YY("):
                        translation += "    " + self.translate_YY(op, True) + "\n"
                    case gate if gate.startswith("RootPhase("):
                        translation += "    " + self.translate_RootPhase(op, True) + "\n"
                    case "SWAP":
                        translation += "    " + self.translate_SWAP(op, True) + "\n"
                    case "SqrtSWAP":
                        translation += "    " + self.translate_SqrtSWAP(op, True) + "\n"
                    case "iSWAP":
                        translation += "    " + self.translate_iSWAP(op, True) + "\n"
                    case "HalfDeutsch":
                        translation += "    " + self.translate_HalfDeutsch(op, True) + "\n"
                    case "fSWAP":
                        translation += "    " + self.translate_fSWAP(op, True) + "\n"
                    case "SqrtX":                    
                        translation += "    " + self.translate_SqrtX(op, True) + "\n"
                    case "MEASURE":
                        error = "OpenQASM does not support MEASURE for custom gates: \n"
                        error += f"{operation}"
                        raise NotImplementedError(error)                  
                    case _:
                        #Le sumo translation después para que las inner custom salgan antes.               
                        inside_custom_translation, inside_custom_call = self.translate_custom_gate(op, True) 
                        translation = inside_custom_translation + "\n" + translation + "    " + inside_custom_call + "\n"
                        
            
            translation += "}\n"

            ParentTranslator.custom_gates[gate] = True


        if isCustom:
            custom_call = self.translate(operation["gate"], target, control, anticontrol, c_control, c_anticontrol, True)
        else:
            custom_call = self.translate(operation["gate"], target, control, anticontrol, c_control, c_anticontrol)    
            translation += custom_call

        return translation, custom_call