read -p "Enter a question number (i): " i

folder="q$i"

cd "$folder" || exit 1

gcc q*

if [ $? -eq 0 ]; then
    ./a.out
fi
rm a.out
cd ..