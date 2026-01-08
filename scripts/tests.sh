#!/usr/bin/env bash

set -e

echo "Spell check markdown files"
npx cspell --config .spelling-config.json --no-progress "./*.md"
npx cspell --config .spelling-config.json --no-progress "./**/*.md"

npx ts-node ./scripts/lint-markdown.ts

#echo "Running eslint..."
#npx eslint --ignore-path .gitignore --ignore-path .eslintignore ./

echo "Validating scripts..."
npx tsc --noEmit --project ./scripts/tsconfig.json
