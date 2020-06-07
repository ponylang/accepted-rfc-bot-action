# Accepted-RFC-bot action

Create assets associated with an accepted Pony RFC after it's PR has been merged to master in the [RFC repo](https://github.com/ponylang/rfcs).

## Example workflow

```yml
name: Accepted RFC Bot

on:
  push:
    branches:
      - master

jobs:
  accepted-rfc-bot:
    runs-on: ubuntu-latest
    name: Complete RFC process
    steps:
      - name: Complete
        uses: ponylang/accepted-rfc-bot-action@initial
        with:
          git_user_name: "Ponylang Main Bot"
          git_user_email: "ponylang.main@gmail.com"
        env:
          API_CREDENTIALS: ${{ secrets.RFC_TOKEN }}
```

`API_CREDENTIALS` must be a personal access token with `public_repo` access to both the [rfc repo](https://github.com/ponylang/rfcs) and the [ponyc repo](https://github.com/ponylang/ponyc).
