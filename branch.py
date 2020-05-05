'''
    this is 分岐 Command module
'''


class Ifbra(object):
    firstcondition = ""
    secondcondition = ""
    result=""
    strcount = 1
    strcount3 = 0
    strcount5 = 0
    variablenumber = 0
    variablenumber2 = 0
    operation=""
    field2=""
    firstconrep=""
    secondconrep=""


    def __init__(self,field1,variabledicts):
        self.field1 = field1
        self.fieldfirst = field1
        self.variabledicts = variabledicts

    def branch(self):
        #条件の読み込み
        for i in range(len(self.field1)-2):
            self.firstcondition=self.firstcondition+self.field1[i]
            self.strcount+=1
            if self.field1[i+1]=="=" and self.field1[i+2]=="=" :
                self.operation=self.field1[i+1]+self.field1[i+2]
                self.field1=self.field1[self.strcount+1:]
                #変数の場合の計算処理
                self.firstconrep=self.firstcondition #条件繰り返しのための変数
                if self.firstcondition in self.variabledicts:
                    self.variablenumber=self.variabledicts[self.firstcondition]
                    self.variablenumber=str(self.variablenumber)
                if self.variablenumber :
                    self.firstcondition=str(self.variablenumber)
                break
            elif self.field1[i+1]==">" and self.field1[i+2]=="=" :
                self.operation=self.field1[i+1]+self.field1[i+2]
                self.field1=self.field1[self.strcount+1:]
                #変数の場合の計算処理
                if self.firstcondition in self.variabledicts:
                    self.variablenumber=self.variabledicts[self.firstcondition]
                    self.variablenumber=str(self.variablenumber)
                if self.variablenumber :
                    self.firstcondition=str(self.variablenumber)
                break
            elif self.field1[i+1]=="<" and self.field1[i+2]=="=" :
                self.operation=self.field1[i+1]+self.field1[i+2]
                self.field1=self.field1[self.strcount+1:]
                #変数の場合の計算処理
                self.firstconrep=self.firstcondition #条件繰り返しのための変数
                if self.firstcondition in self.variabledicts:
                    self.variablenumber=self.variabledicts[self.firstcondition]
                    self.variablenumber=str(self.variablenumber)
                if self.variablenumber :
                    self.firstcondition=str(self.variablenumber)
                break
            elif self.field1[i+1]=="!" and self.field1[i+2]=="=" :
                self.operation=self.field1[i+1]+self.field1[i+2]
                self.field1=self.field1[self.strcount+1:]
                #変数の場合の計算処理
                self.firstconrep=self.firstcondition #条件繰り返しのための変数
                if self.firstcondition in self.variabledicts:
                    self.variablenumber=self.variabledicts[self.firstcondition]
                    self.variablenumber=str(self.variablenumber)
                if self.variablenumber :
                    self.firstcondition=str(self.variablenumber)
                break
            elif self.field1[i+1]=="<" and self.field1[i+2]!="=" :
                self.operation=self.field1[i+1]
                self.field1=self.field1[self.strcount:]
                #変数の場合の計算処理
                self.firstconrep=self.firstcondition #条件繰り返しのための変数
                if self.firstcondition in self.variabledicts:
                    self.variablenumber=self.variabledicts[self.firstcondition]
                    self.variablenumber=str(self.variablenumber)
                if self.variablenumber :
                    self.firstcondition=str(self.variablenumber)
                break
            elif self.field1[i+1]==">" and self.field1[i+2]!="=" :
                self.operation=self.field1[i+1]
                self.field1=self.field1[self.strcount:]
                #変数の場合の計算処理
                self.firstconrep=self.firstcondition #条件繰り返しのための変数
                if self.firstcondition in self.variabledicts:
                    self.variablenumber=self.variabledicts[self.firstcondition]
                    self.variablenumber=str(self.variablenumber)
                if self.variablenumber :
                    self.firstcondition=str(self.variablenumber)
                break

        if self.strcount==len(self.field1):
            self.result="error"


        #処理の読み取り
        for g in range(len(self.field1)-1):
            self.secondcondition=self.secondcondition+self.field1[g]
            self.strcount3+=1
            if self.field1[g+1]==";" or self.field1[g+1]=="；":
                self.field1=self.field1[self.strcount3+1:]
                #変数の場合の計算処理
                self.secondconrep=self.secondcondition #条件繰り返しのための変数
                if self.secondcondition in self.variabledicts:
                    self.variablenumber2=self.variabledicts[self.secondcondition]
                    self.variablenumber2=str(self.variablenumber2)
                if self.variablenumber2 :
                    self.secondcondition=str(self.variablenumber2)

                break

        if self.strcount3==len(self.field1):
                self.result="error"


        for h in range(len(self.field1)-2):
            self.strcount5+=1
            self.field2=self.field2+self.field1[h]
            if self.field1[h+1]=="}" and self.field1[h+2]=="}":
                self.field2=self.field2+self.field1[h+2]
                self.field1=self.field1[self.strcount5+2:]
                break
            #elif self.field1[h+1]=="}" or self.field1[h+1]=="｝":
            elif self.field1[h+1]=="}" and self.field1[h+2]!="}":
                self.field1=self.field1[self.strcount5+1:]
                break

        if self.strcount5==len(self.field1):
             self.result=="error"

        #条件の正当性の確認
        if self.operation=="==" and self.result!="error" and self.firstcondition==self.secondcondition:
            self.result="true"
        elif self.operation==">=" and self.result!="error" and int(self.firstcondition)>=int(self.secondcondition):
            self.result="true"
        elif self.operation=="<=" and self.result!="error" and int(self.firstcondition)<=int(self.secondcondition):
            self.result="true"
        elif self.operation=="!=" and self.result!="error" and self.firstcondition!=self.secondcondition:
            self.result="true"
        elif self.operation==">" and self.result!="error" and int(self.firstcondition)>int(self.secondcondition):
            self.result="true"
        elif self.operation=="<" and self.result!="error" and int(self.firstcondition)<int(self.secondcondition):
            self.result="true"
        else :
            self.result="error"


        return self.field1


    def returnresult(self):
        return self.result

    def branch2(self):
        return self.field2

    def returnfirstfield(self):
        return self.fieldfirst

    def returnfirstconrep(self):
        return self.firstconrep
    def returnsecondconrep(self):
        return self.secondconrep
    def returnoperation(self):
        return self.operation
