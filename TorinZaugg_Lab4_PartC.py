"""
SCADA - Lab 4 Part C
Torin Zaugg
19/10/2018
------
This program connects to a Modus PLC via TCP/IP and runs through a set
of testcases to determine if the PLC is working or not.
"""
#Import the MobdusTcpClient
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

#Import and configure logging
import logging
logging.basicConfig()
log = logging.getLogger()
#log.setLevel(logging.DEBUG) #More verbos
log.setLevel(logging.INFO)  #Less verbos

#PLC Configuratin
## For the purposes of this lab, I will be using ROHRFLOTE as my server running ModbusPLC and
## connecting to it using my MacBookPRO as the client.
#PLCAddress = "192.168.2.8" #Address of the server on my LAN
PLCAddress="192.0.2.130"    #Address of the same server on TOKEN VPN (accessable through college network)
PLCPort = 502

#Common strings
## Strings I print alot are stored here so I'd have to keep typing them out
num = 0
strt = "-=-+-=-+-=-+-=-+-=-+-=-+-=-+-= [TEST CASE # %d] -+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-="
end =  "-=-+-=-+-=-+-=-+-=-+-=-+-=-+ [END TEST CASE # %d] -=-+-=-+-=-+-=-+-=-+-=-+-=-+-=\n\n"

#Custom Methods
## This method converts a list to a decimal number
def toDecimal(list):
    dec = 0
    for n in range(0, len(list)):
        dec = dec + (list[n] * (2**n))
    return dec

## This method converts a string of binary to a string of boolean values
def toBool(binVal):
    valAsStr = ""
    valAsBin = bin(toDecimal(binVal))
    for n in range(2, len(valAsBin)):
        if valAsBin[n] == "1":
            if n == 2:
                valAsStr = valAsStr + "True"
            else:
                valAsStr = valAsStr + ", True"
        elif valAsBin[n] == "0":
            if n == 2:
                valAsStr = valAsStr + "False"
            else:
                valAsStr = valAsStr + ", False"
        else:
            valAsStr = "ERROR"
    return valAsStr

## This method converts a string of binary to a string of boolean but in a different
## way than the method above
def convert(bin):
    splitValue = list(bin)
    valAsBool = ""
    for n in range(0, len(splitValue)):
        if splitValue[n] == "1":
            if n == 0:
                valAsBool = valAsBool + "True"
            else:
                valAsBool = valAsBool + ", True"
        elif splitValue[n] == "0":
            if n == 0:
                valAsBool = valAsBool + "False"
            else:
                valAsBool = valAsBool + ", False"
        else:
            valAsBool = "ERROR"
    return valAsBool

## This method separates binary values
def binSeparator(binVal):
    valSeparated = ""
    for n in range(2, len(binVal)):
        if binVal[n] == "1":
            if n == 2:
                valSeparated = valSeparated + "1"
            else:
                valSeparated = valSeparated + ", 1"
        elif binVal[n] == "0":
            if n == 2:
                valSeparated = valSeparated + "0"
            else:
                valSeparated = valSeparated + ", 0"
        else:
            valSeparated = "ERROR"
    return valSeparated

## This method removes the first two characters of its input string
def rmTwoVal(num):
    NewNum = ""
    for n in range(2, len(num)):
        NewNum = NewNum + num[n]
    return NewNum

## This function checks if the resulted value is equal to the expected value
def resultCheck(result, expect):
    if(result == expect):
        return True
    else:
        return False

#Connect to the PLC
client = ModbusClient(PLCAddress,PLCPort)
client.connect()

"""
Above this line is configuration and connection
-----------------------------------------------
Below this line are test testcases
"""

## TEST CASE 1 ##
# This testcase is supposed to read four coils using function code 1.
# Encoded in these bits is my birthday (02)
# The coil it is encoded in was chosen by my birth month (09)
num = 1
numCoils = 4
startPos = 9
expected = 2
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the status of four coils. My birthday is encoded in those coils."
print "      Expected Result:   %d" % expected
print ""
rc = client.read_coils(startPos, numCoils, unit=0x01)
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print "      Does result = expected?: " + str(resultCheck(toDecimal(list = rc.bits), expected))
print end % num

