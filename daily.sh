#!/bin/bash

DAY_DIR="$1"

if [ -z "$DAY_DIR" ]; then
    echo "Usage: ./daily.sh weekly_transactions/day1"
    exit 1
fi

if [ ! -d "$DAY_DIR" ]; then
    echo "Error: folder '$DAY_DIR' does not exist."
    exit 1
fi

echo "=== Running $DAY_DIR ==="

rm -f transactions/session_*.atf
rm -f transactions/merged.atf
rm -f transactions/daily_transactions.atf

shopt -s nullglob
session_files=("$DAY_DIR"/session*.txt)
shopt -u nullglob

if [ ${#session_files[@]} -eq 0 ]; then
    echo "Error: no session files found in '$DAY_DIR'."
    exit 1
fi

SESSION_NUM=1

for session_file in "${session_files[@]}"
do
    echo "Running $session_file ..."
    python3 frontend.py accounts.txt transactions/session_${SESSION_NUM}.atf < "$session_file"
    SESSION_NUM=$((SESSION_NUM + 1))
done

cat transactions/session_*.atf > transactions/merged.atf

grep -v "^00$" transactions/merged.atf > temp.atf
echo "00" >> temp.atf
mv temp.atf transactions/merged.atf

cp transactions/merged.atf transactions/daily_transactions.atf

python3 backend/backend.py

echo "=== Finished $DAY_DIR ==="