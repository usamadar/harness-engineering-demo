"""Ticket classification rules."""

from harness_demo.ticket import RoutingDecision, Ticket

HIGH_PRIORITY = "high"
NORMAL_PRIORITY = "normal"

SECURITY_QUEUE = "security"
INCIDENT_QUEUE = "incident"
BILLING_QUEUE = "billing"
GENERAL_QUEUE = "general"

SECURITY_TERMS = ("password", "credential", "permission", "suspicious access")
INCIDENT_TERMS = ("production", "outage", "cannot log in", "error", "downtime")
BILLING_TERMS = ("invoice", "payment", "refund", "subscription")


class TicketRouter:
    """Routes support tickets to workflow queues using keyword rules."""

    def classify(self, ticket: Ticket) -> RoutingDecision:
        """Classifies a ticket into a queue and priority.

        Args:
            ticket: Ticket value object containing the text to classify.

        Returns:
            A routing decision with queue, priority, and reason.
        """

        normalized_text = ticket.text.casefold()

        if self._contains_term(normalized_text, SECURITY_TERMS):
            return RoutingDecision(
                queue=SECURITY_QUEUE,
                priority=HIGH_PRIORITY,
                reason="Ticket mentions a security-sensitive access concern.",
            )

        if self._contains_term(normalized_text, INCIDENT_TERMS):
            return RoutingDecision(
                queue=INCIDENT_QUEUE,
                priority=HIGH_PRIORITY,
                reason="Ticket mentions a production-impacting incident.",
            )

        if self._contains_term(normalized_text, BILLING_TERMS):
            return RoutingDecision(
                queue=BILLING_QUEUE,
                priority=NORMAL_PRIORITY,
                reason="Ticket mentions billing or subscription work.",
            )

        return RoutingDecision(
            queue=GENERAL_QUEUE,
            priority=NORMAL_PRIORITY,
            reason="Ticket does not match a specialized routing rule.",
        )

    @staticmethod
    def _contains_term(text: str, terms: tuple[str, ...]) -> bool:
        """Checks whether any configured term appears in normalized text.

        Args:
            text: Normalized ticket text.
            terms: Candidate terms to search for.

        Returns:
            True when at least one term appears in text.
        """

        return any(term in text for term in terms)
