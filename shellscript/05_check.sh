#!/usr/bin/env bash
FILE="$1"
if [ -f "$FILE" ]; then
    echo "$FILE があります"
elif [ -d "$FILE" ]; then
    echo "$FILE はディレクトリです"
else
    echo "$FILE は見つかりません"
fi
