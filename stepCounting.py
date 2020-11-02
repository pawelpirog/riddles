class App:

    def solve(self, n):
        global result

        if (n > 0):

            self.solve(n - 1)
            if (n > 1):
                self.solve(n - 2)
        else:
            result += 1

        return result


    def assertEqual(self, param, param1):
        print(param)
        print(param1)

        if (param == param1):
            print("tr")
            return True
        print("f")
        return False


result=0
app = App()
app.assertEqual(app.solve(4), 5)

