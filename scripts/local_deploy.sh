#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.."

alfred_dir="$HOME/Library/Application Support/Alfred/Alfred.alfredpreferences/workflows/user.workflow.51FE2278-A1E3-45EC-ACD2-578138BE9DF1/"

cp generate.py "${alfred_dir}"

mkdir -p "${alfred_dir}/dictionary"
cp dictionary/processed.py "${alfred_dir}/dictionary/"