## TEST CASE 2 ##
# This testcase is supposed to read eight coils using function code 1
# The encoded value is 157
num = 2
numCoils = 8
startPos = 240
expected = 157
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the status of eight coils."
print "      Expected Result:   %d" % expected
print ""
rc = client.read_coils(startPos, numCoils, unit=0x01)
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print "      Does result = expected?: " + str(resultCheck(toDecimal(list = rc.bits), expected))
print end % num

## TEST CASE 3 ##
# This testcase is supposed to read twelve coils using function code 1
# The encoded value is 2306.
num = 3
numCoils = 12
startPos = 496
expected = 2306
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the status of tweve coils."
print "      Expected Result:   %d" % expected
print ""
rc = client.read_coils(startPos, numCoils, unit=0x01)
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print "      Does result = expected?: " + str(resultCheck(toDecimal(list = rc.bits), expected))
print end % num

## TEST CASE 4 ##
# This testcase is supposed to read four imputs using function code 2
# Encoded in these bits is my birthday (02)
# The coil it is encoded in was chosen by my birth month (09)
num = 4
numCoils = 4
startPos = 9
expected = 2
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the status of four inputs. My birthday is encoded in those coils."
print "      Expected Result:   %d" % expected
print ""
rc = client.read_discrete_inputs(startPos, numCoils, unit=0x01)
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print "      Does result = expected?: " + str(resultCheck(toDecimal(list = rc.bits), expected))
print end % num

## TEST CASE 5 ##
# This testcase is supposed to read eight imputs using function code 2
num = 5
numCoils = 8
startPos = 232
expected = 124
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the status of eight discrete inputs."
print "      Expected Result:   %d" % expected
print ""
rc = client.read_discrete_inputs(startPos, numCoils, unit=0x01)
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print "      Does result = expected?: " + str(resultCheck(toDecimal(list = rc.bits), expected))
print end % num

## TEST CASE 6 ##
# This testcase is supposed to read twelve imputs using function code 2
# The encoded value is any twelve-bit number
num = 6
numCoils = 12
startPos = 122
expected = 4095
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the status of twelve discrete inputs. A 12-bit number is encoded in the inputs."
print "      Expected Result:   %d" % expected
print ""
rc = client.read_discrete_inputs(startPos, numCoils, unit=0x01)
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print "      Does result = expected?: " + str(resultCheck(toDecimal(list = rc.bits), expected))
print end % num

## TEST CASE 7 ##
# This testcase is supposed to read one 16UInt using function code 3
# The encoded value is my birthday (02) + 1000. The register is my birthmonth (09).
num = 7
numCoils = 1
startPos = 9
expected = 1002
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the value of one 16UInt. My birthday + 1000 is encoded in the register."
print "      Expected Result:   %d" % expected
print ""
rc = client.read_holding_registers(startPos, numCoils)
print "      Booleans:  [" + toBool(rc.registers) + "]"
print "      Binary:    [" + binSeparator(bin(toDecimal(rc.registers))) + "]"
print "      Decimal:   " + str(toDecimal(rc.registers))
print "      Hex:       " + rmTwoVal(hex(toDecimal(rc.registers)))
print ""
print "      Does result = expected?: " + str(resultCheck(toDecimal(list = rc.registers), expected))
print end % num

