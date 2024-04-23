clear
# touch out.txt correct.txt
cd ../
for i in {1..100};
do
    python3 testing/testGenerator.py $1 > testCase.txt;
    cat testCase.txt >> testCases.txt
    execute/$1 < testCase.txt >> out.txt;
    python3 testing/q$1.py < testCase.txt >> correct.txt
done
diff out.txt correct.txt
rm out.txt correct.txt testCase.txt testCases.txt