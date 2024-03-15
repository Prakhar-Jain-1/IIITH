#!/bin/bash

while true; do
    read -p "Enter a question number (1-5): " i
    if [[ "$i" =~ ^[1-5]$ ]]; then
        folder="q$i"
        
        cd "$folder" || exit 1
        gcc q$i.* -o q$i

        if [ $? -eq 0 ]; then
            ./q$i
        fi

        rm q$i
        cd ..
    else
        echo "Invalid input. Exiting."
        break
    fi
done