'''
    this is 条件繰り返し Command module
'''


class Conrep(object):
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


    def __init__(self,field1,variabledicts,firstcondition,secondcondition,operation):
        self.field1 = field1
        self.fieldfirst = field1
        self.variabledicts = variabledicts
        self.firstcondition = firstcondition
        self.secondcondition = secondcondition
        self.operation = operation

    def conditionrepete(self):

        if self.firstcondition in self.variabledicts:
            self.variablenumber=self.variabledicts[self.firstcondition]
            self.variablenumber=str(self.variablenumber)
        if self.variablenumber :
            self.firstcondition=str(self.variablenumber)

        if self.secondcondition in self.variabledicts:
            self.variablenumber2=self.variabledicts[self.secondcondition]
            self.variablenumber2=str(self.variablenumber2)
        if self.variablenumber2 :
            self.secondcondition=str(self.variablenumber2)



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


        return self.result


    def returnresult(self):
        return self.result

    def conditionrepete2(self):
        return self.field2

    def returnfirstfield(self):
        return self.fieldfirst
