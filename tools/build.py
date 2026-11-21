"""Builds index.html from tools/src.html by embedding the sample data. Run from the tools/ folder: python3 build.py"""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'src.html'), encoding='utf-8').read()
csv = open(os.path.join(here, '..', 'sample_data', 'hdfc_statement_aug-oct_2026.csv'), encoding='utf-8').read()
sms = open(os.path.join(here, '..', 'sample_data', 'bank_sms_nov_2026.txt'), encoding='utf-8').read()
s = s.replace('__SAMPLE_CSV__', json.dumps(csv)).replace('__SAMPLE_SMS__', json.dumps(sms))
open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8').write(s)
print('index.html built')
