#!/usr/bin/env node

import markdownLint from 'markdownlint'
import config from '../.markdownlint.json'
import * as path from 'path'
import * as fs from 'fs'
import { exit } from 'process'
// Directories to ignore when searching for markdown files:
const ignoreDirs = [ 'node_modules', 'venv', '.venv', 'cdk.out', '.history', 'build' ]

let filenames: string[] = []
getFilenames('.', '.md')

/* Run linter */
const options = { 'config': config, 'files': filenames }

console.log(`\n\nStart markdown linting... checking ${filenames.length} files...\n`)
markdownLint(options, (err, result) => {
  if (err) {
    console.error(`Something went wrong: ${err}` + '\n\n')
    exit(1)
  } else if (result !== undefined && result.toString().length > 0) {
    // lint errors were returned
    console.error(`${result.toString()}\n\n`)
    exit(1)
  } else {
    // all ok!
    console.log('...markdown linting done, all good!\n')
  }
})

/* Get all markdown files in repo */
function getFilenames (startPath: string, filter: string) {
  if (!fs.existsSync(startPath)) {
    console.error(`No directory found for '${startPath}'`)
    return
  }

  const files = fs.readdirSync(startPath)
  for (const file in files) {
    let filename = path.join(startPath, files[ file ])

    // Skip file if any element from ignoreDirs appears
    if (ignoreDirs.some(v => filename.includes(v))) {
      continue
    }

    // Recurse if filename is a directory
    if (fs.lstatSync(filename).isDirectory()) {
      getFilenames(filename, filter)
    } else if (filename.endsWith(filter)) {
      // Add filename if file type is .md
      filenames.push(filename)
    }
  }
}
