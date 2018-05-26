# 1Password migration tool
Export tool for people who can't or don't want to use native 1Password export. This tool will export your documents, groups, items, templates, users and valuts into JSON.

## Requirements
 * python 3 or higher
 * [op](https://support.1password.com/command-line/)

## Usage
 1. Sign in to your 1password account using `op signin ...`
 2. [Export your session](https://support.1password.com/command-line/#appendix-session-management)
 3. Run `python3 export.py` (it will take a while; 1 item per ~3 seconds)

Output of export script is **not encrypted**. I recommend to use openssl.
