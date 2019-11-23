#!/usr/bin/env bash


# difference between $() ${} ``
# https://stackoverflow.com/questions/27472540/difference-between-and-in-bash/27472808
# commnad substitution: `` or $()
# execute what's inside and replace it.

# ${} is just to disambiguate. e.g. ${var}text

# if-else decision
if [ cond ]; then
  echo "if block"
else
  echo "else block"
fi

# if file exists
if [[ -f "filename"]]; then
  echo "exisits"
fi

# if file does not exist
if [[ -e "filename"]]; then
  echo "exisits"
fi


# for loops: like c systax
for (( c=1; c<=5; c++ )) 
do
  echo "Welcome $c times" 
done

for VARIABLE in "file1" "file2" "file3"
do
  echo "$VARIABLE"
done
# split string


