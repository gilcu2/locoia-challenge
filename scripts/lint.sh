#!/usr/bin/env sh

TO_CHECK="
gistapi
tests/
"

ruff check $TO_CHECK
