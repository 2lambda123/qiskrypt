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

from unittest import TestCase, TestLoader, TestSuite
"""
Import TestCase, TestLoader and TestSuite from Unittest.
"""

from qiskit import QuantumRegister
"""
Import Quantum Register from IBM's Qiskit.
"""

from src.circuit.registers.quantum.QiskryptQuantumRegister import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.circuit.registers.quantum.fully_quantum.QiskryptFullyQuantumRegister import QiskryptFullyQuantumRegister
"""
Import the Qiskrypt's Fully-Quantum Register.
"""

from src.circuit.registers.quantum.semi_quantum.QiskryptSemiQuantumRegister import QiskryptSemiQuantumRegister
"""
Import the Qiskrypt's Semi-Quantum Register.
"""

from src.circuit.registers.classical.QiskryptClassicalRegister import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""


class QiskryptSemiQuantumRegisterTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Semi-Quantum Register.
    """

    def test_no_1_qiskrypt_semi_quantum_register_1_qubit(self):
        """
        Test Case #1:

        - Create a Qiskrypt's Semi-Quantum Register, with 1 qubit.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        semi_quantum_register_name = "semi_qu_reg"
        """
        Set the name of the Qiskrypt's Semi-Quantum Register.
        """

        semi_quantum_register_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Semi-Quantum Register.
        """

        qiskrypt_semi_quantum_register = \
            QiskryptSemiQuantumRegister(name=semi_quantum_register_name,
                                        num_qubits=semi_quantum_register_num_qubits,
                                        quantum_register=None)
        """
        Create a Qiskrypt's Semi-Quantum Register, given its name and number of bits.
        """

        assert(semi_quantum_register_name == qiskrypt_semi_quantum_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Semi-Quantum Register.
        """

        assert(semi_quantum_register_num_qubits == qiskrypt_semi_quantum_register.get_num_qubits())
        """
        Assertion for the number of qubits of the Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register.get_quantum_register(), QuantumRegister))
        """
        Assertion for the IBM's Qiskit Quantum Register of the Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register, QiskryptQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Quantum Register.
        """

        assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Fully-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register, QiskryptSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Semi-Quantum Register.
        """

        assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_semi_quantum_register_2_qubits(self):
        """
        Test Case #2:

        - Create a Qiskrypt's Semi-Quantum Register, with 2 qubits.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        semi_quantum_register_name = "semi_qu_reg"
        """
        Set the name of the Qiskrypt's Semi-Quantum Register.
        """

        semi_quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Semi-Quantum Register.
        """

        qiskrypt_semi_quantum_register = \
            QiskryptSemiQuantumRegister(name=semi_quantum_register_name,
                                        num_qubits=semi_quantum_register_num_qubits,
                                        quantum_register=None)
        """
        Create a Qiskrypt's Semi-Quantum Register, given its name and number of bits.
        """

        assert(semi_quantum_register_name == qiskrypt_semi_quantum_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Semi-Quantum Register.
        """

        assert(semi_quantum_register_num_qubits == qiskrypt_semi_quantum_register.get_num_qubits())
        """
        Assertion for the number of qubits of the Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register.get_quantum_register(), QuantumRegister))
        """
        Assertion for the IBM's Qiskit Quantum Register of the Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register, QiskryptQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Quantum Register.
        """

        assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Fully-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register, QiskryptSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Semi-Quantum Register.
        """

        assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_semi_quantum_register_4_qubits(self):
        """
        Test Case #3:

        - Create a Qiskrypt's Semi-Quantum Register, with 4 qubits.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        semi_quantum_register_name = "semi_qu_reg"
        """
        Set the name of the Qiskrypt's Semi-Quantum Register.
        """

        semi_quantum_register_num_qubits = 4
        """
        Set the number of qubits for the Qiskrypt's Semi-Quantum Register.
        """

        qiskrypt_semi_quantum_register = \
            QiskryptSemiQuantumRegister(name=semi_quantum_register_name,
                                        num_qubits=semi_quantum_register_num_qubits,
                                        quantum_register=None)
        """
        Create a Qiskrypt's Semi-Quantum Register, given its name and number of bits.
        """

        assert(semi_quantum_register_name == qiskrypt_semi_quantum_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Semi-Quantum Register.
        """

        assert(semi_quantum_register_num_qubits == qiskrypt_semi_quantum_register.get_num_qubits())
        """
        Assertion for the number of qubits of the Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register.get_quantum_register(), QuantumRegister))
        """
        Assertion for the IBM's Qiskit Quantum Register of the Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register, QiskryptQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Quantum Register.
        """

        assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Fully-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register, QiskryptSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Semi-Quantum Register.
        """

        assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_4_qiskrypt_semi_quantum_register_8_qubits(self):
        """
        Test Case #4:

        - Create a Qiskrypt's Semi-Quantum Register, with 8 qubits.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        semi_quantum_register_name = "semi_qu_reg"
        """
        Set the name of the Qiskrypt's Semi-Quantum Register.
        """

        semi_quantum_register_num_qubits = 8
        """
        Set the number of qubits for the Qiskrypt's Semi-Quantum Register.
        """

        qiskrypt_semi_quantum_register = \
            QiskryptSemiQuantumRegister(name=semi_quantum_register_name,
                                        num_qubits=semi_quantum_register_num_qubits,
                                        quantum_register=None)
        """
        Create a Qiskrypt's Semi-Quantum Register, given its name and number of bits.
        """

        assert(semi_quantum_register_name == qiskrypt_semi_quantum_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Semi-Quantum Register.
        """

        assert(semi_quantum_register_num_qubits == qiskrypt_semi_quantum_register.get_num_qubits())
        """
        Assertion for the number of qubits of the Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register.get_quantum_register(), QuantumRegister))
        """
        Assertion for the IBM's Qiskit Quantum Register of the Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register, QiskryptQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Quantum Register.
        """

        assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Fully-Quantum Register.
        """

        assert(isinstance(qiskrypt_semi_quantum_register, QiskryptSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Semi-Quantum Register.
        """

        assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Semi-Quantum Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)


if __name__ == "__main__":

    qiskrypt_semi_quantum_register_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptSemiQuantumRegisterTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Semi-Quantum Register.
    """

    qiskrypt_semi_quantum_register_test_suite = \
        TestSuite([qiskrypt_semi_quantum_register_test_cases])
    """
    Load the Test Suite with the Test Cases for the Qiskrypt's Semi-Quantum Register.
    """