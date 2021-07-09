"""

Copyrights:\n
- © Qiskrypt, 2021 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum cryptography, quantum communication and
  other protocols/algorithms, built using the IBM's Qiskit.

College(s):\n
- NOVA School of Science and Technology, NOVA University of Lisbon, Portugal.
- Faculty of Sciences, University of Lisbon, Portugal.
- Tecnico Lisboa, University of Lisbon, Portugal.
- School of Engineering, University of Connecticut, United States of America.

Other Institution(s):\n
- Instituto de Telecomunicacoes, Portugal.
- SQIG, Portugal.
- LASIGE, Portugal.
- UT Austin Program, Portugal.

Author(s):\n
- Ruben Barreiro (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

Acknowledgement(s):\n
- Prof. Andre Souto (Faculty of Sciences, University of Lisbon, Portugal).
- Prof. Paulo Mateus (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Nikola Paunkovic (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Walter Krawec (School of Engineering, University of Connecticut, United States of America).

"""

"""
Import required Libraries and Packages.
"""

from numpy import sqrt, exp
"""
Import Squared Root and Exponential from NumPy.
"""

from qiskit import QuantumCircuit
"""
Import Quantum Circuit from IBM's Qiskit.
"""

from qiskit.quantum_info.operators import Operator
"""
Import Operator of the Quantum_Info.Operators Module from IBM's Qiskit.
"""

from src.circuit.registers.quantum.QiskryptQuantumRegister import QiskryptQuantumRegister
"""
Import Qiskrypt's Quantum Register of
the Src.Circuit.Registers.Quantum.QiskryptQuantumRegister Module from Qiskrypt.
"""

from src.circuit.registers.quantum.fully_quantum.QiskryptFullyQuantumRegister import QiskryptFullyQuantumRegister
"""
Import Qiskrypt's Fully-Quantum Register of
the Src.Circuit.Registers.Quantum.Fully_Quantum.QiskryptFullyQuantumRegister Module from Qiskrypt.
"""

from src.circuit.registers.quantum.semi_quantum.QiskryptSemiQuantumRegister import QiskryptSemiQuantumRegister
"""
Import Qiskrypt's Semi-Quantum Register of
the Src.Circuit.Registers.Quantum.Semi_Quantum.QiskryptSemiQuantumRegister Module from Qiskrypt.
"""

