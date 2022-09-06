import periodictable as prd
from PIL import Image, ImageDraw, ImageFont, ImageFilter
#-----------------------------------------------------------------------------------------

class BreakingBadGenerator(object):
    def __init__(self, name, background):
        self.name = name
        self.symbols = []
        self.background = background

    def findSymbols(self):  
        splited_name = self.name.split()
        pile = []
        for word in splited_name:
            for i in range(len(word)):
                try:
                    symbol = word[i].upper() + word[i+1] # like Al, Br, Ba...
                    prd.elements.symbol(symbol) #To check if it's an element
                    self.symbols.append(symbol)
                    pile.append(1)
                    break # because it's founded
                except : # index error or not an element
                    try:
                        symbol = word[i].upper() # like C, O, H...
                        prd.elements.symbol(symbol) #To check if it's an element
                        self.symbols.append(symbol)
                        pile.append(1)
                        break # because it's found
                    except : # not an element 
                        continue
                    
            if len(pile) == 0: # No symbol is found
                self.symbols.append('none') 
            else:
                pile.pop() # square_size symbol is found
        return self.symbols
                
    def rewriteName(self):
        splited_name = self.name.split()
        wordsNum = len(splited_name)
        newName = [[]*i for i in range(wordsNum)]
        for j in range(wordsNum):
            i = 0
            symbol_found = False
            while i < len(splited_name[j]):
                if self.symbols[j] == splited_name[j][i].upper() and symbol_found == False:
                    newName[j].append(self.symbols[j])
                    symbol_found = True
                else:
                    try:
                        if self.symbols[j] == splited_name[j][i].upper() + splited_name[j][i+1] and symbol_found == False:
                            newName[j].append(self.symbols[j])
                            symbol_found = True
                            i+=1
                        else:
                            newName[j].append(splited_name[j][i])
                    except:
                        newName[j].append(splited_name[j][i])
                i += 1
                
        return newName

    def findSquareSize(self, new_name, bg_width, bg_heigth):
        wordsNum = len(new_name)
        max_word = new_name[0]
        for word in new_name:
            if len(word)>len(max_word):
                max_word = word
        square_size_1 = bg_width//len(max_word)
        square_size_2 = bg_heigth//wordsNum
        return min(square_size_1, square_size_2)

    def addSquare(self, bg_width, bg_heigth, square_size):
        draw = ImageDraw.Draw(self.background, mode="RGBA")
        draw.rectangle((bg_width,bg_heigth,bg_width+square_size, bg_heigth+square_size), fill=(0,120,40,200) ,outline="white", width=4)

    def addText(self, caractere, element, z, mass, bg_width, bg_heigth, square_size, font):
        z_font = ImageFont.truetype('arial.ttf', size=square_size//6)
        element_font = ImageFont.truetype('arial.ttf', size=square_size//7)
        mass_font = ImageFont.truetype('arial.ttf', size=square_size//9)

        x1,y1 = font.getsize(caractere)
        x2,y2 = element_font.getsize(element)
        x3,y3 = z_font.getsize(z)
        x4,y4 = mass_font.getsize(mass)

        draw = ImageDraw.Draw(self.background)
        draw.text( ((2*bg_width+square_size-x1)//2,(2*bg_heigth+square_size-y1)//2), caractere, font=font,fill="white") #stroke_width=5, stroke_fill=(0,150,80)
        draw.text( ((2*bg_width+square_size-x2)//2,bg_heigth+0.5*y2) , element, font=element_font, fill="white" )
        draw.text( (bg_width+0.5*y3,bg_heigth+square_size-1.5*y3) , z, font=z_font, fill="white" )
        draw.text( (bg_width+square_size-x4-0.5*y3,bg_heigth+square_size-y4-0.5*y3) , mass, font=mass_font, fill="white" )

    def composeSquares(self, new_name):
        bg_width, bg_heigth = self.background.size
        square_size = 10*(self.findSquareSize(new_name, bg_width, bg_heigth))//11    
        #C:/Windows/Fonts/Arial/arialbd.ttf
        font1 = ImageFont.truetype("C:/Windows/Fonts/Arial/arialbd.ttf", size=(square_size//2))
        font2 = ImageFont.truetype("website/static/Heart Breaking Bad.otf", size=(square_size))
        wordsNum = len(new_name)
        
        k = 0
        for j in range(wordsNum):
            i = 0
            symbol_found = False
            for c in new_name[j]:
                if c == self.symbols[j] and symbol_found == False:
                    symbol_found = True
                    element = prd.elements.symbol(c).name
                    z = int(prd.elements.symbol(c).number)
                    mass = str(prd.elements.symbol(c).mass)
                    self.addSquare((bg_width-len(new_name[j])*square_size)//2 + i , k+(j+1)*(bg_heigth-square_size*wordsNum)//(wordsNum+1), square_size)
                    self.addText(c, element ,str(z), mass,
                        (bg_width-len(new_name[j])*square_size)//2 + i , k+(j+1)*(bg_heigth-square_size*wordsNum)//(wordsNum+1), square_size, font1)
                    
                else:
                    self.addText(c.lower(), '', '', '', 
                        (bg_width-len(new_name[j])*square_size)//2 + i ,k+(j+1)*(bg_heigth-square_size*wordsNum)//(wordsNum+1), square_size, font2)
                i += square_size
            k += square_size
        
        signature = "Ahmed&Ahmed"
        font3 = ImageFont.truetype("arial.ttf", size = bg_heigth//40)   
        sgnt_width, sgnt_heigth = font3.getsize(signature)
        draw = ImageDraw.Draw(self.background)
        draw.text((bg_width-sgnt_width-10,bg_heigth-sgnt_heigth-10), signature, fill="white", font=font3)

    def createImage(self):
        self.findSymbols()
        new_name = self.rewriteName()
        with Image.open(self.background) as img:
            self.background = img.filter(ImageFilter.BoxBlur(4))
            self.composeSquares(new_name)
            self.background.save("website/static/img/result.jpg")
        self.background.close()