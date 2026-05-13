"""Tests for ticket routing behavior."""

import unittest

from harness_demo.router import BILLING_QUEUE, GENERAL_QUEUE, INCIDENT_QUEUE, SECURITY_QUEUE
from harness_demo.router import HIGH_PRIORITY, NORMAL_PRIORITY, TicketRouter
from harness_demo.ticket import Ticket


class TicketRouterTest(unittest.TestCase):
    """Covers keyword-based ticket classification."""

    def setUp(self) -> None:
        self.router = TicketRouter()

    def test_classify__mentions_password__routes_to_security(self) -> None:
        decision = self.router.classify(Ticket("I need to reset my password."))

        self.assertEqual(SECURITY_QUEUE, decision.queue)
        self.assertEqual(HIGH_PRIORITY, decision.priority)

    def test_classify__mentions_production_outage__routes_to_incident(self) -> None:
        decision = self.router.classify(Ticket("There is a production outage."))

        self.assertEqual(INCIDENT_QUEUE, decision.queue)
        self.assertEqual(HIGH_PRIORITY, decision.priority)

    def test_classify__mentions_invoice__routes_to_billing(self) -> None:
        decision = self.router.classify(Ticket("I need a copy of my invoice."))

        self.assertEqual(BILLING_QUEUE, decision.queue)
        self.assertEqual(NORMAL_PRIORITY, decision.priority)

    def test_classify__has_no_known_terms__routes_to_general(self) -> None:
        decision = self.router.classify(Ticket("How do I change my profile photo?"))

        self.assertEqual(GENERAL_QUEUE, decision.queue)
        self.assertEqual(NORMAL_PRIORITY, decision.priority)

    def test_ticket__empty_text__raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            Ticket("   ")


if __name__ == "__main__":
    unittest.main()
