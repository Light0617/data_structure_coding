for i in {1..54}
do
  if [ "$i" -lt 10 ]; then
    i='0'$i
  fi
  echo "Welcome $i times"
  python check_brackets.py < tests/$i > out
  diff -w out tests/$i.a
done