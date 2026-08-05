#!/usr/bin/env python3
from pathlib import Path
import hashlib, sys
root = Path(__file__).resolve().parents[1]
failures = []
for algo, fname in [('sha256','SHA256SUMS.txt'), ('sha512','SHA512SUMS.txt')]:
    mf = root/'verification'/fname
    for line in mf.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        expected, rel = line.split('  ', 1)
        p = root/rel
        h = hashlib.new(algo)
        with p.open('rb') as f:
            for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
        if h.hexdigest()!=expected:
            failures.append(f'{algo} {rel}')
if failures:
    print('FAIL')
    print('\n'.join(failures))
    sys.exit(1)
print('PASS: all repository-tree manifest entries verified.')
