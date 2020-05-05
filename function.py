'''
    this is 関数 Command module
'''


class Func(object):
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
    funcname=""
    funcmain=""

    def __init__(self,field1,variabledicts):
        self.field1 = field1
        self.variabledicts = variabledicts


    def function(self):
        #関数名の読み取り
        for i in range(len(self.field1)-1):
            self.funcname=self.funcname+self.field1[i]
            self.strcount+=1
            if self.field1[i+1]==";" or self.field1[i+1]=="；" :
                self.field1=self.field1[self.strcount:]
                #return self.field1
                break

        if self.strcount==len(self.field1):
                self.funcname="error"


        #｝の前までの処理読み取り
        for g in range(len(self.field1)-1):
            self.strcount3+=1
            self.funcmain=self.funcmain+self.field1[g]
            if self.field1[g+1]=="}" or self.field1[g+1]=="｝":
                self.field1=self.field1[self.strcount3+1:]
                break

        if self.strcount3==len(self.field1):
             self.funcmain="error"

        return self.field1

    def returnfuncname(self):
        return self.funcname

    def returnfuncmain(self):
        return self.funcmain
