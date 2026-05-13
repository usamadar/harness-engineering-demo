# Architecture

The app classifies support-ticket text into a queue and priority. It is small
on purpose so the harness is easy to see.

## Modules

- `ticket.py` defines the value objects used by the app.
- `router.py` contains classification rules.
- `cli.py` is a thin command-line adapter around the router.

## Design Rules

- `TicketRouter` is the only place where classification decisions live.
- `cli.py` should not contain business rules.
- `Ticket` and `RoutingDecision` should remain simple value objects.
- New rules must be covered by tests in `tests/test_router.py`.

## Classification Model

Queues:

- `security`: passwords, credentials, permissions, suspicious access.
- `incident`: production outages, login failures, errors, downtime.
- `billing`: invoices, payments, refunds, subscriptions.
- `general`: everything else.

Priorities:

- `high`: security or incident queue.
- `normal`: billing or general queue.
