'''
    this is 繰り返し Command module
'''


class Repetition(object):
    firsttimes = ""
    secondnumber = ""
    result=0
    strcount = 1
    strcount3 = 0
    variablenumber = 0
    variablenumber2 = 0
    field2=""


    def __init__(self,field1,variabledicts):
        self.field1 = field1
        self.variabledicts = variabledicts

    def repete(self):
        #回数の文字の読み取り
        for i in range(len(self.field1)-2):
            self.firsttimes=self.firsttimes+self.field1[i]
            self.strcount+=1
            if self.field1[i+1]==";" or self.field1[i+1]=="；" :

                #変数の場合の計算処理
                if self.firsttimes in self.variabledicts:
                    self.variablenumber=self.variabledicts[self.firsttimes]
                if self.variablenumber :
                    self.firsttimes=int(self.variablenumber)

                self.field1=self.field1[self.strcount:]
                self.result = int(self.firsttimes)
                #return self.field1
                break

        if self.strcount==len(self.field1):
                self.result="error"

        #｝の前までの処理読み取り
        for g in range(len(self.field1)-1):
            self.strcount3+=1
            self.field2=self.field2+self.field1[g]
            if self.field1[g+1]=="}" or self.field1[g+1]=="｝":
                self.field1=self.field1[self.strcount3+1:]
                break

        if self.strcount3==len(self.field1):
             self.result="error"

        return self.field1

    def repete2(self):
        return self.field2


    def repetetimes(self):
        return self.result
