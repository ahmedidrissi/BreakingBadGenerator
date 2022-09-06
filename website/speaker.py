import pyttsx3 
import periodictable as prd
#-----------------------------------------------------------------------------------------

class Speaker(object):
    def __init__(self, name, symbols):
        # initialise the pyttsx3 engine 
        self.name = name
        self.symbols = symbols
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')  #getting details of voices
        self.engine.setProperty('voice', self.voices[1].id)  #changing index, changes voices.
        self.engine.setProperty('rate', 160)  #changing speed
    
    def speak(self):
        self.engine.say(self.name)
        self.engine.runAndWait()
        self.engine.stop()

    def readSymbols(self):
        text = ''
        for symbol in self.symbols:
            text += prd.elements.symbol(symbol).name + ', '
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()

    def symbolInfos(self):
        for symbol in self.symbols:
            if symbol != 'none':
                self.name = prd.elements.symbol(symbol).name
                z = prd.elements.symbol(symbol).number
                mass = prd.elements.symbol(symbol).mass
                density = prd.elements.symbol(symbol).density
                self.speak()
                if len(symbol) == 1:
                    smbl = symbol
                if len(symbol) == 2:
                    smbl = symbol[0] + ' ' + symbol[1]
                elif len(symbol) == 3:
                    smbl = symbol[0] + ' ' + symbol[1] + ' ' + symbol[2]
                self.name = 'symbol: ' + smbl
                self.speak()
                self.name = 'atomic number: ' + str(z)
                self.speak()
                self.name = 'mass: ' + str(mass)
                self.speak()
                self.name = 'density: '+ str(density)
                self.speak()