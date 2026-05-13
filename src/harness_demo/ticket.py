"""Value objects for ticket routing."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Ticket:
    """Represents support-ticket text submitted for queue classification.

    Args:
        text: User-provided ticket text.

    Raises:
        ValueError: Raised when ticket text is empty or only whitespace.
    """

    text: str

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("Ticket text cannot be empty.")


@dataclass(frozen=True)
class RoutingDecision:
    """Represents the queue and priority selected for a ticket.

    Args:
        queue: Workflow queue that should handle the ticket.
        priority: Relative urgency assigned to the ticket.
        reason: Human-readable explanation of the routing decision.
    """

    queue: str
    priority: str
    reason: str
