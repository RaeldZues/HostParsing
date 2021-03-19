import pandas as pd
import os

# output optimization on the ide
pd.set_option('display.width', 500)
pd.set_option('max_colwidth', 15)
pd.set_option('display.max_rows', 8)

'''
This function splits my CSV files based on hostid and renames the file based on the hostid and old filename.
'''


def splitByHID():
    file_dir = r'./collected'
    path = os.listdir(file_dir)
    output_path = r'./base_compare/%s_%s.csv'
    for file in path:
        file_path = os.path.join(file_dir, file)
        if (file.find('autoruns')) == False:
            proc = pd.read_csv(file_path, sep=',', encoding='iso-8859-1', usecols=['hostid','profile','location','itemname',
                                                                                   'enabled','launch_string','launch_file',
                                                                                   'description', 'company', 'is_verified',
                                                                                   'signer', 'version',	'imagepath','file',
                                                                                   'imagesize',	'time']).fillna('Zero')

        else:
            proc = pd.read_csv(file_path, sep=',', encoding='iso-8859-1').fillna('Zero')

        for i in proc[r'hostid'].unique():
                (proc[proc[r'hostid'] == i]).to_csv(output_path % (file.strip('.csv'), i), sep=',' , encoding='iso-8859-1')



'''
Need to figure out how to pass this info into my function after importing it into something else?
'''

if __name__ == "__main__":
    splitByHID()