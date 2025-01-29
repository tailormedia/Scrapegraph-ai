from tests.graphs.abstract_graph_test import TestGraph
import pytest


class TestAbstractGraph:
    def test_invalid_llm_provider(self):
        """
        Test that creating a concrete subclass of AbstractGraph with an invalid LLM provider raises a ValueError
        with the correct error message.
        """
        expected_error_message = "Provider invalid_provider is not supported."
        with pytest.raises(ValueError, match=expected_error_message):
            TestGraph("Test prompt", {"llm": {"model": "invalid_provider/model"}})
