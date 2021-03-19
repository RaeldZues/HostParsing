import pandas as pd
"""
Dependencies:
    filtered list  = Hashes not in NSRL Database and not in baseline
    collected list = Original filehasher.csv file containing file paths

This can be MD5's or SHA1's does not matter. From the run directory this will create a folder and output
matches of specific file types that are in the filtered list.

file types exported = [ dlls exe msi bat vbs scr pif cmd ps1 ps2 js application jar vb vbs ]
"""


def hash_lookup():
    print('YOU ARE NOW DOING THE HASH LOOKUP')
    # This is for printing to screen formatting
    pd.set_option('display.width', 500)
    pd.set_option('max_colwidth', 200)
    pd.set_option('display.max_rows', 80)
    # This file should be the csv file from the original filehasher export per hostid
    collected_orignal = pd.read_csv(r'./nsrl/collected/filehasher.csv', usecols=['filepath', 'hash'],
                                    encoding='iso-8859-1')
    # This is the filtered file from the nsrl database
    filtered = pd.read_csv(r'./nsrl/output/collected_nsrl_diffed.csv', names=['index', 'hash'], encoding='iso-8859-1')
    # This is a join statement to find the path
    results = filtered.merge(collected_orignal, on='hash', how='inner')
    filepath = results['filepath'].str.split('.')

    # This creates seperate files for each file type thats interesting for us.
    # Need to figure out how to scale this? Seperate folders by hostid?
    print('     Filtering DLLs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'dll']).to_csv(r'./nsrl/output/dlls.csv')
    print('     Filtering EXEs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'exe']).to_csv(r'./nsrl/output/exes.csv')
    print('     Filtering PS1s to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'ps1']).to_csv(r'./nsrl/output/ps1s.csv')
    print('     Filtering PIFs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'pif']).to_csv(r'./nsrl/output/pif.csv')
    print('     Filtering applications to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'application']).to_csv(r'./nsrl/output/application.csv')
    print('     Filtering MSIs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'msi']).to_csv(r'./nsrl/output/msi.csv')
    print('     Filtering SCRs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'scr']).to_csv(r'./nsrl/output/scr.csv')
    print('     Filtering JARs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'jar']).to_csv(r'./nsrl/output/jar.csv')
    print('     Filtering BATs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'bat']).to_csv(r'./nsrl/output/bat.csv')
    print('     Filtering CMDs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'cmd']).to_csv(r'./nsrl/output/cmd.csv')
    print('     Filtering VBs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'vb']).to_csv(r'./nsrl/output/vb.csv')
    print('     Filtering VBSs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'vbs']).to_csv(r'./nsrl/output/vbs.csv')
    print('     Filtering JSs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'js']).to_csv(r'./nsrl/output/js.csv')
    print('     Filtering VBEs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'vbe']).to_csv(r'./nsrl/output/vbe.csv')
    print('     Filtering PS2s to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'ps2']).to_csv(r'./nsrl/output/ps2.csv')
    print('     Filtering cpls to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'cpl']).to_csv(r'./nsrl/output/cpl.csv')
    print('     Filtering coms to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'com']).to_csv(r'./nsrl/output/com.csv')
    print('     Filtering gadgets to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'gadget']).to_csv(r'./nsrl/output/gadget.csv')
    print('     Filtering infs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'inf']).to_csv(r'./nsrl/output/inf.csv')
    print('     Filtering inss to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'ins']).to_csv(r'./nsrl/output/ins.csv')
    print('     Filtering inxs to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'inx']).to_csv(r'./nsrl/output/inx.csv')
    print('     Filtering isus to a new file!')
    (results[['hash', 'filepath']][filepath.str[-1] == 'isu']).to_csv(r'./nsrl/output/isu.csv')

if __name__ == "__main__":
    hash_lookup()
