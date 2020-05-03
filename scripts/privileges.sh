#!/bin/bash
default_handle=/dev/ttyUSB0
rs232_handle=${1:-$default_handle}
chmod 666 $rs232_handle