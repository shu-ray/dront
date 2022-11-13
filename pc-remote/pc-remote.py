import keyboard
import time
import simplepyble

key_state = False
def is_bump(key):
    global key_state
    if key != key_state:
        if key_state == False:
            key_state = True
            return True
        if key_state == True:
            key_state = False
            return False
    return -1

# Select my only adapter
adapter = simplepyble.Adapter.get_adapters()[0]
adapter.set_callback_on_scan_start(lambda: print("Scan started."))
adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
adapter.set_callback_on_scan_found(lambda peripheral: print(f"Found {peripheral.identifier()} [{peripheral.address()}]"))

# Scan for 5 seconds
adapter.scan_for(5000)
peripherals = adapter.scan_get_results()

# Query the user to pick a peripheral
print("Please select a peripheral:")
for i, peripheral in enumerate(peripherals):
    print(f"{i}: {peripheral.identifier()} [{peripheral.address()}]")
choice = int(input("Enter choice: "))
peripheral = peripherals[choice]

print(f"Connecting to: {peripheral.identifier()} [{peripheral.address()}]")
peripheral.connect()
print("Successfully connected, listing services...")
services = peripheral.services()
service_characteristic_pair = []
for service in services:
    for characteristic in service.characteristics:
        service_characteristic_pair.append((service.uuid, characteristic))

# Query the user to pick a service/characteristic pair
print("Please select a service/characteristic pair:")
for i, (service_uuid, characteristic) in enumerate(service_characteristic_pair):
    print(f"{i}: {service_uuid} {characteristic}")
choice = int(input("Enter choice: "))
service_uuid, characteristic_uuid = service_characteristic_pair[choice]

# peripheral.write_command is for expected write and the versa is p.write_request

while True:
    #print(is_bump(keyboard.is_pressed("ctrl+alt+z")))
    if print(keyboard.is_pressed("w")):
        peripheral.write_command(service_uuid,characteristic_uuid,1)
    if print(keyboard.is_pressed("d")):
        peripheral.write_command(service_uuid,characteristic_uuid,2)
    if print(keyboard.is_pressed("s")):
        peripheral.write_command(service_uuid,characteristic_uuid,3)
    if print(keyboard.is_pressed("a")):
        peripheral.write_command(service_uuid,characteristic_uuid,4)
    time.sleep(0.1)