import Telnet
import time
host = "192.168.0.1"

tn = Telnet(host)
tn.read_until(b"Username:")
tn.write(b"admin")

time.sleep(3)

tn.read_until(b"Password:")
tn.write(b"admin123")

time.sleep(3)

tn.read_until(b"server")
tn.write(b"system-view")

tn.write(b"interface g0/0/2")
time.sleep(3)

