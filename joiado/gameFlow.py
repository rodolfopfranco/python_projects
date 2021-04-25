class GameFlow():

    def getLvl1(self):
        return 50

    def selectJewel(self,board):
        joia1Coord = input("informe a coordenada da joia a mover (x y)").split()
        joia1Color = board.matrix[int(joia1Coord[0])][int(joia1Coord[1])]
        joia2Coord = input("informe a coordenada da joia com a qual trocará de lugar (x y)").split()
        joia2Color = board.matrix[int(joia2Coord[0])][int(joia2Coord[1])]
        if self.checkJewelMovement(int(joia1Coord[0]),int(joia1Coord[1]),int(joia2Coord[0]),int(joia2Coord[1])):
            board.jewelSwap(joia1Color,int(joia1Coord[0]),int(joia1Coord[1]),joia2Color,int(joia2Coord[0]),int(joia2Coord[1]))
            combo_count = 0
            temp_score = 0
            while (board.jewelMatchCheck(int(joia1Coord[0]),int(joia1Coord[1]),int(joia2Coord[0]),int(joia2Coord[1]))):
                combo_count += 1
                temp_score += board.temp_score
                board.jewelCascade()
                #print(board) Used if wanting to see results beetween combos
                print("combo!",combo_count)
                print("temp_score:",temp_score)
            else:
                board.addScore(temp_score*combo_count)
                print("score:",board.getScore())
        return board

    def checkJewelMovement(self,joia1CoordX,joia1CoordY,joia2CoordX,joia2CoordY):
        # Checks if the other jewel selected is next to the main one
        if (joia1CoordX + 1 == joia2CoordX) or (joia1CoordX - 1 == joia2CoordX) or (joia1CoordX == joia2CoordX):
            if (joia1CoordY + 1 == joia2CoordY) or (joia1CoordY - 1 == joia2CoordY) or (joia1CoordY == joia2CoordY):
                return True
        else:
            return False