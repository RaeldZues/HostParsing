import pandas as pd
import re
import os

def ioc_extract():
    print('YOU HAVE STARTED YOUR BASELINE COMPARISON')
    # Variables for code
    process_baseline = r'./baseline/processlisting_full.csv'
    service_baseline = r'./baseline/services_full.csv'
    autoruns_baseline = r'./baseline/autoruns_full.csv'
    scheduled_baseline = r'./baseline/scheduledTasks.csv'
    software_baseline = r'./baseline/software_full.csv'
    dlls_baseline = r'./baseline/dlls_full.csv'
    firewall_baseline = r'./baseline/firewall_full.csv'
    modules_baseline = r'./baseline/modules_full.csv'
    md5_baseline = r'./baseline/md5_full.csv'
    diff_path = r'./base_diff'
    base_compare = r'./base_compare'
    hash_path = r'./nsrl/collected'

    for file in os.listdir(base_compare):
        if (file.find('filehasher') == False):
            print(file)
            columns = ['filepath', 'hash']
            base = (pd.read_csv(md5_baseline, encoding='iso-8859-1', usecols=['filepath', 'hash'])).apply(lambda s: s.str.replace('"', "")).fillna('ZERO')
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1', usecols=['filepath', 'hash'])).apply(lambda s: s.str.replace('"', "")).fillna('ZERO')
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(hash_path, file), sep=',')
            print('MD5 hashes Diff: \n')
            print(y)

if __name__ == "__main__":
    ioc_extract()