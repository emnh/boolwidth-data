for i in `seq -w 0 50 450`; do wget 'http://people.cs.uu.nl/hansb/treewidthlib/search.php?data_mode=known+bounds&offset='$i -O page$i.html ; done
