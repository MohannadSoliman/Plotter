
class Validator:
    def __init__(self) -> None:
        """
        Constructor initializing arrays needed for validation
        """
        self.polynomial = ""
        self.min = ""
        self.max = ""
        self.ops = ['+', '*', '^', '/', '-']
        self.double_ops = set([op1 + op2 for op1 in self.ops for op2 in self.ops])
        self.accepted = frozenset('0123456789x.-+*/^() ')
        pass

    def is_unwanted_chars(self):
        """
        Checks if there're un wanted characters
        """
        if set(self.polynomial) <= self.accepted:
            return False
        return True
    
    def is_double_operators(self):
        """
        Checks if there're double operator like : // ** ^^
        """
        for i in range(1, len(self.polynomial)):
            if self.polynomial[i-1:i+1] in self.double_ops:
                return True
        return False

    def is_leading_operators(self):
        """
        Checks if there're leading operators like : *2^x /4*x
        """
        if self.polynomial[0] in self.ops[:-1]:
            return True
        return False

    def is_trailing_operators(self):
        """
        Checks if there're trailing operators like : 4*x+
        """
        if self.polynomial[-1] in self.ops:
            return True
        return False

    def is_unbalanced_brackets(self):
        """
        Checks if there're unbalanced brackets like : 2*(4*x)(
        """
        size = len(self.polynomial)
        if size == 0:
            return True
        if size % 2 == 1:
            return False
        size = 0
        stack = []
        for c in self.polynomial:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if size == 0 or stack.pop() != '(':
                    return True
            size = len(stack)
        if len(stack) != 0:
            return True
        return False
    # DANGEROUS! DO NOT USE ON ITS OWN
    def is_invalid_expression(self):
        """
        As a last chance it checks if the expression can't be evaluated
        for expressions like : 3x 3.2.2*x^4
        """
        x = 1
        try:
            eval(self.polynomial.replace('^', '**'), {}, {'x' : x})
            return False
        except Exception:
            return True

    def is_invalid_range(self):
        """
        Checks if the range contains anything other than numbers
        """
        try:
            float(self.min), float(self.max)
            return False
        except Exception:
            return True


    def validate_expression(self, polynomial, min, max):
        """
        Gathers all the implemented validators and calls them one after the other
        """
        self.polynomial = polynomial.strip()
        self.min = min.strip()
        self.max = max.strip()
        if self.is_unwanted_chars():
            return "Invalid Input!\nOnly Numbers and x, . - + / * ^ Allowed!"
        if self.is_leading_operators():
            return "Invalid Input!\nLeading Operators Not Allowed"
        if self.is_trailing_operators():
            return "Invalid Input!\nTrailing Operators Not Allowed"
        if self.is_double_operators():
            return "Invalid Expression!\nDouble Operators Are Not Allowed!"
        if self.is_unbalanced_brackets():
            return "Invalid Expression!\nUnbalanced Parentheses!"
        if self.is_invalid_expression():
            return "Invalid Expression! Check for:\n- Missing '*' Between Constant and Variable\n- Wrong Decimal Point"
        if self.is_invalid_range():
            return "Invalid Range!\nMake Sure Min and Max Are Numeric"

        return "Success"

