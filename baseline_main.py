import time
import os
import ioc_extractor as extract
import filetypeLookup as lookup
import nsrldiff
import Baseline_process as bp
import split_hostid as hid
import lowercase as lc


def main():
    # This is the start of the running of functions
    folder_create()
    lc.lower_cased()
    time.sleep(3)
    hid.splitByHID()
    time.sleep(3)
    bp.baseline()
    time.sleep(3)
    nsrldiff.nsrl_diff()
    time.sleep(3)
    lookup.hash_lookup()
    time.sleep(3)
    extract.ioc_extract()
    time.sleep(3)


def folder_create():
    # This makes the directory paths if you have nothing setup.
    if not os.path.exists('./collected'):
        os.makedirs('./collected')
    if not os.path.exists('./base_compare'):
        os.makedirs('./base_compare')
    if not os.path.exists('./baseline'):
        os.makedirs('./baseline')
    if not os.path.exists('./base_diff'):
        os.makedirs('./base_diff')
    if not os.path.exists('./stackranked'):
        os.makedirs('./stackranked')
    if not os.path.exists('./nsrl'):
        os.makedirs('./nsrl')
    if not os.path.exists('./nsrl/collected'):
        os.makedirs('./nsrl/collected')
    if not os.path.exists('./nsrl/output'):
        os.makedirs('./nsrl/output')
    if not os.path.exists('./iocs'):
        os.makedirs('./iocs')
    if not os.path.exists('./iocs/output'):
        os.makedirs('./iocs/output')
    if not os.path.exists('./iocs/sorted'):
        os.makedirs('./iocs/sorted')
main()