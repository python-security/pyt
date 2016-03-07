echo "LabelVisitor:"
python -m unittest label_visitor_test.py

echo ""
echo "VarsVisitor:"
python -m unittest vars_visitor_test.py

echo ""
echo "CFG:"
python -m unittest cfg_creator_test.py
