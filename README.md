# MCP AI Demo Target

This repository is a clean live target for demonstrating the MCP Engineering Operations Platform.

It contains a manual GitHub Actions workflow that can create a deterministic failed build for a `payments-api` scenario. The MCP platform can investigate this repository through governed GitHub MCP tools.

## Demo Prompt

```text
Check why the latest GitHub build failed, inspect logs and recent changes, create an issue if it is code-related, and ask approval before rerunning the workflow.
```
