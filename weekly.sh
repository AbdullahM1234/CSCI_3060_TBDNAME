#!/bin/bash

echo "=== Running weekly simulation ==="

for day in weekly_transactions/day1 weekly_transactions/day2 weekly_transactions/day3 weekly_transactions/day4 weekly_transactions/day5 weekly_transactions/day6 weekly_transactions/day7
do
    echo "----- $day -----"
    ./daily.sh "$day"
done

echo "=== Weekly simulation complete ==="