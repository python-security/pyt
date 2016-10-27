# This script uses the pydepgraph to draw a dependency graph between modules
# install pydepgraph from your linux package manager

pydepgraph -p pyt/ -g 1 | dot -Tpng -o graph.png
xdg-open graph.png
