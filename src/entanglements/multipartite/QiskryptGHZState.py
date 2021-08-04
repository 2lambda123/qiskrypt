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

from src.entanglements.QiskryptQuantumEntanglement \
    import QiskryptQuantumEntanglement
"""
Import the Qiskrypt's Quantum Entanglement.
"""

from src.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES
"""
Import the available Quantum Entanglement cardinalities for
the Qiskrypt's Quantum Entanglement.
"""

from src.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES
"""
Import the available Quantum Entanglement types for
the Qiskrypt's Quantum Entanglement.
"""

from src.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptGHZState(QiskryptQuantumEntanglement):
    """
    Object class for the Qiskrypt's GHZ State.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit):
        """
        Constructor of the Qiskrypt's GHZ State.

        :param name: the name of the Qiskrypt's GHZ State.
        :param qiskrypt_quantum_circuit: the name of the Qiskrypt's GHZ State.
        """

        if qiskrypt_quantum_circuit.get_total_num_qubits() >= 3:
            """
            If the number of qubits of
            the given Qiskrypt's Quantum Circuit is greater or equal than 3.
            """

            super().__init__(name, POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES[1],
                             POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES[0],
                             qiskrypt_quantum_circuit)
            """
            Calls the constructor of the super-class Qiskrypt's Quantum Entanglement.
            """

            self.qiskit_quantum_register_control_index = None
            """
            Set the index of the control IBM Qiskit's Quantum Register, as None.
            """

            self.qiskit_quantum_registers_target_indexes = None
            """
            Set the indexes of the target IBM Qiskit's Quantum Registers, as None.
            """

            self.control_qubit_index = None
            """
            Set the index of a qubit inside the control IBM Qiskit's Quantum Register, as None.
            """

            self.target_qubits_indexes = None
            """
            Set the indexes of the qubits inside the target IBM Qiskit's Quantum Registers, as None.
            """

        else:
            """
            If the number of qubits and bits of
            the given Qiskrypt's Quantum Circuit is strictly lower than 3.
            """

            # TODO - Throw Exception

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's GHZ State.

        :return super().get_name(): the name of the Qiskrypt's GHZ State.
        """

        """
        Return the name of the Qiskrypt's GHZ State.
        """
        return super().get_name()

    def get_quantum_entanglement_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's GHZ State.

        :return super().get_quantum_entanglement_cardinality(): the cardinality of
                                                                the Qiskrypt's GHZ State.
        """

        """
        Return the cardinality of the Qiskrypt's GHZ State.
        """
        return super().get_quantum_entanglement_cardinality()

    def get_quantum_entanglement_type(self) -> str:
        """
        Return the type of the Qiskrypt's GHZ State.

        :return super().get_quantum_entanglement_type(): the type of the Qiskrypt's GHZ State.
        """

        """
        Return the type of the Qiskrypt's GHZ State.
        """
        return super().get_quantum_entanglement_type()

    def get_qiskrypt_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's GHZ State.

        :return super().get_qiskrypt_quantum_circuit(): the Qiskrypt's Quantum Circuit,
                                                        from which it will be configured
                                                        the Qiskrypt's GHZ State.
        """

        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's GHZ State.
        """
        return super().get_qiskrypt_quantum_circuit()

    def get_qiskit_quantum_register_control_index(self) -> int:
        """
        Return the index of the control IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.

        :return self.qiskit_quantum_register_control_index: the index of the control
                                                            IBM Qiskit's Quantum Register of
                                                            the Qiskrypt's GHZ State.
        """

        """
        Return the index of the control IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.
        """
        return self.qiskit_quantum_register_control_index

    def get_qiskit_quantum_registers_target_indexes(self) -> list:
        """
        Return the indexes of the target IBM Qiskit's Quantum Registers of the Qiskrypt's GHZ State.

        :return self.qiskit_quantum_registers_target_indexes: the indexes of the target
                                                           IBM Qiskit's Quantum Registers of
                                                           the Qiskrypt's GHZ State.
        """

        """
        Return the index of the target IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.
        """
        return self.qiskit_quantum_registers_target_indexes

    def get_control_qubit_index(self) -> int:
        """
        Return the index of a qubit inside the control IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.

        :return self.control_qubit_index: the index of a qubit inside
                                          the control IBM Qiskit's Quantum Register of
                                          the Qiskrypt's GHZ State.
        """

        """
        Return the index of a qubit inside the control IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.
        """
        return self.control_qubit_index

    def get_target_qubits_indexes(self) -> list:
        """
        Return the indexes of the qubits inside the target IBM Qiskit's Quantum Registers of the Qiskrypt's GHZ State.

        :return self.target_qubit_index: the indexes of the qubits inside
                                         the target IBM Qiskit's Quantum Registers of
                                         the Qiskrypt's GHZ State.
        """

        """
        Return the indexes of the qubits inside the target IBM Qiskit's Quantum Registers of the Qiskrypt's GHZ State.
        """
        return self.target_qubits_indexes
