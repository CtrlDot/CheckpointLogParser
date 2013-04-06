#! /usr/bin/env python

##########################################
# Log Parser Main
#
#
# Written By Shamir Charania
##########################################

import argparse
import CheckpointLog
import Helper

parser = argparse.ArgumentParser()
parser.add_argument("file",type=str,help="The file to parse")
parser.add_argument("rule",type=str,help="    The rule to search.  This actually searches the \
                                              current rule number column so probably like 555-Policy-Name")

args = parser.parse_args()

Helper.PrintTitle("Rule Analyzer")

checkpointLog = CheckpointLog.CheckpointLog(args.file)

mustHaveHeaders = [
                   "Origin",
                   "Source",
                   "Destination",
                   "Service",
                   "Protocol",
                   "Current Rule Number"
                   ]

missingHeader = checkpointLog.HasHeaders(mustHaveHeaders)
if not missingHeader == None:
    raise Exception("Log does not contain necessary headers = " + missingHeader)

print "Parsing {0}, looking for rule {1}".format(args.file,args.rule)

sources = {}
destinations = {}
origins = {}
protocols = {}
flows = {}

matchingLines = 0

values = checkpointLog.GetLineByHeader(mustHaveHeaders)
while (len(values)):
    origin = values[0]
    source = values[1]
    destination = values[2]
    service = values[3]
    protocol = values[4]
    rule = values[5]
    
    if not (rule == args.rule): 
        values = checkpointLog.GetLineByHeader(mustHaveHeaders)
        continue
    
    Helper.AddToDict(source,sources)
    Helper.AddToDict(destination,destinations)
    Helper.AddToDict("Protocol " + protocol.ljust(5) + " Service: " + service.ljust(20) + " {0} ==> {1}".format(source,destination) ,flows)
    Helper.AddToDict(origin, origins)
    Helper.AddToDict(protocol,protocols)
    matchingLines += 1
    values = checkpointLog.GetLineByHeader(mustHaveHeaders)

checkpointLog.Close()

print "Total lines read {0}".format(checkpointLog.GetLinesRead())
print "Total matching lines {0}".format(matchingLines)
print ""


Helper.PrintTop10(sources,"Sources")
Helper.PrintTop10(destinations,"Destinations")
Helper.PrintTop10(flows,"Flows")
Helper.PrintTop10(origins, "Origins")
Helper.PrintTop10(protocols,"Protocols")