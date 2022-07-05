# Examples

This directory contains a VS code based too that makes http requests against feature servers to more easily test rodeo endpoints in `beta`.

## Installation

The VS Code and the [Rest Client][rest-client] plugin are required to
interactively execute requests.

Additionally, `cloudflared` will need to be installed locally to authenticate
against cloudflare and retrieve and access token.

```
brew install cloudflared
```

Edit the `.env` file to configure which server and account are used. The
cloudflare access token is also saved to this file.

```
$ cp .env.template .env
```

## Usage

A cloudflare access token needs to be generated first and saved to the `.env`
file. The cloudflare access token are short lived and this may need to be
rerun after several minutes.

```
./scripts/auth
```

After the auth script is run, you can use the .http file like normal. The
config values in `.env` will be loaded as variables.

[rest-client][https://marketplace.visualstudio.com/items?itemname=humao.rest-client]
