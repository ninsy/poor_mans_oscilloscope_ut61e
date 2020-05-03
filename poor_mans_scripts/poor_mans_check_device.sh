#!/bin/bash
# You are supposed to plug-in/out your USB-RS232 within 5 secs ;)
diff <(lsusb -v) <(sleep 5 && lsusb -v) > poor_mans_diff.txt
