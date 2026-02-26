#!/bin/bash

for input in tests/inputs/*.txt
do
  base=$(basename "$input" .txt)

  diff tests/outputs/$base.out tests/expected/$base.out
  if [ -f tests/outputs/$base.atf ]; then
    diff tests/outputs/$base.atf tests/expected/$base.atf
  fi
done