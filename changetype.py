'''
    this is 型変換 Command module
'''


class Changetype(object):
    firsttimes = ""
    secondnumber = ""
    result=0
    strcount = 1
    strcount3 = 0
    variablenumber = 0
    variablenumber2 = 0
    field2=""
    function=""
    variablename=""


    def __init__(self,field1,variabledicts,funcdicts):
        self.field1 = field1
        self.variabledicts = variabledicts
        self.funcdicts = funcdicts

    def changetype(self):
        #回数の文字の読み取り
        for i in range(len(self.field1)-2):
            self.firsttimes=self.firsttimes+self.field1[i]
            self.strcount+=1
            if self.field1[i+1]==";" or self.field1[i+1]=="；" :

                #変数の場合の計算処理
                if self.firsttimes in self.variabledicts:
                    self.variablename=self.firsttimes
                    self.variablenumber=self.variabledicts[self.firsttimes]
                if self.variablenumber :
                    self.firsttimes=self.variablenumber


                self.field1=self.field1[self.strcount:]
                self.result = self.firsttimes
                #return self.field1
                break

        if self.strcount==len(self.field1):
                self.result="error"
        #｝の前までの処理読み取り
        for g in range(len(self.field1)-1):
            self.strcount3+=1
            self.field2=self.field2+self.field1[g]

            if self.field1[g+1]=="}" or self.field1[g+1]=="｝":

                #関数の場合の計算処理
                if self.field2 in self.funcdicts:
                    self.function=self.funcdicts[self.field2]
                if self.function :
                    self.field2=self.function

                self.field1=self.field1[self.strcount3+1:]
                break

        if self.strcount3==len(self.field1):
             self.result="error"

        return self.field1

    def changetype2(self):
        return self.field2

    def returnvariablename(self):
        return self.variablename

    def repetetimes(self):
        return self.result
