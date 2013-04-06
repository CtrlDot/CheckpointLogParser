#! /usr/bin/env python

######
# Log Summary Report
#
# Basically reads in a fw.log file and prints out some useful top 10 stats
#
# Top 10 is determined by number of line matches
#
#
# Written by Shamir Charania
######


import CheckpointLog
import Helper
import argparse
import sys

parser = argparse.ArgumentParser(description="This program provides a Log Summary Report \
                                              on a given log file.  Basically it will try \
                                              and provide an overview of what is in the file \
                                              via some useful top 10 stats")

parser.add_argument("file", help="The logfile to parse.")
args = parser.parse_args()

Helper.PrintTitle("Log Summary")

checkpointLog = CheckpointLog.CheckpointLog(args.file)

mustHaveHeaders = [
                   "Current Rule Number",
                   "Origin",
                   "Source",
                   "Destination",
                   "Service",
                   "Protocol"
                  ]
    
missingHeader = checkpointLog.HasHeaders(mustHaveHeaders)
if not missingHeader == None:
    raise Exception("Log does not contain necessary headers = " + missingHeader)


print 'Parsing {}'.format(args.file)
print 'Log file size: {} bytes'.format(checkpointLog.GetFileSize())
print 'Note: Top 10 determined by number of lines that match'
print ''
print ''

origins = {}
rules = {}
sources = {}
destinations = {}
services = {}
protocols = {}

values = checkpointLog.GetLineByHeader(mustHaveHeaders)
while (len(values)):
    currentRuleName = values[0]
    origin = values[1]
    source = values[2]
    destination = values[3]
    service = values[4]
    protocol = values[5]
    
    Helper.AddToDict(origin,origins)
    Helper.AddToDict(currentRuleName, rules)
    Helper.AddToDict(source,sources)
    Helper.AddToDict(destination,destinations)
    Helper.AddToDict(service,services)
    Helper.AddToDict(protocol, protocols)
    
    values = checkpointLog.GetLineByHeader(mustHaveHeaders)

checkpointLog.Close()

print "Number of lines parsed: {}".format(checkpointLog.GetLinesRead())

Helper.PrintTop10(origins, "Top 10 Origins")
Helper.PrintTop10(rules, "Top 10 Rules")
Helper.PrintTop10(sources, "Top 10 Sources")
Helper.PrintTop10(destinations, "Top 10 Destinations")
Helper.PrintTop10(services, "Top 10 Services")
Helper.PrintTop10(protocols, "Top 10 Protocols")