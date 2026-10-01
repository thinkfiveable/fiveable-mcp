# Fiveable for AP Teachers

Connect your Fiveable teacher workspace to an AI app for AP rubric grading, assignment drafts, question-bank materials, and class insights.

## Connect

Add this remote Streamable HTTP server URL to a client that supports OAuth sign-in:

```text
https://fiveable.me/api/mcp/teacher
```

Sign in with your Fiveable account and review the separate teacher consent screen. There is no local server package or API key to install. This connection is separate from Fiveable for AP Students; student access does not grant teacher workspace access.

Fiveable for AP Teachers is tested in Claude and ChatGPT. Other MCP clients must support remote Streamable HTTP and OAuth; compatibility has not been verified in every client.

### Claude and ChatGPT

Follow the current [teacher setup guide](https://fiveable.me/mcp/teachers) for your app. Start with:

> What can you do with my Fiveable account?

This reads your workspace and helps confirm the connection without changing it.

### Cursor and other MCP clients

Use the teacher-only [mcp.json](mcp.json) configuration, or add the remote URL above through your client's MCP settings. Follow the client's OAuth prompt when it requests account access. This configuration is provided for compatible clients; the teacher workflow has not been independently tested in Cursor.

Do not install the repository's root Gemini extension for teacher access: that extension connects to the student server. A teacher Gemini extension is not included until its OAuth and teacher workflow can be verified.

## What it supports

- Grade pasted or uploaded essays and imported Google Classroom work on the AP rubric, then review draft scores and approve them.
- Pull Fiveable questions with answer keys and stimuli for warm-ups, worksheets, and other class materials.
- Create classes, manage rosters, and build assignment drafts.
- Review class, student, question, topic, and skill results to plan what to reteach.
- Preview student-visible actions before confirming publication, date changes, results release, or sending grades to Google Classroom.

Scores stay drafts until the teacher approves them. Your AI app runs the conversation; scores and class data come from Fiveable. Plan allowances match the teacher workspace on the website; connecting does not bypass them.

## Privacy and control

Students appear to the AI app as a first name, last initial, and anonymous handle. Student emails and account ids are not returned. Essay text is shared with the AI app only when you ask to read a specific response. Your AI provider's privacy settings apply to your chat.

Publishing, changing dates, handing back results, and sending grades to Google Classroom require a preview and confirmation. Disconnect in Fiveable under Account → Integrations → Connected AI apps.

## Documentation and support

- [Teacher setup and overview](https://fiveable.me/mcp/teachers)
- [Teacher documentation](https://fiveable.me/mcp/teachers/docs)
- [Teacher workspace](https://fiveable.me/assignments)
- [Privacy policy](https://fiveable.me/privacy)
- [Terms](https://fiveable.me/terms-of-use)
- Support: [help@fiveable.me](mailto:help@fiveable.me)

This repository contains public metadata for the hosted service. It contains no teacher records or credentials. The production implementation lives in Fiveable's private application repository.

## Official MCP Registry publication

The teacher entry uses `io.github.thinkfiveable/fiveable-ap-teachers`, independently of the student entry. The publishing workflow validates metadata and authenticates with the existing GitHub OIDC permission.

After this metadata is merged to `main`, changes to `teachers/server.json` publish the teacher entry. Maintainers can also dispatch **Publish to MCP Registry** with connector `teachers`, or push a `teachers-v*` release tag. Student `v*` tags and the default manual dispatch still publish the student entry. Increment the relevant server version for each new registry release; registry versions cannot be overwritten.
