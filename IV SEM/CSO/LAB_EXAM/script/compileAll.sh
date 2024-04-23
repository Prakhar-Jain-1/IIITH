cd ../execute
for n in {1..12};
do
    gcc ../codes/q$n/q$n.c ../codes/q$n/q$n.s -o $n
done