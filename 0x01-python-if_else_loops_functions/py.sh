#!/bin/bash
for file in *.py
do
  echo '#!/usr/bin/python3' > "$file"
done