from src.circuit.registers.classical.QiskryptClassicalRegister import QiskryptClassicalRegister
"""
Import Qiskrypt's Classical Register of
the Src.Circuit.Registers.Classical.QiskryptClassicalRegister Module from Qiskrypt.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitUnsupportedTypeRegistersError
"""
Import the Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
"""


class QiskryptQuantumCircuit:
    """
    Class for the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, name="qu_circ", quantum_registers=None,
                 fully_quantum_registers=None, semi_quantum_registers=None,
                 classical_registers=None, global_phase=0, quantum_circuit=None):
        """
        :param name: The name for the Qiskrypt's Quantum Circuit.
        :param quantum_registers: The Qiskrypt's Quantum Registers for the Qiskrypt's Quantum Circuit.
        :param fully_quantum_registers: The Qiskrypt's Fully-Quantum Registers for the Qiskrypt's Quantum Circuit.
        :param semi_quantum_registers: The Qiskrypt's Semi-Quantum Registers for the Qiskrypt's Quantum Circuit.
        :param classical_registers: The Qiskrypt's Classical Registers for the Qiskrypt's Quantum Circuit.
        :param global_phase: The global phase for the Qiskrypt's Quantum Circuit.
        :param quantum_circuit: The IBM's Qiskit Quantum Circuit.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        if quantum_circuit is None:
            """
            If there is no given any IBM's Quantum Circuit, it will be created a new one,
            according to the given Qiskrypt's Quantum, Fully-Quantum and Semi-Quantum and
            Classical Registers.
            """

            if (quantum_registers is not None) and (fully_quantum_registers is None) and \
                (semi_quantum_registers is None) and (classical_registers is not None):
                """
                If the Qiskrypt's Quantum and Classical Registers given as arguments are not None,
                but the Qiskrypt's Fully-Quantum and Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Classical Memory).
                """

                if (isinstance(quantum_registers, list)) and (isinstance(classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum and Classical Registers are lists.
                    """

                    for quantum_register in quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.quantum_registers = quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.classical_registers = classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.quantum_circuit = \
                        QuantumCircuit([quantum_register.quantum_register for quantum_register in quantum_registers],
                                       [classical_register.classical_register for classical_register in classical_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (quantum_registers is None) and (fully_quantum_registers is not None) and \
                (semi_quantum_registers is None) and (classical_registers is not None):
                """
                If the Qiskrypt's Fully-Quantum and Classical Registers given as arguments are not None,
                but the Qiskrypt's Quantum and Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Fully-Quantum/Classical Memory).
                """

                if (isinstance(fully_quantum_registers, list)) and (isinstance(classical_registers, list)):
                    """
                    If the Qiskrypt's Fully-Quantum and Classical Registers are lists.
                    """

                    for fully_quantum_register in fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.fully_quantum_registers = fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.classical_registers = classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.quantum_circuit = \
                        QuantumCircuit([fully_quantum_register.quantum_register for fully_quantum_register in fully_quantum_registers],
                                       [classical_register.classical_register for classical_register in classical_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (quantum_registers is None) and (fully_quantum_registers is None) and \
                (semi_quantum_registers is not None) and (classical_registers is not None):
                """
                If the Qiskrypt's Semi-Quantum and Classical Registers given as arguments are not None,
                but the Qiskrypt's Quantum and Fully-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Semi-Quantum/Classical Memory).
                """

                if (isinstance(semi_quantum_registers, list)) and (isinstance(classical_registers, list)):
                    """
                    If the Qiskrypt's Semi-Quantum and Classical Registers are lists.
                    """

                    for semi_quantum_register in semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.semi_quantum_registers = semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.classical_registers = classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.quantum_circuit = \
                        QuantumCircuit([semi_quantum_register.quantum_register for semi_quantum_register in semi_quantum_registers],
                                       [classical_register.classical_register for classical_register in classical_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (quantum_registers is None) and (fully_quantum_registers is None) and \
                (semi_quantum_registers is not None) and (classical_registers is not None):
                """
                If the Qiskrypt's Semi-Quantum and Classical Registers given as arguments are not None,
                but the Qiskrypt's Quantum and Fully-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Semi-Quantum/Classical Memory).
                """

                if (isinstance(semi_quantum_registers, list)) and (isinstance(classical_registers, list)):
                    """
                    If the Qiskrypt's Semi-Quantum and Classical Registers are lists.
                    """

                    for semi_quantum_register in semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.semi_quantum_registers = semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.classical_registers = classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.quantum_circuit = \
                        QuantumCircuit([semi_quantum_register.quantum_register for semi_quantum_register in semi_quantum_registers],
                                       [classical_register.classical_register for classical_register in classical_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (quantum_registers is not None) and (fully_quantum_registers is None) and \
                (semi_quantum_registers is None) and (classical_registers is None):
                """
                If the Qiskrypt's Quantum Registers given as arguments are not None,
                but the Qiskrypt's Fully-Quantum, Semi-Quantum and Classical Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a Quantum Memory).
                """

                if isinstance(quantum_registers, list):
                    """
                    If the Qiskrypt's Quantum Registers are lists.
                    """

                    for quantum_register in quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.quantum_registers = quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.classical_registers = None
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.quantum_circuit = \
                        QuantumCircuit([quantum_register.quantum_register for quantum_register in quantum_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (quantum_registers is None) and (fully_quantum_registers is not None) and \
                (semi_quantum_registers is None) and (classical_registers is None):
                """
                If the Qiskrypt's Fully-Quantum Registers given as arguments are not None,
                but the Qiskrypt's Quantum, Semi-Quantum and Classical Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a Fully-Quantum Memory).
                """

                if isinstance(fully_quantum_registers, list):
                    """
                    If the Qiskrypt's Fully-Quantum Registers are lists.
                    """

                    for fully_quantum_register in fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.fully_quantum_registers = fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.classical_registers = None
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.quantum_circuit = \
                        QuantumCircuit([fully_quantum_register.quantum_register for fully_quantum_register in fully_quantum_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (quantum_registers is None) and (fully_quantum_registers is None) and \
                (semi_quantum_registers is not None) and (classical_registers is None):
                """
                If the Qiskrypt's Semi-Quantum Registers given as arguments are not None,
                but the Qiskrypt's Quantum, Fully-Quantum and Classical Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a Semi-Quantum Memory).
                """

                if isinstance(semi_quantum_registers, list):
                    """
                    If the Qiskrypt's Semi-Quantum Registers are lists.
                    """

                    for semi_quantum_register in semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.semi_quantum_registers = semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.classical_registers = None
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.quantum_circuit = \
                        QuantumCircuit([semi_quantum_register.quantum_register for semi_quantum_register in semi_quantum_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (quantum_registers is None) and (fully_quantum_registers is None) and \
                (semi_quantum_registers is None) and (classical_registers is not None):
                """
                If the Qiskrypt's Classical Registers given as arguments are not None,
                but the Qiskrypt's Quantum, Fully-Quantum and Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a Classical Memory).
                """

                if isinstance(classical_registers, list):
                    """
                    If the Qiskrypt's Classical Registers are lists.
                    """

                    for classical_register in classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.classical_registers = classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.quantum_circuit = \
                        QuantumCircuit([classical_register.classical_register for classical_register in classical_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

    @staticmethod
    def raise_unsupported_type_registers_error():
        """
        Return/Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
        :raise unsupported_type_registers_error: an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
        """

        unsupported_type_registers_error = QiskryptQuantumCircuitUnsupportedTypeRegistersError()
        """
        Retrieve the Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
        """
        raise unsupported_type_registers_error
