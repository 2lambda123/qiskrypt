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
Definition of the custom Exception messages.
"""

MESSAGE_DICE_NOT_THROWN_YET_EXCEPTION = "Dice Not Thrown Yet Error: " \
                                        "The Dice of the Quantum Dice Throwing was not thrown yet!!!\n"
"""
The custom defined message for the Dice Not Thrown Yet Error for
the Qiskrypt's Quantum Dice Throwing.
"""

MESSAGE_DICE_ALREADY_THROWN_EXCEPTION = "Dice Already Thrown Error: " \
                                        "The Dice of the Quantum Dice Throwing was already thrown!!!\n"
"""
The custom defined message for the Dice Already Thrown Error for
the Qiskrypt's Quantum Dice Throwing.
"""


class QiskryptQuantumDiceThrowingDiceNotThrownYetError(Exception):
    """
    Object Class of the Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.
    """

    def __init__(self, message=MESSAGE_DICE_NOT_THROWN_YET_EXCEPTION):
        """
        Constructor for the Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.

        :param message: the custom message for the Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.
        """

        self.message = message
        """
        Set the custom message for the Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumDiceThrowingDiceAlreadyThrownError(Exception):
    """
    Object Class of the Dice Already Thrown Error for the Qiskrypt's Quantum Dice Throwing.
    """

    def __init__(self, message=MESSAGE_DICE_ALREADY_THROWN_EXCEPTION):
        """
        Constructor for the Dice Already Thrown Error for the Qiskrypt's Quantum Dice Throwing.

        :param message: the custom message for the Dice Already Thrown Error for the Qiskrypt's Quantum Dice Throwing.
        """

        self.message = message
        """
        Set the custom message for the Dice Already Thrown Error for the Qiskrypt's Quantum Dice Throwing.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """