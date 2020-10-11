for i in `seq 12 1000`
do
    python testdata.py > tests/sample-${i}.in
done
