from smartcard.System import readers
from smartcard.util import toHexString

# List all available readers
available_readers = readers()
if not available_readers:
    print("No smart card readers found.")
else:
    reader = available_readers[0]
    print("Using reader:", reader)

    # Connect to the reader
    connection = reader.createConnection()
    connection.connect()

    # Example: sending a command to get card info (this depends on card type)
    get_data_command = [0x00, 0xA4, 0x04, 0x00, 0x00]  # Replace with actual command for your card
    data, sw1, sw2 = connection.transmit(get_data_command)

    # Print the response (card data)
    print("Card data:", toHexString(data))
    print("Status words:", hex(sw1), hex(sw2))
