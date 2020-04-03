#!/usr/bin/env python
# -*- coding: cp1252 -*-
'''
    Pymodbus Synchronous Client Examples
    --------------------------------------------------------------------------
    
    The following is an example of how to use the synchronous modbus client
    implementation from pymodbus.
    
    It should be noted that the client can also be used with
    the guard construct that is available in python 2.5 and up::
    
    with ModbusClient('127.0.0.1') as client:
    result = client.read_coils(1,10)
    print result
    '''
#---------------------------------------------------------------------------#
# import the various server implementations
#---------------------------------------------------------------------------#


from pymodbus.client.sync import ModbusTcpClient as ModbusClient

#from pymodbus.client.sync import ModbusUdpClient as ModbusClient
#from pymodbus.client.sync import ModbusSerialClient as ModbusClient

#---------------------------------------------------------------------------#
# configure the client logging
#---------------------------------------------------------------------------#


import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


#---------------------------------------------------------------------------#
# choose the client you want
#---------------------------------------------------------------------------#
# make sure to start an implementation to hit against. For this
# you can use an existing device, the reference implementation in the tools
# directory, or start a pymodbus server.
#
# If you use the UDP or TCP clients, you can override the framer being used
# to use a custom implementation (say RTU over TCP). By default they use the
# socket framer::
#
#    client = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
#
# It should be noted that you can supply an ipv4 or an ipv6 host address for
# both the UDP and TCP clients.
#
# There are also other options that can be set on the client that controls
# how transactions are performed. The current ones are:
#
# * retries - Specify how many retries to allow per transaction (default = 3)
# * retry_on_empty - Is an empty response a retry (default = False)
# * source_address - Specifies the TCP source address to bind to
#
# Here is an example of using these options::
#
#    client = ModbusClient('localhost', retries=3, retry_on_empty=True)
#---------------------------------------------------------------------------#

client = ModbusClient('127.0.0.1', port=502)

#client = ModbusClient(method='ascii', port='/dev/pts/2', timeout=1)
#client = ModbusClient(method='rtu', port='/dev/pts/2', timeout=1)

client.connect()

#---------------------------------------------------------------------------#
# specify slave to query
#---------------------------------------------------------------------------#
# The slave to query is specified in an optional parameter for each
# individual request. This can be done by specifying the `unit` parameter
# which defaults to `0x00`
#---------------------------------------------------------------------------#

#--== TEST CASE 1 ----------------------------------------------------------#
print ""
print "TESTCASE 1 ---------------TESTCASE 1------------------TESTCASE 1-----"
print ""
print "READ 8 Output coils starting at coil # 1.  Simulator has the number 12 encoded"
print ""
variable_name = client.read_coils(0, 8)
print " Values of the 8 coils read:"
print variable_name.bits
print "**END OF TESTCASE 1**   **END OF TESTCASE 1**   **END OF TESTCASE 1**"
print ""
#--== **  TEST CASE 1  ** --------------------------------------------------#


#--== TEST CASE 2 ----------------------------------------------------------#
print ""
print "TESTCASE 2 ---------------TESTCASE 2------------------TESTCASE 2-----"
print ""
print "Write the number 12 to coils 1 to 4. "
print ""
variable_name = client.read_coils(0, 3)
print " Values of coils 1 – 4 before being written to"
print variable_name.bits
write_status = client.write_coils(0, [False, False, True, True])
variable_name = client.read_coils(0, 3)
print " Values of coils 1 – 4 after being written to"
print variable_name.bits
print "**END OF TESTCASE 2**   **END OF TESTCASE 2**   **END OF TESTCASE 2**"
print ""
#--== **  TEST CASE 2  ** --------------------------------------------------#




#---------------------------------------------------------------------------#
# example requests
#---------------------------------------------------------------------------#
# simply call the methods that you would like to use. An example session
# is displayed below along with some assert checks. Note that some modbus
# implementations differentiate holding/input discrete/coils and as such
# you will not be able to write to these, therefore the starting values
# are not known to these tests. Furthermore, some use the same memory
# blocks for the two sets, so a change to one is a change to the other.
# Keep both of these cases in mind when testing as the following will
# _only_ pass with the supplied async modbus server (script supplied).
#---------------------------------------------------------------------------#

#rq = client.write_coil(1, True)
#rr = client.read_coils(1,1)
# assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.bits[0] == True)          # test the expected value

#---------------------------------------------------------------------------#
# close the client
#---------------------------------------------------------------------------#

client.close()
