# ADR 0002: Route Business Rules Through TicketRouter

## Status

Accepted.

## Context

The app has a CLI and a classifier. Without a boundary, future changes could put
classification rules in the CLI because it is the easiest file to edit.

## Decision

All classification rules live in `TicketRouter`. The CLI remains an adapter that
parses input, invokes the router, and prints the decision.

## Consequences

Tests can focus on one business-rule module. The CLI stays simple, and agents
have a clear place to make routing changes.
