#!/usr/bin/env python3
"""Offline mechanical verifier for this public-only static Zenodo mirror.
This verifies mechanical consistency only; approval and rights are separately recorded.
"""
from pathlib import Path
import hashlib,json,sys
base=Path(__file__).resolve().parent
lines=(base/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines()
for line in lines:
  digest,filename=line.split('  ',1)
  p=base/filename
  assert p.is_file(),f'Missing: {filename}'
  assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,f'Hash mismatch: {filename}'
source=(base/'index.html').read_text(encoding='utf-8')
start=source.index('const DATA=')+len('const DATA=')
embedded,off=json.JSONDecoder().raw_decode(source[start:])
disk=json.loads((base/'DATA.json').read_text(encoding='utf-8'))
assert embedded==disk,'DATA.json does not match embedded data'
expected={'catalog':164,'edges':531,'questions_metadata':112,'oin_parent_index':91,'cepsad_cases':75,'cepsad_internal_objections':40,'objections':55,'arguments':19,'question_relations':216,'unresolved_registry_index':37,'AI_interpretive_link_assessments':81}
for name,n in expected.items():
  assert len(embedded[name])==n,(name,len(embedded[name]),n)
held=[v for v in embedded['objections'] if v.get('argument_id')=='ARG-17']
assert len(held)==3 and all(v.get('public_summary') is None and v.get('reviewer_reply_assessment') is None for v in held),'Held objection source text could be included'
assert 'PUBLIC RESEARCH EDITION v1.0 RC9' in source
assert 'PUBLIC RELEASE CANDIDATE RC9' not in source
print('PASS:',len(lines),'verified file hashes; all inventory counts and held-placeholder checks passed.')
print('NOTE: Scientific validity, rights clearance and external mirror approval are NOT certified.')
