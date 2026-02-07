#!/bin/bash
set -e

script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "${script_dir}/.."

plutil -lint workflow/info.plist

mkdir -p /tmp/alfred-password-gen
mkdir -p /tmp/alfred-password-gen/dictionary

cp workflow/icon.png /tmp/alfred-password-gen
cp workflow/info.plist /tmp/alfred-password-gen

cp generate.py /tmp/alfred-password-gen
cp dictionary/processed.py /tmp/alfred-password-gen/dictionary

version=$(cat workflow/version)
sed -i '' "s/VERSION_PLACEHOLDER/$version/g" /tmp/alfred-password-gen/info.plist

cd /tmp/alfred-password-gen

zip -r archive.zip *

cd "${script_dir}"/..
mv /tmp/alfred-password-gen/archive.zip password-generator.alfredworkflow
