# Task 01: Add SLA Classification

## Goal

Add support for routing tickets about SLA breaches or missed response-time
commitments.

## Desired Behavior

When ticket text mentions any of these concepts, route it to the `incident`
queue with `high` priority:

- `sla`
- `service level`
- `missed response`
- `response time`

## Acceptance Criteria

- The new behavior is implemented in `TicketRouter`.
- `cli.py` remains a thin adapter and contains no classification rules.
- Tests cover at least two SLA phrases.
- `python3 scripts/check.py` passes.

## Teaching Notes

This task is deliberately small. The point is to show how a clear harness helps
an agent discover context, make a focused change, and verify it without human
babysitting.
