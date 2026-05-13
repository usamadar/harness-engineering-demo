# Task 02: Add Customer Success Routing

## Goal

Add a new `customer_success` queue for account-expansion or onboarding tickets.

## Desired Behavior

Route ticket text to `customer_success` with `normal` priority when it mentions:

- `onboarding`
- `training`
- `adoption`
- `renewal planning`

## Acceptance Criteria

- The new behavior is implemented in `TicketRouter`.
- `cli.py` remains free of classification rules.
- Tests cover at least two customer-success phrases.
- Documentation is updated if the queue list changes.
- `python3 scripts/check.py` passes.

## Teaching Notes

Use this as the second exercise after the SLA task. It is slightly broader
because the architecture docs must change too.
