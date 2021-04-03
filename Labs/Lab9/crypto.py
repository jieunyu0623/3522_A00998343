import ast

import des
import argparse
import abc
import enum

from des import DesKey

KEY_LENGTH_AVAILABLE = [8, 16, 24]


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class KeyLengthError(Exception):
    """
    throws an error when the DES key length is not 8, 16, or 24.
    """
    def __init__(self, length):
        super().__init__(f"\nKeys must be 8, 16, or 24 characters long. "
                         f"Your key is {length} characters long.\n")
        self.length = length


class MultipleInputValueError(Exception):
    """
    throws an error when there are multiple input values.
    """
    def __init__(self, string, file):
        super().__init__(f"\nYou have multiple input values. "
                         f"String '{string}' and file path '{file}' were detected!\n")
        self.string = string
        self.file = file


class NoInputValueError(Exception):
    """
    throws an error when there are no input values.
    """
    def __init__(self):
        super().__init__(f"\nNo input values were detected!\n")


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:
    """
    Crypto class used for handling multiple handlers for encryption and decryption.
    """

    def __init__(self):
        en_key = KeyLengthHandler()
        en_input = InputValidationHandler()
        en_encrypt = EncryptionCryptoHandler()
        en_print = PrintHandler()
        en_key.next_handler = en_input
        en_input.next_handler = en_encrypt
        en_encrypt.next_handler = en_print

        de_key = KeyLengthHandler()
        de_input = InputValidationHandler()
        de_decrypt = DecryptionCryptoHandler()
        de_print = PrintHandler()
        de_key.next_handler = de_input
        de_input.next_handler = de_decrypt
        de_decrypt.next_handler = de_print

        self.encryption_start_handler = en_key
        self.decryption_start_handler = de_key

    def execute_request(self, request: Request):
        """
        executes request based on the type of encryption/decryption mode
        :param request:
        :return: self.encryption_start_handler.handle_request(request)
        """
        if request.encryption_state is CryptoMode.EN:
            return self.encryption_start_handler.handle_request(request)
        elif request.encryption_state is CryptoMode.DE:
            return self.decryption_start_handler.handle_request(request)


class BaseCryptoHandler(abc.ABC):
    """
    Base class for multiple handlers
    """

    def __init__(self, next_handler=None):
        """
        grabs the next handler.
        :param next_handler: BaseCryptoHandler
        """
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, request: Request):
        """
        handles request for different type of handlers
        :param request: Request
        :return: None
        """
        pass

    def set_handler(self, handler):
        """
        sets the handler
        :param handler: BaseCryptoHandler
        :return: None
        """
        self.next_handler = handler


class EncryptionCryptoHandler(BaseCryptoHandler):
    """
    Encryption handler class inherited from BaseCryptoHandler
    """

    def handle_request(self, request: Request):
        """
        handles encryption depending on the type of input source.
        :param request: Request
        :return: self.next_handler
        """
        print("Encryption handler running...")
        byte_key = request.key.encode()
        key = DesKey(byte_key)

        if request.data_input:
            print("Encrypting from the string passed...")
            byte_str = request.data_input.encode()
            request.result = key.encrypt(byte_str, padding=True)  # automatically sets the length to 8, 16 or 24.
        else:
            print("Encrypting from the file...")
            with open(request.input_file) as file:
                byte_str = file.read().encode()
                request.result = key.encrypt(byte_str, padding=True)

        if not self.next_handler:
            return
        else:
            self.next_handler.handle_request(request)


class DecryptionCryptoHandler(BaseCryptoHandler):
    """
    Decryption handler class inherited from BaseCryptoHandler
    """

    def handle_request(self, request: Request):
        """
        handles decryption depending on the type of input source.
        :param request: Request
        :return: self.next_handler
        """
        print("Decryption handler running...")
        byte_key = request.key.encode()
        key = DesKey(byte_key)

        if request.data_input:
            print("Decrypting from the string passed...")
            request.result = ast.literal_eval(request.data_input)
        else:
            with open(request.input_file, "rb+") as file:
                request.result = file.read()

        request.result = key.decrypt(request.result, padding=True).decode('utf-8')

        if not self.next_handler:
            return
        else:
            self.next_handler.handle_request(request)


class PrintHandler(BaseCryptoHandler):
    """
    PrintHandler class inherited from BaseCryptoHandler
    """

    def handle_request(self, request: Request):
        """
        handles printing the encrypted/decrypted data to the console
        or writing to a file
        :param request: Request
        :return: self.next_handler
        """
        print("Print Handler running...")
        if request.output.lower() == "print":
            print(request.result)
        else:
            print("hello")
            with open(request.output, "w+") as output_file:
                output_file.write(request.result)


class KeyLengthHandler(BaseCryptoHandler):
    """
    KeyLengthHandler class inherited from BaseCryptoHandler
    """

    def handle_request(self, request: Request):
        """
        checks if the key passed or from a file is 8, 16, 24 in length
        :param request: Request
        :return: self.next_handler
        """
        print("Key Length Check running...")
        if len(request.key) in KEY_LENGTH_AVAILABLE:
            if not self.next_handler:
                return
            else:
                self.next_handler.handle_request(request)
        else:
            raise KeyLengthError(len(request.key))


class InputValidationHandler(BaseCryptoHandler):
    """
    InputValidationHandler class inherited from BaseCryptoHandler
    """

    def handle_request(self, request: Request):
        """
        checks if the input data has a single value
        :param request: Request
        :return: self.next_handler
        """
        print("Input Validation Check running...")

        # case 1: two inputs
        if request.data_input and request.input_file:
            raise MultipleInputValueError(request.data_input,
                                           request.input_file)

        # case 2: no inputs
        if request.data_input is None and not request.input_file:
            raise NoInputValueError

        if not self.next_handler:
            return
        else:
            self.next_handler.handle_request(request)


def main(request: Request):
    """
    grabs input source (arguments) from the terminal and pass to execute_request method
    :param request: Request
    :return: None
    """
    crypto = Crypto()
    try:
        crypto.execute_request(request)
    except FileNotFoundError as e: # if the file is not found, prints the FileNotFoundError
        print(e)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
