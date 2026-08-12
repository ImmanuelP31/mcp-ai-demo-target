def validate_payment_payload(payload: dict) -> bool:
    """Small demo file used as changed-code evidence for MCP demos."""
    return bool(payload.get("amount")) and bool(payload.get("currency"))

# Demo source-code change for MCP investigation: 2026-08-12T09:08:25Z
