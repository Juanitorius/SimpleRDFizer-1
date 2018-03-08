#!/usr/bin/env python

__author__ = 'Kemele M. Endris'

from ontario.rdfizer import *
import getopt, sys


if __name__ == '__main__':
    mappingfile = None
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hm:", ["mappingFile="])
    except getopt.GetoptError:
        print('rdfizer.py -m <mappingFile>')
        sys.exit(1)
#    tasks = '[4]'
    for opt, arg in opts:
        if opt == '-h':
            print('rdfizer.py -m <mappingFile>')
            sys.exit()
        elif opt in ("-m", "--mappingFile"):
            mappingfile = arg
#        elif opt in ("-t", "--tasks"):
#            tasks = arg

    main(mappingfile)
#    main(mappingfile,tasks)
