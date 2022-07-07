# Examples

This directory contains a VS code based too that makes http requests against feature servers to more easily test API endpoints. It works like CURL

## Installation

The VS Code and the [Rest Client][rest-client] plugin are required to
interactively execute requests.

[rest-client][https://marketplace.visualstudio.com/items?itemname=humao.rest-client]

Edit the `.env` file to configure which server and account are used. 


## Usage

A cloudflare access token needs to be generated first and saved to the `.env`
file. The cloudflare access token are short lived and this may need to be
rerun after several minutes.

```
./scripts/auth
```

After the auth script is run, you can use the .http file like normal. The
config values in `.env` will be loaded as variables.


