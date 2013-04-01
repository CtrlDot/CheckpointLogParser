CheckpointLogParser
===================

A small set of scripts that you can use to parse checkpoint fw.log files.  You have to have a good understanding of what rules you are logging to the fw.log as this will skew the results considerably.  

Currently the program reads the file line by line and parses out the interesting information.  It then compiles all the information and displays it.  Please note that reading large files will take a long time AND consume a lot of memory.  In future releases, I will try to address this.  For now I am working on the basic functionality. 

The fw.log can have various headers etc depending on how it is exported.  The program tries to deal with different orders of headers but you will have to make sure the base set is part of any export.

Code is written in python 2.7.3.  All scripts use argparse.  Use the -h option to get some help on what args are required, etc.

LogSummary.py
--------------
Basically prints out top 10 reports for all required headers.

Required Headers:
 * Current Rule Number
 * Origin
 * Source
 * Destination
 * Service
 * Protocol

RuleAnalyzer.py
-----------------
Analyses a rule.  It will print out the top 10 sources, destinations and "flows".  Flow is basically source to destination with service considerations.  Rule has to match the "Current Rule Number" column.  This should look something like 555-Policy-Name

Required Headers:
 * Current Rule Number
 * Origin
 * Source
 * Destination
 * Service
 * Protocol