## TEST CASE 8 ##
# This testcase is supposed to read two 16UInt using function code 3
# The encoded value is my birth month and day (0902) + 1000 and + 2000.
num = 8
numCoils = 2
startPos = 52
expected = [1902, 2902]
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the value of two 16UInts. My birth month and day (0902) + 1000 and + 2000 is encoded in the register."
print "      Expected Result 1:   %d" % expected[0]
print "      Expected Result 2:   %d" % expected[1]
print ""
rc = client.read_holding_registers(startPos, numCoils, unit=1)
for i in range(0, numCoils):
    print "      Register " + str(i) + ":"
    print "      Booleans:  [" + convert(rmTwoVal(bin(rc.registers[i]))) + "]"
    print "      Binary:    [" + binSeparator(bin(rc.registers[i])) + "]"
    print "      Decimal:   " + str(rc.registers[i])
    print "      Hex:       " + rmTwoVal(hex(rc.registers[i]))
    print "      Does result = expected?: " + str(resultCheck(rc.registers[i], expected[i]))
print end % num

## TEST CASE 9 ##
# Print the value of a 16UInt using function code 4. Encoded is a my birthday (02) + 1000
num = 9
numCoils = 1
startPos = 9
expected = 1902
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the value of a 16UInt using function code 4. Encoded is a my birth month and day (0902) + 1000"
print "      Expected Result:   %d" % expected
print ""
rc = client.read_input_registers(startPos, numCoils)
print "      Booleans:  [" + toBool(rc.registers) + "]"
print "      Binary:    [" + binSeparator(bin(toDecimal(rc.registers))) + "]"
print "      Decimal:   " + str(toDecimal(rc.registers))
print "      Hex:       " + rmTwoVal(hex(toDecimal(rc.registers)))
print "      Does result = expected?: " + str(resultCheck(toDecimal(rc.registers), expected))
print end % num

## TEST CASE 10 ##
# Print the value of three 16UInts using function code 4. Encoded is a my birthday (02) * 10, 20, and 30.
num = 10
numCoils = 3
startPos = 444
expected = [20, 40, 60]
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Print the value of three 16UInts using function code 4. Encoded is a my birthday (02) * 10, 20, and 30."
print "      Expected Result 1:   %d" % expected[0]
print "      Expected Result 2:   %d" % expected[1]
print "      Expected Result 3:   %d" % expected[2]
print ""
rc = client.read_input_registers(startPos, numCoils)
for i in range(0, numCoils):
    print "      Register " + str(i) + ":"
    print "      Booleans:  [" + convert(rmTwoVal(bin(rc.registers[i]))) + "]"
    print "      Binary:    [" + binSeparator(bin(rc.registers[i])) + "]"
    print "      Decimal:   " + str(rc.registers[i])
    print "      Hex:       " + rmTwoVal(hex(rc.registers[i]))
    print "      Does result = expected?: " + str(resultCheck(rc.registers[i], expected[i]))
print end % num

## TEST CASE 11 ##
# Change the value of a single coil
num = 11
numCoils = 1
startPos = 53
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Change the value of a single coil."
print "      Expected Result:  Opposite value of the initial read"
print ""
rc = client.read_coils(startPos, numCoils, unit=0x01)
print "      Original Value:"
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print "      Changing Value"
if(rc.bits[0] == 0):
    rc = client.write_coil(startPos, 1, unit=0x01)
    expected = 1
elif(rc.bits[0] == 1):
    rc = client.write_coil(startPos, 0, unit=0x01)
    expected = 0
else:
    print "AN ERROR HAPPENED"
rc = client.read_coils(startPos, numCoils, unit=0x01)
print ""
print "      New Value:"
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print "      Does result = expected?: " + str(resultCheck(toDecimal(list = rc.bits), expected))
print end % num

## TEST CASE 12 ##
# Change the value of four coils
num = 12
numCoils = 4
startPos = 65
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Change the value of four coils."
print "      Expected Result:  Opposite value of the initial read"
print ""
rc = client.read_coils(startPos, numCoils, unit=0x01)
print "      Original Value"
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print "      Changing Value"
newValue = []
for n in range(0, len(rc.bits)):
    if(rc.bits[n] == 0):
        newValue.append(1)
    elif(rc.bits[n] == 1):
        newValue.append(0)
    else:
        print "AN ERROR HAPPENED"
rc = client.write_coils(startPos, newValue, unit=0x01)
rc = client.read_coils(startPos, numCoils, unit=0x01)
print ""
print "      New Value"
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print end % num

