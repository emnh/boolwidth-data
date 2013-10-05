#!/bin/bash
for i in "$@"; do
    dot -Tpng $i > $i.png
done
gqview $i.png
