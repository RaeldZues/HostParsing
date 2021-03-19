import pandas as pd
import re
import os


def ioc_extract():
    reMD5 = r"([A-F]|[0-9]){32}"
    reIPv4 = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|\[\.\])){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    reURL = r"[A-Z0-9\-\.\[\]]+(\.|\[\.\])(XN--CLCHC0EA0B2G2A9GCD|XN--HGBK6AJ7F53BBA|" \
            r"XN--HLCJ6AYA9ESC7A|XN--11B5BS3A9AJ6G|XN--MGBERP4A5D4AR|XN--XKC2DL3A5EE0H|XN--80AKHBYKNJ4F|" \
            r"XN--XKC2AL3HYE2A|XN--LGBBAT1AD8J|XN--MGBC0A9AZCG|XN--9T4B11YI5A|XN--MGBAAM7A8H|XN--MGBAYH7GPA|" \
            r"XN--MGBBH1A71E|XN--FPCRJ9C3D|XN--FZC2C9E2C|XN--YFRO4I67O|XN--YGBI2AMMX|XN--3E0B707E|XN--JXALPDLP|" \
            r"XN--KGBECHTV|XN--OGBPF8FL|XN--0ZWM56D|XN--45BRJ9C|XN--80AO21A|XN--DEBA0AD|XN--G6W251D|XN--GECRJ9C|" \
            r"XN--H2BRJ9C|XN--J6W193G|XN--KPRW13D|XN--KPRY57D|XN--PGBS0DH|XN--S9BRJ9C|XN--90A3AC|XN--FIQS8S|" \
            r"XN--FIQZ9S|XN--O3CW4H|XN--WGBH1C|XN--WGBL6A|XN--ZCKZAH|XN--P1AI|MUSEUM|TRAVEL|AERO|ARPA|ASIA|COOP|" \
            r"INFO|JOBS|MOBI|NAME|BIZ|CAT|COM|EDU|GOV|INT|MIL|NET|ORG|PRO|TEL|XXX|AC|AD|AE|AF|AG|AI|AL|AM|AN|AO|AQ|" \
            r"AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BM|BN|BO|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|" \
            r"CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|ER|ES|ET|EU|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|" \
            r"GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|" \
            r"JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MG|MH|MK|ML|MM|MN|MO|" \
            r"MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|" \
            r"PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|ST|SU|SV|SX|SY|SZ|TC|TD|TF|" \
            r"TG|TH|TJ|TK|TL|TM|TN|TO|TP|TR|TT|TV|TW|TZ|UA|UG|UK|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|YE|YT|ZA|ZM|ZW)" \
            r"(/\S+)"
    reDomain = r"[A-Z0-9\-\.\[\]]+(\.|\[\.\])(XN--CLCHC0EA0B2G2A9GCD|XN--HGBK6AJ7F53BBA|XN--HLCJ6AYA9ESC7A|" \
               r"XN--11B5BS3A9AJ6G|XN--MGBERP4A5D4AR|XN--XKC2DL3A5EE0H|XN--80AKHBYKNJ4F|XN--XKC2AL3HYE2A|" \
               r"XN--LGBBAT1AD8J|XN--MGBC0A9AZCG|XN--9T4B11YI5A|XN--MGBAAM7A8H|XN--MGBAYH7GPA|XN--MGBBH1A71E|" \
               r"XN--FPCRJ9C3D|XN--FZC2C9E2C|XN--YFRO4I67O|XN--YGBI2AMMX|XN--3E0B707E|XN--JXALPDLP|XN--KGBECHTV|" \
               r"XN--OGBPF8FL|XN--0ZWM56D|XN--45BRJ9C|XN--80AO21A|XN--DEBA0AD|XN--G6W251D|XN--GECRJ9C|XN--H2BRJ9C|" \
               r"XN--J6W193G|XN--KPRW13D|XN--KPRY57D|XN--PGBS0DH|XN--S9BRJ9C|XN--90A3AC|XN--FIQS8S|XN--FIQZ9S|" \
               r"XN--O3CW4H|XN--WGBH1C|XN--WGBL6A|XN--ZCKZAH|XN--P1AI|MUSEUM|TRAVEL|AERO|ARPA|ASIA|COOP|INFO|JOBS|" \
               r"MOBI|NAME|BIZ|CAT|COM|EDU|GOV|INT|MIL|NET|ORG|PRO|TEL|XXX|AC|AD|AE|AF|AG|AI|AL|AM|AN|AO|AQ|AR|AS|AT" \
               r"|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BM|BN|BO|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|CL|CM|" \
               r"CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|ER|ES|ET|EU|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|" \
               r"GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|JP|" \
               r"KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MG|MH|MK|ML|MM|MN|MO|MP" \
               r"|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|" \
               r"PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|ST|SU|SV|SX|SY|SZ|TC|TD|TF" \
               r"|TG|TH|TJ|TK|TL|TM|TN|TO|TP|TR|TT|TV|TW|TZ|UA|UG|UK|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|YE|YT|ZA|" \
               r"ZM|ZW)\b"
    reEmail = r"\b[A-Za-z0-9._%+-]+(@|\[@\])[A-Za-z0-9.-]+(\.|\[\.\])(XN--CLCHC0EA0B2G2A9GCD|XN--HGBK6AJ7F53BBA|" \
              r"XN--HLCJ6AYA9ESC7A|XN--11B5BS3A9AJ6G|XN--MGBERP4A5D4AR|XN--XKC2DL3A5EE0H|XN--80AKHBYKNJ4F|" \
              r"XN--XKC2AL3HYE2A|XN--LGBBAT1AD8J|XN--MGBC0A9AZCG|XN--9T4B11YI5A|XN--MGBAAM7A8H|XN--MGBAYH7GPA|" \
              r"XN--MGBBH1A71E|XN--FPCRJ9C3D|XN--FZC2C9E2C|XN--YFRO4I67O|XN--YGBI2AMMX|XN--3E0B707E|XN--JXALPDLP|" \
              r"XN--KGBECHTV|XN--OGBPF8FL|XN--0ZWM56D|XN--45BRJ9C|XN--80AO21A|XN--DEBA0AD|XN--G6W251D|XN--GECRJ9C|" \
              r"XN--H2BRJ9C|XN--J6W193G|XN--KPRW13D|XN--KPRY57D|XN--PGBS0DH|XN--S9BRJ9C|XN--90A3AC|XN--FIQS8S|" \
              r"XN--FIQZ9S|XN--O3CW4H|XN--WGBH1C|XN--WGBL6A|XN--ZCKZAH|XN--P1AI|MUSEUM|TRAVEL|AERO|ARPA|ASIA|COOP|" \
              r"INFO|JOBS|MOBI|NAME|BIZ|CAT|COM|EDU|GOV|INT|MIL|NET|ORG|PRO|TEL|XXX|AC|AD|AE|AF|AG|AI|AL|AM|AN|AO|AQ|" \
              r"AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BM|BN|BO|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK" \
              r"|CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|ER|ES|ET|EU|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE" \
              r"|GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|" \
              r"JO|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MG|MH|MK|ML|MM|MN" \
              r"|MO|MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|" \
              r"PN|PR|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|ST|SU|SV|SX|SY|SZ|TC" \
              r"|TD|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TP|TR|TT|TV|TW|TZ|UA|UG|UK|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|YE|YT|" \
              r"ZA|ZM|ZW)\b"

    iocdict = {reMD5:'reMD5', reIPv4: 'reIPv4', reURL: 'reURL', reDomain: 'reDomain', reEmail: 'reEmail'}
    full_host = r"./base_compare"
    output_files = r"./iocs/output"
    sorted_files = r"./iocs/sorted"
    for key, value in iocdict.items():
        for file in os.listdir(full_host):
            with open(os.path.join(full_host, file), 'r', encoding='iso-8859-1') as data:
                text = data.read()            # Instead of with open how can i use pandas to create mutliple columns?
            # This still errors out with list index out of range
            with open(os.path.join(output_files, ("%s_%s.csv" % (str(file).strip('.csv'), value))), 'a',
                      encoding='iso-8859-1') as new_file:
                for m in re.finditer(key, text, re.IGNORECASE):
                    try:
                        m = str(m).split('match=')[-1].split("'")[1]
                        new_file.write(m + '\n')
                    except:
                        pass

    list_output_folder = [x for x in os.listdir(output_files)]
    for item in list_output_folder:
        # This statement removes all files that are blank from the file path
        if os.stat(os.path.join(output_files, item)).st_size == 0:
            os.remove(os.path.join(output_files, item))

    second_list_output_folder = [x for x in os.listdir(output_files)]
    for item in second_list_output_folder:
        print(item)
        # This is the sort unique function from pandas, only accepts single column information
        df = pd.read_csv(os.path.join(output_files, item), header=None,  error_bad_lines=False)
        df = df[0]
        df = df.drop_duplicates()
        df = df.sort_values(ascending=True)
        df = df[0]
        df.to_csv(os.path.join(sorted_files, ('%s.csv' % (str(item).strip('.csv')))))


if __name__ == "__main__":
    ioc_extract()
