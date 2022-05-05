from solutions.CHK.checkout_solution import checkout


class TestCheckout:

    def test_checkout_illegal_input(self):
        illegal_string_response = "1, 2, 3"
        illegal_non_string_response = ["A, B, C"]

        response_1 = checkout(illegal_string_response)
        response_2 = checkout(illegal_non_string_response)

        assert response_1 == -1
        assert response_2 == -1

    def test_checkout_without_special_offers(self):
        skus = "A, B, C, D"
        total = checkout(skus)
        assert total == 115

    def test_checkout_with_special_offers(self):
        skus = "A, A, A, B, C, D"
        total = checkout(skus)
        assert total == 195

    def test_checkout_with_multiple_special_offers(self):
        skus = "A, A, A, A, A, A, B, C, D"
        total = checkout(skus)
        assert total == 325

