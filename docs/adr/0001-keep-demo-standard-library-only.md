# ADR 0001: Keep the Demo Standard-Library Only

## Status

Accepted.

## Context

The repo is used for teaching harness engineering. Extra dependencies would add
setup noise and distract from the harness concept.

## Decision

The application and checks use the Python standard library only.

## Consequences

The demo is easy to run on a clean machine. The tradeoff is that linting,
formatting, coverage, and static typing are represented by lightweight local
checks instead of full production-grade tools.