## TEST CASE 13 ##
# Change the value of eight coils
num = 13
numCoils = 4
startPos = 75
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Change the value of eight coils."
print ""
rc = client.read_coils(startPos, numCoils, unit=0x01)
print "      Original Value"
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print ""
print "      Changing Value"
newValue = []
for n in range(0, len(rc.bits)):
    if(rc.bits[n] == 0):
        newValue.append(1)
    elif(rc.bits[n] == 1):
        newValue.append(0)
    else:
        print "AN ERROR HAPPENED"
rc = client.write_coils(startPos, newValue, unit=0x01)
rc = client.read_coils(startPos, numCoils, unit=0x01)
print ""
print "      New Value"
print "      Booleans:  " + str(rc.bits)
print "      Binary:    " + str(map(int, rc.bits))
print "      Decimal:   " + str(toDecimal(list = rc.bits))
print "      Hex:       " + rmTwoVal(hex(toDecimal(list = rc.bits)))
print end % num

## TEST CASE 14 ##
# Write my birth month and day multiplied by 40
# 0902 * 40 = 36080
num = 14
numCoils = 1
startPos = 22
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Write my birth month and day multiplied by 40 (which is 36080)"
print ""
rc = client.read_holding_registers(startPos, numCoils, unit=0x01)
print "      Original Value"
print "      Booleans:  [" + toBool(rc.registers) + "]"
print "      Binary:    [" + binSeparator(bin(toDecimal(rc.registers))) + "]"
print "      Decimal:   " + str(toDecimal(rc.registers))
print "      Hex:       " + rmTwoVal(hex(toDecimal(rc.registers)))
print ""
print "      Changing Value"
rc = client.write_register(startPos, 36080, unit=0x01)
rc = client.read_holding_registers(startPos, numCoils, unit=0x01)
print ""
print "      New Value"
print "      Booleans:  [" + toBool(rc.registers) + "]"
print "      Binary:    [" + binSeparator(bin(toDecimal(rc.registers))) + "]"
print "      Decimal:   " + str(toDecimal(rc.registers))
print "      Hex:       " + rmTwoVal(hex(toDecimal(rc.registers)))
print ""
print "      Changing value back to avoid breaking the program the next time the testcase is ran"
rc = client.write_register(startPos, 512, unit=0x01)
print end % num

## TEST CASE 15 ##
# Write my birthdate multiplied by 10, then 20
num = 15
numCoils = 2
startPos = 72
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Write my birthdate multiplied by 10 then 20"
print ""
rc = client.read_holding_registers(startPos, numCoils, unit=0x01)
print "      Original Value"
for i in range(0, numCoils):
    print "      Register " + str(i) + ":"
    print "      Booleans:  [" + convert(rmTwoVal(bin(rc.registers[i]))) + "]"
    print "      Binary:    [" + binSeparator(bin(rc.registers[i])) + "]"
    print "      Decimal:   " + str(rc.registers[i])
    print "      Hex:       " + rmTwoVal(hex(rc.registers[i]))
print ""
print "      Changing Value"
rc = client.write_register(startPos, 9020, unit=0x01)
rc = client.write_register(startPos+1, 18040, unit=0x01)
rc = client.read_holding_registers(startPos, numCoils, unit=0x01)
print ""
print "      New Value"
for i in range(0, numCoils):
    print "      Register " + str(i) + ":"
    print "      Booleans:  [" + convert(rmTwoVal(bin(rc.registers[i]))) + "]"
    print "      Binary:    [" + binSeparator(bin(rc.registers[i])) + "]"
    print "      Decimal:   " + str(rc.registers[i])
    print "      Hex:       " + rmTwoVal(hex(rc.registers[i]))
print ""
print "      Changing value back to avoid breaking the program the next time the testcase is ran"
rc = client.write_register(startPos, 2324, unit=0x01)
rc = client.write_register(startPos+1, 6782, unit=0x01)
print end % num

