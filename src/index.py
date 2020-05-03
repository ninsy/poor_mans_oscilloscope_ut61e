#!/home/ninsy/anaconda3/bin/python
import serial
import logging

# TODO: How may I actually reverse engineer protocol? May I just somehow guess all of these data? ask @gynvael.coldwind
# If receiving "[Errno 13] could not open port...", run ./scripts/privileges.sh as sudo

def new_serial():
    s = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=19200,
        bytesize=7,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE
    )
    s.setDTR(True)
    s.setRTS(False)
    return s


def new_logger():
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    l = logging.getLogger('poor_mans_logger')
    l.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    l.addHandler(ch)

    return l 


def parse_line(serial_handle):
    line = s.read_until(b'\r\n')
    return (len(line), line)


if __name__ == "__main__":
    logger = new_logger()
    with new_serial() as s:
        while True:
            line_len, line = parse_line(s)
            logger.debug('%d - %s', line_len, line)