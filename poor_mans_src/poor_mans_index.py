#!/home/ninsy/anaconda3/bin/python
import serial
import logging

# TODO: How may I actually reverse engineer protocol? May I just somehow guess all of these data? ask @gynvael.coldwind

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
    # TODO: csv stream
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    l = logging.getLogger('poor_mans_logger')
    l.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    l.addHandler(ch)

    return l 


if __name__ == "__main__":
    logger = new_logger()
    with new_serial() as s:
        while True:
            line = s.read_until(b'\r\n')
            logger.debug('%d - %s', len(line), line)