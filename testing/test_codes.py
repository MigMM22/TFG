# -------------------------
# QISKIT CODES
# -------------------------
gates_codes = '''
-- X ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name", ancilla=(0, 0))

qc.add_operation("X", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- Y ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("Y", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- Z ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("Z", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- H ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("H", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- R ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("R(1,2)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- P ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("P(1)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- U ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("U(1,2,3)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- RY ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("RY(1)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- RX ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("RX(1)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- RY ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("RY(1)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- RZ ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("RZ(1)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- XX ------ 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name",ancilla=(0, 0))

qc.add_operation("XX(1)", targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- YY ------ 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name",ancilla=(0, 0))

qc.add_operation("YY(1)", targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- ZZ ------ 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name",ancilla=(0, 0))

qc.add_operation("ZZ(1)", targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- XY ------ 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name",ancilla=(0, 0))

qc.add_operation("XY(1)", targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- RootPhase ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("RootPhase(1)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- U1 ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("U1(1)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- U2 ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("U2(1,2)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- U3 ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("U3(1,2,3)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- SqrtX ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("SqrtX", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- HalfDeutsch ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("HalfDeutsch(1)", targets=[0])
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- SWAP ------ 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name",ancilla=(0, 0))

qc.add_operation("SWAP", targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- SqrtSWAP ------ 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name",ancilla=(0, 0))

qc.add_operation("SqrtSWAP", targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- iSWAP ------ 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name",ancilla=(0, 0))

qc.add_operation("iSWAP", targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- fSWAP ------ 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name",ancilla=(0, 0))

qc.add_operation("fSWAP", targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- Barrier ------ 1
::
import qsimov as qj

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation("X", targets=[0])
qc.add_operation("BARRIER")
qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- Custom_Gate ------ 1
::
import qsimov as qj

qa = qj.QGate(1, 0, "CustGate")
qa.add_operation("H", targets=0)

qc = qj.QCircuit(1, 1, "Name",ancilla=(0, 0))

qc.add_operation(qa, targets=[0])

qc.add_operation("MEASURE", targets=(0), outputs=(0))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
'''

gate_operations_codes = '''
-- CONTROL ----- 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name", ancilla=(0, 0))

qc.add_operation("X", targets=[0], controls=[1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- ANTICONTROL ----- 2
::
import qsimov as qj

qc = qj.QCircuit(2, 2, "Name", ancilla=(0, 0))

qc.add_operation("X", targets=[0], anticontrols=[1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- CONTROL 2 ----- 4
::
import qsimov as qj

qc = qj.QCircuit(4, 4, "Name", ancilla=(0, 0))

qc.add_operation("X", targets=[0], controls=[1])
qc.add_operation("Z", targets=[2], controls=[3])

qc.add_operation("MEASURE", targets=(0,1,2,3), outputs=(0,1,2,3))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- ANTICONTROL 2 ----- 4
::
import qsimov as qj

qc = qj.QCircuit(4, 4, "Name", ancilla=(0, 0))

qc.add_operation("X", targets=[0], anticontrols=[1])
qc.add_operation("Z", targets=[2], anticontrols=[3])

qc.add_operation("MEASURE", targets=(0,1,2,3), outputs=(0,1,2,3))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- CONTROL INSIDE CUSTOM GATE----- 2
::
import qsimov as qj

qa = qj.QGate(2, 0, "CustGate")
qa.add_operation("X", targets=0, controls = 1)

qc = qj.QCircuit(2, 2, "Name", ancilla=(0, 0))

qc.add_operation(qa, targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- ANTICONTROL INSIDE CUSTOM GATE----- 2
::
import qsimov as qj

qa = qj.QGate(2, 0, "CustGate")
qa.add_operation("X", targets=0, anticontrols = 1)

qc = qj.QCircuit(2, 2, "Name", ancilla=(0, 0))

qc.add_operation(qa, targets=[0,1])
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- CONTROL CUSTOM GATE----- 2
::
import qsimov as qj

qa = qj.QGate(1, 0, "CustGate")
qa.add_operation("X", targets=0)

qc = qj.QCircuit(2, 2, "Name", ancilla=(0, 0))

qc.add_operation(qa, targets=[0], controls = 1)
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))

executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
::
-- ANTICONTROL CUSTOM GATE----- 2
::
import qsimov as qj

qa = qj.QGate(1, 0, "CustGate")
qa.add_operation("X", targets=0)

qc = qj.QCircuit(2, 2, "Name", ancilla=(0, 0))

qc.add_operation(qa, targets=[0], anticontrols = 1)
qc.add_operation("MEASURE", targets=(0,1), outputs=(0,1))
executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
'''

deutsch_algorithm = '''
-- Deutsch (f(x) = ~x) ----- 1
::
import qsimov as qj
import numpy as np
from sympy.matrices import Matrix
from sympy import I
qc = qj.QCircuit(2, 1, "my_qsimov_circuit")

def oracle():
        custom_gate = qj.QGate(2, 0, "oracle")
        custom_gate.add_operation(f"X", targets=[0])

        custom_gate.add_operation(f"X", targets=[1], controls=[0])

        custom_gate.add_operation(f"X", targets=[0])

        return custom_gate

qc.add_operation(f"X", targets=[0])

qc.add_operation(f"H", targets=[0])
qc.add_operation(f"H", targets=[1])

qc.add_operation("BARRIER")
qc.add_operation(oracle(), targets=[1, 0])
qc.add_operation("BARRIER")
qc.add_operation(f"H", targets=[1])

qc.add_operation("MEASURE", targets=[1], outputs=[0])
executor = qj.Drewom()
result_test = executor.execute(qc, 1000)
'''