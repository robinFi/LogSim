from AndGate import AndGate
from OrGate import OrGate
class LogFunc:
    def executeAnd(self):
        input0 = bool(input('Bitte geben Sie den Wert für input0 an. Mit einer Eingabe setzen Sie ihn auf True. Ohne jegliches Zeichen wird der Wert auf False gesetzt.\n'))
        if input0 != True:
            input0 = False
        else:
            input0 = True
        input1 = bool(input('Bitte geben Sie den Wert für input1 an. Mit einer Eingabe setzen Sie ihn auf True. Ohne jegliches Zeichen wird der Wert auf False gesetzt.\n'))
        if input1 != True:
            input1 = False
        else:
            input1 = True
        und = AndGate(input0, input1)
        und.execute()
        und.show()

    def executeOr(self):
        input0 = bool(input('Bitte geben Sie den Wert für input0 an. Mit einer Eingabe setzen Sie ihn auf True. Ohne jegliches Zeichen wird der Wert auf False gesetzt.\n'))
        if input0 != True:
            input0 = False
        else:
            input0 = True
        input1 = bool(input('Bitte geben Sie den Wert für input1 an. Mit einer Eingabe setzen Sie ihn auf True. Ohne jegliches Zeichen wird der Wert auf False gesetzt.\n'))
        if input1 != True:
            input1 = False
        else:
            input1 = True
        oder = OrGate(input0, input1)
        oder.execute()
        oder.show()

    def Main(self):
        
        print('Willkommen zum Projekt LogSim.\n')
        a = 1
        while a == 1:
            wahl = input('Wählen Sie ihr gewünschtes Logikgatter aus. Schreiben Sie ein A für AND und ein O für Or: ')
            if wahl == 'A' or wahl == 'O':
                if wahl == 'A':
                    LF.executeAnd()
                    erneut = input('Wünschen Sie eine erneute Nutzung? Bitte geben Sie "Ja" ein falls dem so ist. Bei anderer Eingabe wird das Programm beendet.\n' )
                    if erneut == 'Ja':
                        print('Das Programm wird erneut ausgeführt.')
                        print('\n')
                        print('\n')
                        print('\n')
                    else:
                        a = 0
                else:
                    LF.executeOr()
                    erneut = input('Wünschen Sie eine erneute Nutzung? Bitte geben Sie "Ja" ein falls dem so ist. Bei anderer Eingabe wird das Programm beendet.\n' )
                    if erneut == 'Ja':
                        print('Das Programm wird erneut ausgeführt.')
                        print('\n')
                        print('\n')
                        print('\n')
                    else:
                        a = 0
            else:
                print('Fehlerhafte Eingabe. Bitte versuchen Sie es ernueut.\n')
    
        exit()

LF = LogFunc()
LF.Main()