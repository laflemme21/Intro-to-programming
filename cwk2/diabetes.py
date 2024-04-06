"""
Please write your name
@author: Karl Samuel Kassis

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Diabetes:
    def __init__(self, filepath: str) -> None:
        # assign list to 0 to later check if file was opened
        self.list = 0
        try:
            open(filepath, 'r')
        except FileNotFoundError:
            pass
        else:
            self.list = []
            # puts each line in the list
            with open(filepath, 'r') as file:
                self.list = file.readlines()
            # splits each line into a list of words
            for i in range(len(self.list)):
                self.list[i] = self.list[i].split(',')
                if self.list[i][-1][-1] == '\n':
                    self.list[i][-1] = self.list[i][-1][:-1]
            # defines the header and data
            self.header = self.list[0]
            self.data = [self.list[i] for i in range(1, len(self.list))]

    def get_dimension(self) -> list:
        # checks if the file was opened to avoid errors
        if self.list != 0:
            return [len(self.list)-1, len(self.list[0])]

    def web_summary(self, filepath: str) -> None:
        # checks if the file was opened to avoid errors
        if self.list != 0:
            # writes all of the headers of the table
            file = open(filepath, "w")
            file.write(
                '<style>\ntable, th, td {\nborder: 2px solid black;\n')
            file.write(
                'border-color: #96D4D4;\nborder-collapse: collapse;\n}\n')
            file.write(
                'tr:nth-child(even) {background-color: #D6EEEE;}</style>\n')
            file.write(
                '<table style="width:30%">\n<tr>\n  <th rowspan')
            file.write(
                ' = 3 style="width:50%">Attributes</th>')
            file.write(
                '<th colspan = 4 style="width:50%">Class</th>\n')
            file.write(
                '</tr>\n<tr>\n<th colspan=2 style="width:25%">positive</th>')
            file.write(
                '<th colspan = 2 style="width:25%">negative</th>\n')
            file.write(
                '</tr>\n<tr>\n<td style="width:12.5%">yes</td>\n')
            file.write(
                '<td style="width:12.5%">no</td>\n<td ')
            file.write(
                'style="width:12.5%">yes</td>\n')
            file.write('<td style="width:12.5%">no</td>\n</tr>')
            # counts the number of positive and negative yes and no
            # and puts them in a html table
            for i in range(len(self.list[0])):
                if self.list[0][i] != 'Age' and (
                    self.list[0][i] != 'Gender') and (
                    self.list[0][i] != 'class') and (
                        self.list[0][i] != 'gender') and (
                            self.list[0][i] != 'Class') and (
                                self.list[0][i] != 'age'):
                    Pos_yes = 0
                    Pos_no = 0
                    Neg_yes = 0
                    Neg_no = 0
                    for j in range(1, len(self.list)):
                        if self.list[
                            j][i] == 'Yes' or self.list[
                                j][i] == 'yes':
                            if self.list[
                                j][
                                self.list[
                                    0].
                                index
                                ('class' or 'Class')] == 'Positive' or (
                                self.list[j][
                                    self.list[0].
                                    index
                                    ('class' or 'Class')] == 'positive'):
                                Pos_yes += 1
                            else:
                                Neg_yes += 1
                        else:
                            if self.list[
                                j][
                                self.list[0].
                                index
                                ('class' or 'Class')] == 'Positive' or (
                                self.list[j][
                                    self.list[0].
                                    index
                                    ('class' or 'Class')] == 'positive'):
                                Pos_no += 1
                            else:
                                Neg_no += 1
                    file.write('<tr>')
                    file.write('<td>'+self.list[0][i]+'</td>')
                    file.write('<td>'+str(Pos_yes)+'</td>')
                    file.write('<td>'+str(Pos_no)+'</td>')
                    file.write('<td>'+str(Neg_yes)+'</td>')
                    file.write('<td>'+str(Neg_no)+'</td>')
                    file.write('</tr>')
            file.write("</table>\n")

    def count_instances(self, criteria: dict) -> int:
        """
        returns the number of lines in the file
        that countain specific caracteristics

        :param criteria: caracteristics to search for
        :type criteria: dictionnary
        :rtype: int
        :return: number of lines containing the caracteristics

        to use this method you need a variable of the type Diabetes
        print(var.count_instances(
        {'Polyuria': 'No', 'Gender': 'Female', 'class': 'Positive'}))
        the dictionnary can countain as many arguments
        as there are arguments in the header and
        has to be of the form {'arg in header':value,...}

        """
        n = []
        for i in range(len(self.list)):
            n.append(self.list[i])
        for key, value in criteria.items():
            i = 0
            key = self.list[0].index(key)
            while i < len(n):
                if n[i][key] != value:
                    n.pop(i)
                    i -= 1
                i += 1
        return len(n)


if __name__ == '__main__':
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    # d1.count_instances() # change according to your criteria
    print(d1.count_instances(
        {'Polyuria': 'No', 'Gender': 'Female', 'class': 'Positive'}))

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    # d2.count_instances()  # change according to your criteria
    print(d2.count_instances(
        {'Polyuria': 'No', 'Gender': 'Female', 'class': 'Positive'}))
