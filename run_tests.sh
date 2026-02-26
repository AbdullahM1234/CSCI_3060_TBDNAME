#!/bin/bash

for input in tests/inputs/*.txt
do
  base=$(basename "$input" .txt)

  python3 frontend.py accounts.txt tests/outputs/$base.atf < "$input" > tests/outputs/$base.out
done