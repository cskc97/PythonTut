from classa import A


class B:
    def b_method_1(self):
        return 2
    def b_method_2(self):
        a = A()
        val = a.a_method_1()
        return self.b_method_1()+val

    

