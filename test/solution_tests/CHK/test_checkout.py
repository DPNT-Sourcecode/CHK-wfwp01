from solutions.CHK.checkout_solution import checkout


class TestCheckout:

    def test_checkout_illegal_input(self):
        invalid_string_input = "1, 2, 3"
        invalid_non_string_input = ["A, B, C"]
        invalid_string_input_non_alpha = "-"
        invalid_string_lowercase = "abcd"

        response_1 = checkout(invalid_string_input)
        response_2 = checkout(invalid_non_string_input)
        response_3 = checkout(invalid_string_input_non_alpha)
        response_4 = checkout(invalid_string_lowercase)

        assert response_1 == -1
        assert response_2 == -1
        assert response_3 == -1
        assert response_4 == -1

    def test_checkout_without_special_offers_sku_not_in_price_table(self):
        skus = "ABCX"
        total = checkout(skus)
        assert total == 100

    def test_checkout_without_special_offers(self):
        skus = "A, B, C, D"
        total = checkout(skus)
        assert total == 115

    def test_checkout_with_empty_skus(self):
        skus = ""
        total = checkout(skus)
        assert total == 0

    def test_checkout_with_special_offers(self):
        skus = "A, A, A, B, C, D"
        total = checkout(skus)
        assert total == 195

    def test_checkout_with_multiple_special_offers(self):
        skus = "A, A, A, A, A, A, B, C, D"
        total = checkout(skus)
        assert total == 325



