"""Matrix Prossessing"""
class Matrix:
    def show_menu(self):
        """
        Display the menu and process user's choice.
        """
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: >").strip()
        if choice[0] == "1":
            self.add_matrix()
        if choice[0] == "2":
            self.multiply_matrix_by_const()
        if choice[0] == "3":
            self.multiply_matrices()
        if choice[0] == "4":
            self.transpose_menu()
        if choice[0] == "5":
            print(f"Determinant is {self.determinant()}")
        if choice[0] == "6":
            print(self.getMatrixInverse())
        if choice[0] == "0":
            return exit()

    def transpose_menu(self):
        """
        Display transpose menu and process user's choice.
        :return exit code if user`s input is 0
        """
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")

        choice = input("Your choice: >").strip()
        if choice[0] == "1":
            self.transposeMatrix()
        if choice[0] == "2":
            self.side_diagonal()
        if choice[0] == "3":
            self.vertical()
        if choice[0] == "4":
            self.horizontal()
        if choice[0] == "0":
            return exit()

    def create_matrix(self):
        """
        Create a 1-dimensional matrix based on user input.
        :return None
        """
        try:
            self.n = input("Enter number of row and columns separated by space:\n")
            self.n = self.n.split()
            self.m = int(self.n[1])
            self.n = int(self.n[0])
            print(f"{self.m} is m \n n is {self.n}")
            self.matrix = []
            for i in range(self.n):
                row = list(map(float, input().split()))
                self.matrix.extend(row)
            self.print_matrix()
        except: ValueError("You need to enter numbers")

    def print_matrix(self):

        """
        Method for printing matrix
        :return: None
        """
        for i in range(self.n):
            print(self.matrix[self.m*i:self.m*i+self.m])

    def add_matrix(self):
        """
        Method for adding two matrix
        :param another_matrix: list | matrix that we want to add to ours
        :return: None
        """
        try:
            print("Enter the first matrix")
            self.create_matrix()
            print("Enter the second Matrix")
            another_matrix = Matrix()
            another_matrix.create_matrix()
            if self.n == another_matrix.n and self.m == another_matrix.m:
                for i in range(self.n):
                    for k in range(self.m):
                        self.matrix[self.m * i + k] = self.matrix[self.m * i + k] + another_matrix.matrix[self.m * i + k]
                print(f"Your new Matrix is")
                self.print_matrix()
            else:
                print("Matrix's is not equal")
        except: AttributeError(print("You need to enter numbers"))

    def multiply_matrix_by_const(self):
        """
        Method for multiplying matrix by user`s input
        :return: None
        """
        try:
            self.create_matrix()
            const = int(input("Enter the const: >"))
            for i in range(self.n):
                for k in range(self.m):
                    self.matrix[self.m * i + k] = self.matrix[self.m * i + k] * const
            print(f"Your new Matrix is {self.print_matrix()}")
        except: AttributeError(print("You need to enter numbers"))

    def multiply_matrices(self):
        """
        method for multiply matrix`s
        :return: None
        """
        try:
            print("Enter the first matrix")
            self.create_matrix()
            print("Enter the second Matrix")
            another_matrix = Matrix()
            another_matrix.create_matrix()
            if self.m == another_matrix.n:
                result = []
                for i in range(self.n):
                    for j in range(another_matrix.m):
                        element_sum = 0
                        for k in range(self.m):
                                element_sum += self.matrix[i * self.m + k] * another_matrix.matrix[k * another_matrix.m + j]
                        result.append(element_sum)
                self.m = another_matrix.m
                print("Результат умножения матриц:")
                self.matrix = result
                self.print_matrix()
            else:
                print("Impossible to multiply. Rows and columns are not the same")
        except: AttributeError(print("You need to enter numbers"))

    def transpose_matrix(self, matrix=None):
        """
        Transpose the matrix.
        :return: a:array | transposed matrix
        """
        if matrix == None:
            print("Enter the first matrix")
            matrix = self.one_dimention_to_2_dimention()
        print("The result is")
        # Создаем пустую матрицу для транспонирования
        transposed_matrix = []
        # Проходимся по столбцам исходной матрицы
        for j in range(len(matrix[0])):
            # Создаем новую строку для транспонированной матрицы
            new_row = []
            # Проходимся по строкам исходной матрицы
            for i in range(len(matrix)):
                # Добавляем элемент в новую строку
                new_row.append(matrix[i][j])
            # Добавляем новую строку в транспонированную матрицу
            transposed_matrix.append(new_row)
        return transposed_matrix

    def side_diagonal(self):
        """
        Transpose the matrix by its side diagonal.
        :return: None
        """
        print("Enter the  matrix")
        self.create_matrix()
        print("The result is")
        for i in range(self.m):
            print(self.matrix[-1-i::-self.m])

    def vertical(self):
        """
        Transpose the matrix by its vertical line.
        :return: None
        """
        print("Enter the  matrix")
        self.create_matrix()
        print("The result is")
        for i in range(self.m):
            a = self.matrix[self.m * i:self.m*i+self.m]
            print(a[::-1])

    def horizontal(self):
        """
        Transpose the matrix by its horizontal line.
        :return: None
        """
        print("Enter the  matrix")
        self.create_matrix()
        print("The result is")
        for i in range(self.n):
            print(self.matrix[self.m * self.n - self.m*(i+1):(self.m * self.n) - self.m * i])

    def one_dimention_to_2_dimention(self):
        """
        Convert the one-dimensional matrix to two-dimensional.
        :return: two-dimensional matrix
        """
        print("Enter the  matrix")
        self.create_matrix()
        arr = []
        for i in range(self.m):
            arr.append(self.matrix[self.m * i:self.m * i + self.m])
        return arr

    def get_matrix_minor(self, m, i, j):
        """
        Get the minor of the matrix.
        i: index of row we want to exclude
        j: index of column we want to exclude
        """
        result = []  # Создаем пустой список для хранения результатов

        # Проходимся по каждой строке матрицы, кроме строки с индексом i
        for row in (m[:i] + m[i + 1:]):
            # Выбираем элементы строки от начала до j (не включая j) и от j+1 до конца
            new_row = row[:j] + row[j + 1:]
            # Добавляем новую строку в список результатов
            result.append(new_row)

        return result  # Возвращаем полученный список


    def determinant(self, m=None):
        """
        Calculate determinant of the matrix.
        m: matrix
        :return num | determinant of matrix
        """
        # Если матрица не передана, преобразуем ее из одномерного представления
        if m is None:
            m = self.one_dimention_to_2_dimention()
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        # Если размер матрицы больше 2x2, используем рекурсию для вычисления определителя

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * self.determinant(self.getMatrixMinor(m, 0, c))
        return determinant

    def get_matrix_inverse(self):
        """
        Find the inverse of the matrix.
        :return: array | inverse matrix
        """
        # создание двумерной матрицы
        m = self.one_dimention_to_2_dimention()
        determinant = self.determinant(m)
        # Случай для матрицы 2x2
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

        #Находим матрицу алгебраических дополнений (кофакторов)
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = self.getMatrixMinor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * self.determinant(minor))
            cofactors.append(cofactorRow)
        # Транспонируем матрицу алгебраических дополнений
        cofactors = self.transposeMatrix(cofactors)
        # Делим каждый элемент транспонированной матрицы алгебраических дополнений на определитель
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors


my_matrix = Matrix()

while True:
    my_matrix.show_menu()
