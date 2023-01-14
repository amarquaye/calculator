"""
A simple calculator application made using beeware
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial


class Calculator(toga.App):

    def startup(self):
        
        main_box = toga.Box(style=Pack(direction=COLUMN,flex=1))
        main_input_box = toga.Box(style=Pack(direction=ROW))
        self.main_input = toga.TextInput(style=Pack(padding=5,flex=1))
        main_input_box.add(self.main_input)
        main_box.add(main_input_box)

        # Creating a first row to take 7 to +
        first_row = toga.Box(style=Pack(direction=ROW,flex=1))

        # Creating buttons
        # Button 7
        but7 = toga.Button('7',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='7'))
        # Button 8
        but8 = toga.Button('8',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='8'))
        # Button 9
        but9 = toga.Button('9',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='9'))
        # Addition button
        addbut = toga.Button('+',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='+'))

        
        # Adding buttons to the first row
        first_row.add(but7,but8,but9,addbut)

        # Adding firstrow to the mainbox
        main_box.add(first_row)

        
        # Creating second row for   4 to -
        second_row = toga.Box(style=Pack(direction=ROW,flex=1))

        # Button 4
        but4 = toga.Button('4',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='4'))
        # Button 5
        but5 = toga.Button('5',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='5'))
        # Button 6
        but6 = toga.Button('6',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='6'))
        # Minus button
        minus_but = toga.Button('-',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='-'))

        # Adding them to seconr row
        second_row.add(but4,but5,but6,minus_but)

        # Adding second row to main box
        main_box.add(second_row)

        
        # Creating third row for 1 t0 x
        # Creating third row
        third_row = toga.Box(style=Pack(direction=ROW,flex=1))
        # Button 1
        but1 = toga.Button('1',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='1'))
        # Button 2
        but2 = toga.Button('2',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='2'))
        # Button 3
        but3 = toga.Button('3',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='3'))
        # Multiplication button
        mult_but = toga.Button('X',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='*'))

        # Adding the buttons to third row
        third_row.add(but1,but2,but3,mult_but)

        # Adding third row to main box
        main_box.add(third_row)


        # Creating fourth row for . to /
        #Creating fourth row
        fourth_row = toga.Box(style=Pack(direction=ROW,flex=1))
        # Creating buttons
        # Decimal butto.
        dec_but = toga.Button('.',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='.'))
        # Zero button
        zero_but = toga.Button('0',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='0'))
        # Clear button
        clear_but = toga.Button('C',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='C'))
        # Division button
        div_but = toga.Button('/',style=Pack(flex=1,padding=20),on_press=partial(self.enterdata,number='/'))

        # Adding the buttons to the fourth row
        fourth_row.add(dec_but,zero_but,clear_but,div_but)

        # Adding fourth row to main box
        main_box.add(fourth_row)


        # Creating last row
        last_row = toga.Box(style=Pack(direction=ROW,flex=1))
        # Creating equal button
        equal_but = toga.Button('=',style=Pack(flex=1,padding=20),on_press=self.calculate)

        # Adding equal button to last row
        last_row.add(equal_but)
        # Adding last row to main box
        main_box.add(last_row)





        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def enterdata(self, widget, number):
        """Function to print entered data"""
        if (number == 'C'):
            self.main_input.value = ''
        else:
            self.main_input.value = self.main_input.value + number

    def calculate(self, widget):
        """Function to display calculated data"""
        output = eval(self.main_input.value)
        self.main_input.value = str(output)
        


def main():
    return Calculator()
