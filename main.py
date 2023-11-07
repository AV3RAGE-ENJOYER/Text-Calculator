class Calculator:

    def __init__(self, max_number):
        self.numbers = {
            0: "ноль",
            1: "один",
            2: "два",
            3: "три",
            4: "четыре",
            5: "пять",
            6: "шесть",
            7: "семь",
            8: "восемь",
            9: "девять",
            10: "десять"
        }

        self._generate_dictionary(max_number)

        self.inv_numbers = {v: k for k, v in self.numbers.items()}

        self.operations = {
            "плюс": "+",
            "минус": "-",
            "умножить": "*",
            "разделить": "/"
        }

    @staticmethod
    def _get_number_rank(n):
        return len(str(n))

    def _get_number_name(self, n):
        if self._get_number_rank(n) == 2:
            match n:
                case 11:
                    return "одиннадцать"
                case 12:
                    return "двенадцать"
                case 13:
                    return "тринадцать"
                case 14:
                    return "четырнадцать"
                case 40:
                    return "сорок"
                case 90:
                    return "девяносто"

            if 13 <= n <= 20:
                return self.numbers[int(str(n)[1])] + "надцать"

            return "test"

        elif self._get_number_rank(n) == 3:
            match n:
                case 100:
                    "сто"

            return

    def _generate_dictionary(self, max_number):
        for i in range(11, max_number):
            self.numbers[i] = self._get_number_name(i)

    def prompt(self, query):
        query_split = query.split()

        if "на" in query_split:
            query_split = list(filter(("на").__ne__, query_split))

        converted_query = ""
        for el in query_split:
            if el in self.inv_numbers:
                converted_query += str(self.inv_numbers[el])

            if el in self.operations:
                converted_query += self.operations[el]

        return self.numbers[eval(converted_query)]


if __name__ == "__main__":
    calc = Calculator(100)
    query = "пять плюс одиннадцать"
    print(calc.prompt(query))
