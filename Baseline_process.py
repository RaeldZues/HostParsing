import pandas as pd
import os

pd.set_option('display.width', 500)
pd.set_option('max_colwidth', 50)
pd.set_option('display.max_rows', 8)


def baseline():
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


# This is the core base comparison portion. Copy a single elif/if statement for new additions changing pertinents.
    for file in os.listdir(base_compare):
        if file.find('process') == False:
            print(file)
            columns = ['name', 'command_line', 'description', 'exe_path']
            base = (pd.read_csv(process_baseline, encoding='iso-8859-1',
                                usecols=['name', 'command_line', 'description', 'exe_path'])).apply(
                lambda s: s.str.replace('"', "")).fillna(0)
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1',
                                   usecols=['name', 'command_line', 'description', 'exe_path'])).apply(
                lambda s: s.str.replace('"', "")).fillna(0)
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(diff_path, file), sep=',')
            print('Process Listing Diff: \n')
            print(y)

        elif (file.find('chedule') == False):
            columns = ['task_name', 'author', 'task_to_run_path', 'task_to_run', 'start_in', 'run_as_user', 'schedule_type']
            base = (pd.read_csv(scheduled_baseline, encoding='iso-8859-1',
                                usecols=['task_name', 'author', 'task_to_run_path', 'task_to_run', 'start_in', 'run_as_user',
                                         'schedule_type'])).apply(lambda s: s.str.replace('"', "")).fillna(0)
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1',
                                   usecols=['task_name', 'author', 'task_to_run_path', 'task_to_run', 'start_in', 'run_as_user',
                                            'schedule_type'])).apply(lambda s: s.str.replace('"', "")).fillna(0)
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(diff_path, file), sep=',')
            print('Scheduled Tasks diff: \n')
            print(y)

        elif (file.find('ervice') == False):
            columns = ['name', 'path_name', 'file_args', 'start_mode', 'start_name', 'description']
            base = (pd.read_csv(service_baseline, encoding='iso-8859-1',
                                usecols=['name', 'path_name', 'file_args', 'start_mode', 'start_name', 'description']))\
                                .apply(lambda s: s.str.replace('"', "")).fillna(0)
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1',
                                   usecols=['name', 'path_name', 'file_args', 'start_mode', 'start_name',
                                            'description'])).apply(lambda s: s.str.replace('"', "")).fillna(0)
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(diff_path, file), sep=',')
            print('Services listing diff: \n')
            print(y)

        elif (file.find('autorun') == False):
            columns = ['profile', 'location', 'itemname', 'launch_string', 'launch_file', 'signer', 'imagepath', 'file']
            base = (pd.read_csv(autoruns_baseline, encoding='iso-8859-1',usecols=['profile', 'location', 'itemname',
                                            'launch_string', 'launch_file', 'signer','imagepath',
                                            'file'])).apply(lambda s: s.str.replace('"', "")).fillna(0)
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1',usecols=['profile',
                                            'location', 'itemname', 'launch_string', 'launch_file', 'signer',
                                            'imagepath', 'file'])).apply(lambda s: s.str.replace('"', "")).fillna(0)
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(diff_path, file), sep=',')
            print('Autoruns listing diff: \n')
            print(y)

        elif (file.find('oftware') == False):
            columns = ['name', 'comments', 'publisher', 'install_location', 'display_name']
            base = (pd.read_csv(software_baseline, encoding='iso-8859-1',
                                usecols=['name', 'comments', 'publisher', 'install_location', 'display_name'])).apply(
                lambda s: s.str.replace('"', "")).fillna('ZERO')
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1',
                                   usecols=['name', 'comments', 'publisher', 'install_location', 'display_name'])).apply(
                lambda s: s.str.replace('"', "")).fillna('ZERO')
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(diff_path, file), sep=',')
            print('Software listing diff: \n')
            print(y)

        elif (file.find('dll') == False):
            columns = ['executing_prog', 'executing_cmdpath', 'dll_pathname', 'file', 'verified', 'publisher']
            base = (pd.read_csv(dlls_baseline, encoding='iso-8859-1',
                                usecols=['executing_prog', 'executing_cmdpath', 'dll_pathname', 'file', 'verified',
                                         'publisher'])).apply(lambda s: s.str.replace('"', "")).fillna('ZERO')
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1',
                                   usecols=['executing_prog', 'executing_cmdpath', 'dll_pathname', 'file', 'verified',
                                            'publisher'])).apply(lambda s: s.str.replace('"', "")).fillna('ZERO')
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(diff_path, file), sep=',')
            print('DLL Listing Diff: \n')
            print(y)

        elif (file.find('module') == False):
            columns = ['process_name', 'file_path', 'file_name', 'md5']
            base = (pd.read_csv(dlls_baseline, encoding='iso-8859-1',usecols=['process_name', 'file_path', 'file_name', 'md5'])
                    ).apply(lambda s: s.str.replace('"', "")).fillna('ZERO')
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1',
                                   usecols=['process_name', 'file_path', 'file_name', 'md5'])
                       ).apply(lambda s: s.str.replace('"', "")).fillna('ZERO')
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(diff_path, file), sep=',')
            print('DLL Listing Diff: \n')
            print(y)

        elif (file.find('filehasher') == False):
            print(file)
            columns = ['filepath', 'hash']
            base = (pd.read_csv(md5_baseline, encoding='iso-8859-1', usecols=['filepath', 'hash'])).apply(
                lambda s: s.str.replace('"', "")).fillna('ZERO')
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1',
                                   usecols=['filepath', 'hash'])).apply(lambda s: s.str.replace('"', "")).fillna(
                'ZERO')
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(hash_path, file), sep=',')
            print('MD5 hashes Diff: \n')
            print(y)


        elif (file.find('fire') == False):
            print(file)
            columns = ['rule_name', 'enabled', 'direction', 'profile', 'grouping', 'localip', 'remoteip', 'protocol',
                       'localport', 'remoteport', 'edge_traversal', 'action']
            base = (pd.read_csv(firewall_baseline, encoding='iso-8859-1', usecols=['rule_name', 'enabled', 'direction', 'profile', 'grouping', 'localip', 'remoteip', 'protocol',
                       'localport', 'remoteport', 'edge_traversal', 'action'])).apply(lambda s: s.str.replace('"', "")).fillna(0)
            collect = (pd.read_csv((os.path.join(base_compare, file)), encoding='iso-8859-1', usecols=['rule_name', 'enabled', 'direction', 'profile', 'grouping', 'localip', 'remoteip', 'protocol',
                       'localport', 'remoteport', 'edge_traversal', 'action'])).apply(lambda s: s.str.replace('"', "")).fillna(0)
            full = [base, collect]
            x = pd.concat(full, keys=['base', 'collect'])
            y = x.drop_duplicates(subset=columns, keep=False)
            y = y.ix['collect']
            y.to_csv(os.path.join(diff_path, file), sep=',')
            print('Firewall configuration Diff: \n')
            print(y)

if __name__ == "__main__":
    baseline()





