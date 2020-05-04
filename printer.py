'''
    this is 出力 Command module
'''

class Printer(object):
    result=""
    firststr=""
    strcount=0
    variablestr=""

    def __init__(self,field1,variabledicts):
        self.field1 = field1
        self.variabledicts = variabledicts

    def printstr(self):
        for g in range(len(self.field1)-1):
            self.firststr=self.firststr+self.field1[g]
            self.strcount+=1
            #変数なし
            if self.field1[g+1]=="終" and (self.field1[g]=='"' or self.field1[g]=='”'):
                #
                self.firststr=self.firststr.replace('"','')
                self.firststr=self.firststr.replace('”','')
                self.result=self.firststr
                #今回の命令を全て消去して次に渡す
                self.field1=self.field1[self.strcount+1:]
                break
            #変数あり
            elif self.field1[g+1]=="終" :
                if self.firststr in self.variabledicts:
                    self.variablestr=self.variabledicts[self.firststr]
                else:
                    self.result="error"
                if self.variablestr :
                    self.firststr=str(self.variablestr)
                    self.result=self.firststr
                    #今回の命令を全て消去して次に渡す
                    self.field1=self.field1[self.strcount+1:]
                    break
        if self.strcount==len(self.field1):
                self.result=="error"


        #print(self.result)
        return self.field1

    def returnresult(self):
        return self.result
