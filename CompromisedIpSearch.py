#! /usr/bin/env python

##############################################
##  Tries to find communication with known compromised ips
##
##
##
## Written by Shamir Charania
##############################################

import Helper
import urllib2
import CheckpointLog
import argparse

def AddDShieldResultsTo(dict):
    print "Importing latest dshield results, limit 5000"
    data = (urllib2.urlopen("http://www.dshield.org/ipsascii.html?limit=5000")).read().splitlines()
    for line in data:
        if line.startswith('#') or line == '':
            continue
        linesplit = line.split()
        dict[Helper.DeleteLeadingZerosFromIP(linesplit[0])] = 'dshield'

parser = argparse.ArgumentParser(description="This program downloads various bad ip lists \
                                                and then searches the checkpoint log for those \
                                                addresses")

parser.add_argument("file", help="The logfile to parse.")
parser.add_argument("--all", help="Prints all flows rather than top 10", action='store_true')
args = parser.parse_args()

Helper.PrintTitle("Compromised IP Search")
    
    
ipAddressesToFind = {}
AddDShieldResultsTo(ipAddressesToFind)

checkpointLog = CheckpointLog.CheckpointLog(args.file)

mustHaveHeaders = [
                   'Source',
                   'Destination',
                   'Service',
                   'Protocol'
                   ]

missingHeader = checkpointLog.HasHeaders(mustHaveHeaders)
if not missingHeader == None:
    raise Exception("Log does not contain necessary headers = " + missingHeader)

flows = {}

values = checkpointLog.GetLineByHeader(mustHaveHeaders)
while (len(values)):
    source = values[0]
    destination = values[1]
    service = values [2]
    protocol = values[3]
    
    if (source in ipAddressesToFind):
        Helper.AddToDict("Protocol " + protocol.ljust(5) + " Service: " + service.ljust(20) + " {0} ==> {1}".format(source,destination) + " ::::List Source:" + ipAddressesToFind[source] ,flows)
        
        
    if (destination in ipAddressesToFind):
        Helper.AddToDict("Protocol " + protocol.ljust(5) + " Service: " + service.ljust(20) + " {0} ==> {1}".format(source,destination) + " ::::List Source:" + ipAddressesToFind[destination],flows)
    
    values = checkpointLog.GetLineByHeader(mustHaveHeaders)

checkpointLog.Close()

if args.all:
    Helper.PrintAll(flows,"Flows")
else:
    Helper.PrintTop10(flows, "Flows")
