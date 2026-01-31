#!/bin/bash
set -e

script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "${script_dir}/.."

alfred_dir="$HOME/Library/Application Support/Alfred/Alfred.alfredpreferences/workflows/user.workflow.51FE2278-A1E3-45EC-ACD2-578138BE9DF1/"

cp generate.py "${alfred_dir}"

mkdir -p "${alfred_dir}/dictionary"
cp dictionary/processed.py "${alfred_dir}/dictionary/"
