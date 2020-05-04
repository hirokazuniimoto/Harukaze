'''
    this is 計算 Command module

'''
class Calculate(object):

    firstnumber = ""
    operation = "a"
    secondnumber = ""
    result=""
    strcount = 1
    strcount3 = 0
    variablenumber = 0
    variablenumber2 = 0
    sub=""

    def __init__(self,field1,variabledicts):
        self.field1 = field1
        self.variabledicts = variabledicts

    def calculate(self,firstnumber1,operation1,secondnumber1):
        if operation1=="+":
            self.result=int(firstnumber1)+int(secondnumber1)
        elif operation1=="-":
            self.result=int(firstnumber1)-int(secondnumber1)
        elif operation1=="*":
            self.result=int(firstnumber1)*int(secondnumber1)
        elif operation1=="/":
            self.result=int(firstnumber1)//int(secondnumber1)
        else:
            self.result="error"
        return self.result

    def form(self):
        #演算子までの文字の読み取り
        for i in range(len(self.field1)-1):
            self.firstnumber=self.firstnumber+self.field1[i]
            self.strcount+=1
            if self.field1[i+1]=="+" or self.field1[i+1]=="-" or self.field1[i+1]=="*" or self.field1[i+1]=="//" :
                self.operation=self.field1[i+1]

                #変数の場合の計算処理

                if self.firstnumber in self.variabledicts:
                    self.variablenumber=self.variabledicts[self.firstnumber]
                    self.variablenumber=str(self.variablenumber)
                if self.variablenumber :
                    self.firstnumber=str(self.variablenumber)

                self.firstoper = self.firstnumber+self.operation
                self.field1=self.field1[self.strcount:]
                break

        

        if self.strcount==len(self.firstnumber)+len(self.operation)+len(self.field1):
            self.result=self.field1[:1]
            self.sub="rrr"


        #最後までの文字の読み取り
        for g in range(len(self.field1)-1):
            self.secondnumber=self.secondnumber+self.field1[g]
            self.strcount3+=1
            if self.field1[g+1]=="終" and self.sub!="rrr":

                #変数の場合の計算処理
                if self.secondnumber in self.variabledicts:
                    self.variablenumber2=self.variabledicts[self.secondnumber]
                    self.variablenumber2=str(self.variablenumber2)
                if self.variablenumber2 :
                    self.secondnumber=str(self.variablenumber2)


                #calculate関数の実行
                self.calculate(self.firstnumber,self.operation,self.secondnumber)
                #今回の命令を全て消去して次に渡す
                self.field1=self.field1[self.strcount3+1:]
                break


        if self.strcount3+1==len(self.field1) :
                #self.result=="error"
                self.field1=self.field1[self.strcount3+1:]


        return self.field1


    def returnresult(self):
        return self.result
