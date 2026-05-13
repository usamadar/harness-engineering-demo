"""Command-line adapter for ticket routing."""

import argparse

from harness_demo.router import TicketRouter
from harness_demo.ticket import Ticket


def build_parser() -> argparse.ArgumentParser:
    """Builds the command-line parser.

    Returns:
        Configured argument parser for the ticket-routing CLI.
    """

    parser = argparse.ArgumentParser(description="Classify support-ticket text.")
    parser.add_argument("text", help="Ticket text to classify.")
    return parser


def main() -> None:
    """Runs the ticket-routing command-line interface."""

    args = build_parser().parse_args()
    decision = TicketRouter().classify(Ticket(args.text))
    print(f"queue={decision.queue}")
    print(f"priority={decision.priority}")
    print(f"reason={decision.reason}")


if __name__ == "__main__":
    main()
