'''
    this is 数値変数 文字変数 Command module
'''

class Variable(object):

    var1 = ""
    strcount = 1
    strcount3 = 0
    number = ""
    varlist= ""
    result = ""
    varnumber = 0
    func=""
    varfunc=""

    def __init__(self,field1):
        self.field1 = field1


    def varmker(self):

        #
        for i in range(len(self.field1)-1):
            self.var1=self.var1+self.field1[i]
            self.strcount+=1
            if self.field1[i+1]=="=" :
                self.varlist=self.var1
                self.field1=self.field1[self.strcount:]
                break
        if self.strcount == len(self.field1):
            self.varlist = "error"

        if self.field1[0]=="{":
            for n in range(1,len(self.field1)):
                self.strcount3+=1
                self.func=self.func+self.field1[n]
                if self.field1[n+1]=="}" and self.varlist!="error":
                    self.varfunc=self.func
                    self.field1=self.field1[self.strcount3+2:]
                    break


        #
        else:
            for g in range(len(self.field1)):
                self.number=self.number+self.field1[g]
                self.strcount3+=1
                if self.field1[g+1]=="終" and self.varlist!="error":
                    self.varnumber = int(self.number)
                    self.var1 = int(self.number)
                    #if "+" in self.varnumber :

                    #id(self.var1) = id(self.field1)
                    self.field1=self.field1[self.strcount3+1:]
                    break

            if self.strcount == len(self.field1):
                self.varnumber = "error"


        return self.field1




    def varlistcall(self):
        return self.varlist

    def varnumbercall(self):
        return self.varnumber

    def varfunccall(self):
        return self.varfunc



class Variablestr(object):

    var2 = ""
    strcount2 = 1
    strcount4 = 0
    string = ""
    varlist2= ""
    result2 = ""
    varstring = 0

    def __init__(self,field1):
        self.field2 = field1


    def varmker2(self):
        #
        for i in range(len(self.field2)-1):
            self.var2=self.var2+self.field2[i]
            self.strcount2+=1
            if self.field2[i+1]=="=" :
                self.varlist2=self.var2
                self.field2=self.field2[self.strcount2:]
                break
        if self.strcount2 == len(self.field2):
            self.varlist2 = "error"

        #
        for g in range(len(self.field2)):
            self.string=self.string+self.field2[g]
            self.strcount4+=1
            if self.field2[g+1]=="終" and self.varlist2!="error":
                self.varstring = self.string
                self.var2 = self.string
                #id(self.var1) = id(self.field1)
                self.field2=self.field2[self.strcount4+1:]
                break

        if self.strcount2 == len(self.field2):
            self.varstring = "error"


        return self.field2




    def varlistcall2(self):
        return self.varlist2

    def varnumbercall2(self):
        return self.varstring
