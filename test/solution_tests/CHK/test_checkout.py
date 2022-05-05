from solutions.CHK.checkout_solution import checkout


class TestCheckout:

    def test_checkout_illegal_input(self):
        invalid_string_input = "1, 2, 3"
        invalid_non_string_input = ["A, B, C"]
        empty_string_input = ""
        invalid_string_input_non_alpha = "-"

        response_1 = checkout(invalid_string_input)
        response_2 = checkout(invalid_non_string_input)
        response_3 = checkout(empty_string_input)
        response_4 = checkout(invalid_string_input_non_alpha)

        assert response_1 == -1
        assert response_2 == -1
        assert response_3 == -1
        assert response_4 == -1

    def test_checkout_without_special_offers_lower_case_skus(self):
        skus = "a, b, c, d"
        total = checkout(skus)
        assert total == 115

    def test_checkout_without_special_offers_lower_case_skus_and_no_spaces(self):
        skus = "abcd"
        total = checkout(skus)
        assert total == 115

    def test_checkout_without_special_offers_sku_not_in_price_table(self):
        skus = "abcx"
        total = checkout(skus)
        assert total == 100

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

