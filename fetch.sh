#!/bin/bash

# `fetch.sh`: download, unpack, verify the file count, exit non-zero on failure | Recreate `data/raw` with one command |

set -euo pipefail

gunzip UNGDC_1946-2025.tar
tar xf UNGDC_1946-2025.tar
rm UNGDC_1946-2025.tar
rm "./TXT/Session 47 - 1992/.DS_Store-to-UTF-8.txt"
echo "Delete files: $(find ./TXT/ -type f -name '*.txt' | grep -v '[0-9]\{4\}\.txt$')"

echo "Speech files: $(find ./TXT/ -type f -name '*.txt' | wc -l)"
