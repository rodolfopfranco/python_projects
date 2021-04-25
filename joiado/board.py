from jewel import Jewel

class Board:

    def __init__(self):
        """starts the matrix (8x8) and populates with jewels"""
        self.matrix = [[],[],[],[],[],[],[],[]]
        self.jewelsPopulate()
        self.temp_score = 0
        self.score = 0

    def __str__(self):
        matrix_string='  0  1  2  3  4  5  6  7  \n'
        for i in range(8):
            matrix_string+=str(i)+"|"
            for j in range(8):
                matrix_string+=str(self.matrix[i][j].getColor())+" |"
            matrix_string+=" \n"
        return matrix_string

    def addScore(self,temp_score):
        self.score += temp_score

    def getScore(self):
        return self.score

    def jewelsPopulate(self):
        """inserts jewels on the board"""
        for i in range(8):
            for j in range(8):
                temp=Jewel()
                while self.jewelCascadeAvoid(i,j,temp):
                    temp=Jewel()
                self.matrix[i].append(temp)

    def jewelCascadeAvoid(self,coordinatex,coordinatey,jewel):
        """checks if there's the same jewel in 2 rows before and above before placing it, to avoid cascade. returns true if there is"""
        if coordinatex > 1:
            if self.matrix[coordinatex-1][coordinatey].getColor() == jewel.getColor() and self.matrix[coordinatex-2][coordinatey].getColor() == jewel.getColor():
                return True
        if coordinatey > 1:
            if self.matrix[coordinatex][coordinatey - 1].getColor() == jewel.getColor() and self.matrix[coordinatex][coordinatey - 2].getColor() == jewel.getColor():
                return True
        return False

    def jewelRemove(self,h_match_start1, h_jewel_count1, v_match_start1, v_jewel_count1, h_match_start2, h_jewel_count2, v_match_start2, v_jewel_count2):
        #removes the matched jewels
        if (h_match_start1[0] != 666):
            for i in range (0,h_jewel_count1):
                self.matrix[h_match_start1[0]][h_match_start1[1]+ i].setColor(0)
        if (v_match_start1[0] != 666):
            for i in range (0,v_jewel_count1):
                self.matrix[v_match_start1[0] + i][v_match_start1[1]].setColor(0)
        if (h_match_start2[0] != 666):
            for i in range (0,h_jewel_count2):
                self.matrix[h_match_start2[0]][h_match_start2[1] + i].setColor(0)
        if (v_match_start2[0] != 666):
            for i in range (0,v_jewel_count2):
                self.matrix[v_match_start2[0] + i][v_match_start2[1]].setColor(0)
        if (h_match_start1[0] == 666) and (v_match_start1[0] == 666) and (h_match_start2[0] == 666) and (v_match_start2[0] == 666):
            return False
        else:
            return True

    def jewelMatchCheck(self,j1x,j1y,j2x,j2y):
        """checks if you got 3 matching jewels"""
        h_match_start1, h_jewel_count1 = self.matchHorizontal(j1x,j1y)
        v_match_start1, v_jewel_count1 = self.matchVertical(j1x, j1y)
        h_match_start2, h_jewel_count2 = self.matchHorizontal(j2x, j2y)
        v_match_start2, v_jewel_count2 = self.matchVertical(j2x,j2y)
        if (self.jewelRemove(h_match_start1, h_jewel_count1, v_match_start1, v_jewel_count1, h_match_start2, h_jewel_count2, v_match_start2, v_jewel_count2)):
            self.temp_score = v_jewel_count1 + v_jewel_count2 + h_jewel_count1 + h_jewel_count2
            return True
        else:
            self.jewelSwap(self.matrix[j1x][j1y],j1x,j1y,self.matrix[j2x][j2y],j2x,j2y)
            return False

    def jewelCascade(self):
        #Checks boardfor 0s and if finds one, swaps it 'till the top of the column
        for i in range(8):
            for j in range(8):
                if (int(self.matrix[i][j].getColor()) == 0):
                    self.jewelUp(i,j)
        for i in range(8):
            for j in range(8):
                if (int(self.matrix[i][j].getColor()) == 0):
                    self.matrix[i][j] = Jewel()

    def jewelUp(self,x,y):
        #rises the jewel to the top of column. V stands for if the match is vertcal or not
        i = x
        while i != 0:
            self.jewelSwap(self.matrix[i][y],i,y,self.matrix[i-1][y],i-1,y)
            i -= 1

    def matchVertical(self,x,y):
        # searches horizontal match
        jewel_found = 666
        jewel_count = 0
        vertical_match_start = [666,666]
        for i in range(-2,3):
            if (x + i > 7) or (x + i < 0):
                continue
            if (int(self.matrix[x + (i)][y].color)) == (jewel_found):
                jewel_count += 1
            elif (jewel_count < 3):
                jewel_found = self.matrix[x + (i)][y].color
                jewel_count = 1
                vertical_match_start = [x + (i), y]
            else:
                continue
        if (jewel_count < 3):
            vertical_match_start = [666, 666]
            jewel_found = 666
            jewel_count = 0
        return vertical_match_start, jewel_count

    def matchHorizontal(self,x,y):
        # searches vertical match, returns coordinate from start and jewel count
        jewel_found = 666
        jewel_count = 0
        for i in range(-2, 3):
            if (y + i > 7) or (y + i < 0):
                continue
            if (int(self.matrix[x][y + (i)].color)) == (jewel_found):
                jewel_count += 1
            elif (jewel_count < 3):
                jewel_found = self.matrix[x][y + (i)].color
                jewel_count = 1
                horizontal_match_start = [x, y + (i)]
            else:
                continue
        if (jewel_count < 3):
            horizontal_match_start = [666, 666]
            jewel_found = 666
            jewel_count = 0
        return horizontal_match_start, jewel_count

    def boardUpdate(self,joia1Coord,joia1Color,joia2Coord,joia2Color):
        temp = joia1Color
        self.matrix[joia1Coord[0]][joia1Coord[1]] = joia2Color
        self.matrix[joia2Coord[0]][joia2Coord[1]] = temp

    def jewelSwap(self,joia1,joia1CoordX,joia1CoordY,joia2,joia2CoordX,joia2CoordY):
        #Swaps Jewel1 with Jewel 2 in the board.
        joia1C=[joia1CoordX,joia1CoordY]
        joia2C= [joia2CoordX, joia2CoordY]
        self.boardUpdate(joia1C,joia1,joia2C,joia2)