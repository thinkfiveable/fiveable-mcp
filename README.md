# Fiveable for AP Students

Use Fiveable's AP study content and student study tools inside MCP-compatible AI apps.

## Teacher connector

Looking for grading and class prep? [Fiveable for AP Teachers](teachers/README.md) is a separate connector with its own endpoint and OAuth consent. The root extension and configuration in this repository remain student-only.

## Connect

Add this remote Streamable HTTP endpoint to your MCP client:

```text
https://fiveable.me/api/mcp
```

There is no package to install and no API key to copy. Public discovery and limited content previews work without a Fiveable account. Personal progress and saved actions use Fiveable OAuth.

### Cursor

This repository includes a Cursor plugin manifest and an `mcp.json` configuration for the hosted Fiveable server. In Cursor, open **Customize → MCPs**, add a remote server, and use:

```text
https://fiveable.me/api/mcp
```

Cursor will open Fiveable's OAuth flow when a personalized tool needs account access.

### Gemini CLI

Install this repository as a Gemini CLI extension:

```bash
gemini extensions install https://github.com/thinkfiveable/fiveable-mcp
```

Gemini CLI connects to the hosted Fiveable MCP through the extension. Run `/mcp auth fiveable-ap-students` to connect a Fiveable account for personalized tools.

## What it supports

- AP subjects, units, study guides, key terms, and relevant passages
- Multiple-choice practice and adaptive diagnostics
- Fiveable and student-supplied FRQ scoring
- AP score calculators
- Personal progress, study plans, and completed exam results
- Official Fiveable cheatsheets
- Student-accessible assignment summaries with released feedback

The connector is student-only. It does not expose teacher rosters, active answer keys, internal moderation tools, or another student's data.

## Documentation and support

- [Fiveable for AP Students documentation](https://fiveable.me/mcp/docs)
- [Setup guides](https://fiveable.me/mcp#client-setup)
- [Privacy policy](https://fiveable.me/privacy)
- [Terms](https://fiveable.me/terms)
- Support: [help@fiveable.me](mailto:help@fiveable.me)

## Security

Fiveable uses OAuth 2.1 with PKCE for connected tools. Please report security issues through Fiveable's published security contact rather than a public GitHub issue.

This repository contains public metadata and documentation for the hosted service. The production server implementation lives in Fiveable's private application repository.