## TEST CASE 16 ##
# Write my birthdate multiplied by 10, then 20, then 30
num = 16
numCoils = 3
startPos = 102
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Write my birthdate multiplied by 10, then 20, then 30"
print ""
rc = client.read_holding_registers(startPos, numCoils, unit=0x01)
print "      Original Value"
for i in range(0, numCoils):
    print "      Register " + str(i) + ":"
    print "      Booleans:  [" + convert(rmTwoVal(bin(rc.registers[i]))) + "]"
    print "      Binary:    [" + binSeparator(bin(rc.registers[i])) + "]"
    print "      Decimal:   " + str(rc.registers[i])
    print "      Hex:       " + rmTwoVal(hex(rc.registers[i]))
print ""
print "      Changing Value"
rc = client.write_register(startPos, 9020, unit=0x01)
rc = client.write_register(startPos+1, 18040, unit=0x01)
rc = client.write_register(startPos+2, 27060, unit=0x01)
rc = client.read_holding_registers(startPos, numCoils, unit=0x01)
print ""
print "      New Value"
for i in range(0, numCoils):
    print "      Register " + str(i) + ":"
    print "      Booleans:  [" + convert(rmTwoVal(bin(rc.registers[i]))) + "]"
    print "      Binary:    [" + binSeparator(bin(rc.registers[i])) + "]"
    print "      Decimal:   " + str(rc.registers[i])
    print "      Hex:       " + rmTwoVal(hex(rc.registers[i]))
print ""
print "      Changing value back to avoid breaking the program the next time the testcase is ran"
rc = client.write_register(startPos, 3141, unit=0x01)
rc = client.write_register(startPos+1, 59265, unit=0x01)
rc = client.write_register(startPos+2, 30, unit=0x01)
print end % num

## TEST CASE 17 ##
# Write my name
# Here's how this works:
#   Each register contains one letter of my full name.
#   Torin Zaugg = 11 registers (Torin = 5, Zaugg = 5, the space between the two = 1)
#   I am using python to convert the string "Torin Zaugg" to decimal (ASCII) which is written into each
#   register and printed back out again
name = "Torin Zaugg"
nameSplit = list(name)
default = "Empty Void "
defaultSplit = list(default)
num = 17
numCoils = len(nameSplit)
startPos = 256
print strt % num
print "      Test case: %d" % num
print "      Scenario:   Write my name"
print ""
rc = client.read_holding_registers(startPos, numCoils, unit=0x01)
print "      Original Value"
for i in range(0, numCoils):
    print "      Register " + str(i) + ":"
    print "      Booleans:  [" + convert(rmTwoVal(bin(rc.registers[i]))) + "]"
    print "      Binary:    [" + binSeparator(bin(rc.registers[i])) + "]"
    print "      Decimal:   " + str(rc.registers[i])
    print "      Hex:       " + rmTwoVal(hex(rc.registers[i]))
    print "      ASCII:     " + chr(rc.registers[i])
print ""
print "      Changing Value"
letters = []
for i in range(0,len(nameSplit)):
    letters.append(ord(nameSplit[i]))
rc = client.write_registers(startPos, letters, unit=0x01)
rc = client.read_holding_registers(startPos, numCoils, unit=0x01)
print ""
print "      New Value"
for i in range(0, numCoils):
    print "      Register " + str(i) + ":"
    print "      Booleans:  [" + convert(rmTwoVal(bin(rc.registers[i]))) + "]"
    print "      Binary:    [" + binSeparator(bin(rc.registers[i])) + "]"
    print "      Decimal:   " + str(rc.registers[i])
    print "      Hex:       " + rmTwoVal(hex(rc.registers[i]))
    print "      ASCII:     " + chr(rc.registers[i])
print ""
print "      Changing value back to avoid breaking the program the next time the testcase is ran"
defaults = []
for i in range(0,len(defaultSplit)):
    defaults.append(ord(defaultSplit[i]))
rc = client.write_registers(startPos, defaults,unit=0x01)
print end % num

client.close()
