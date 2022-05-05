from solutions.CHK.checkout_solution import checkout


class TestCheckout:

    def test_checkout_illegal_input(self):
        illegal_string_response = "1, 2, 3"
        illegal_non_string_response = ["A, B, C"]

        response_1 = checkout(illegal_string_response)
        response_2 = checkout(illegal_non_string_response)

        assert response_1 == -1
        assert response_2 == -1


