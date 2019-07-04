for i in {1..24}
do
  if [ "$i" -lt 10 ]; then
    i='0'$i
  fi
  echo "Welcome $i times"
  python tree-height.py < tests/$i  > out
  diff -w out tests/$i.a
done