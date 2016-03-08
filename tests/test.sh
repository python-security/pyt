if [ $# -eq 0 ]
then
    echo "Input python 3 command as argument."
    exit 1
fi

python3=$(which $1)

echo "LabelVisitor:"
$python3 -m unittest -v label_visitor_test.py

echo ""
echo "VarsVisitor:"
$python3 -m unittest -v vars_visitor_test.py

echo ""
echo "CFG:"
$python3 -m unittest -v cfg_creator_test.py
