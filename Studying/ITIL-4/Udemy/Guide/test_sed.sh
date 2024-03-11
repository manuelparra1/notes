#!/bin/bash

sed -n '/^Test.*$/p; /# Question/p; /^##.*$/p' Test_02_Attempt_02.txt > temp_file.txt
sed '/^##.*$/N; s/\n\(^[A-Z].*$\)\n/\n### \1\n/' temp_file.txt > formatted_file.txt
sed '/^>.*$/d; /Explanation/N; s/\n\n\(Explanation\)\n/\r\r*\1*\r/' formatted_file.txt > temp_file.txt
mv temp_file.txt formatted_file.txt

echo "Formatting complete! Check formatted_file.txt"
