'''
The programming lamguage "HarukaZe"

Main source module(script.py)

since 2020/05/02

'''
#ライブラリの読み込み
import sys
from sys import argv
from flask import Flask , render_template , request
#命令モジュールの読み込み
from calculate import *
from printer import *
from varmker import *
from repete import *
from branch import *
from conditionrepete import *
from function import *

'''
実行関数
'''

'''
flask用
'''
app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


#コードの受け取り
#code=input("入力してくっださい：")
#code=request.form['field1']
#f = open(sys.argv[1])
#field1 = f.read()
#f.close()


@app.route('/', methods=['POST'])


def returnfield1():
    code=request.form['field1']
    #受け取ったコードの改行を消去
    code=code.replace("\n","")
    code=code.replace("\r","")
    #変数を保存してある辞書を渡す
    variabledicts1={}
    funcdicts1={}

    #関数の実行をしてリストで受け取る
    resultlist=HarukaZe(code,variabledicts1,funcdicts1)
    result1=""
    for i in range(len(resultlist)):
        n=i+1
        result1=result1+"  "+str(resultlist[i])
    return render_template('index.html', result=result1)


def HarukaZe(field,variabledicts,funcdicts):
    com = ""
    Command = ['計算','出力',] #必要ない
    g = 0 #必要ない
    field1 = ""
    count = 0
    strcount2 = 1

    variabledicts = variabledicts
    funcdicts = funcdicts

    printlist  = []

    field1=field

    #コードの空白消去
    field1=field1.replace(" ","")
    field1=field1.replace("　","")


    #繰り返し命令実行


    while len(field1)>0 :

        #print(variabledicts)
        #print(printlist)
        #print(funcdicts)


        strcount2 = 1
        com = ""
        #命令部分の読み取り
        for n in range(len(field1)-1):
            com=com+field1[n]
            strcount2+=1
            if field1[n+1]==":" or field1[n+1]=="：":
                #comp = com+":"
                field1=field1[strcount2:]
                break
            else:
                count+=1

        #print(com)   #実行チェック
        #print(field1)   #実行チェック


        #命令の実行

        '''
        if count==len(field1):
            result="error"
            break
        '''

        if com == "計算":
            cal = Calculate(field1,variabledicts)
            field1=cal.form()
            #flask用関数returnresult()
            result=cal.returnresult()
            printlist.append(result)
            #print(result)
            #return render_template('index.html', title=result1)

            #print(field1)
            #print(result1)
        elif com == "出力":
            pri = Printer(field1,variabledicts)
            field1=pri.printstr()
            result=pri.returnresult()
            printlist.append(result)

        elif com == "数値変数":
            var = Variable(field1)
            field1=var.varmker()
            variable1 = var.varlistcall()
            variable2 = var.varnumbercall()
            #変数のなかに計算処理がある場合
            varfunc1 = var.varfunccall()
            varfunc1 = varfunc1[3:]
            #print(varfunc1)
            #計算コマンド限定の処理
            if varfunc1:
                cal2 = Calculate(varfunc1,variabledicts)
                varfunc1=cal2.form()
                result=cal2.returnresult()
                variable2=result
            #作った変数をnumbersicts辞書に保存
            numberdict = {variable1 : variable2}
            variabledicts.update(numberdict)
            #print(numberdicts)
            #print(variabledicts["number"])
            #print(field1)
        elif com == "文字変数":
            var = Variablestr(field1)
            field1=var.varmker2()
            #作った変数をnumbersicts辞書に保存
            variable1 = var.varlistcall2()
            variable2 = var.varnumbercall2()
            stringdict = {variable1 : variable2}
            variabledicts.update(stringdict)
            #print(variabledicts)
            #print(variabledicts["string"])

        elif com == "繰り返し":
            rep = Repetition(field1,variabledicts,funcdicts)
            field1=rep.repete()
            times = rep.repetetimes()
            field2 = rep.repete2()
            for i in range(times):
                print(field2)
                result3=HarukaZe(field2,variabledicts,funcdicts)
                for g in range(len(result3)):
                    printlist.append(result3[g])
        elif com == "分岐":
            ifbra = Ifbra(field1,variabledicts)
            field1 = ifbra.branch()
            result = ifbra.returnresult()
            field2 = ifbra.branch2()
            if result=="true":
                HarukaZe(field2)

        elif com == "条件繰り返し":



            '''
            conrep = Conrep(field1,variabledicts)
            field1 = conrep.conditionrepete()
            result = conrep.returnresult()
            #conrep = Ifbra(field1,variabledicts)
            #field1 = conrep.branch()
            #result = conrep.returnresult()
            #field2 = conrep.branch2()
            #fieldfirst = conrep.returnfirstfield()
            #field2 = feild2 + "}"
            '''

            conrep = Ifbra(field1,variabledicts)
            field1 = conrep.branch()
            result = conrep.returnresult()
            field2 = conrep.branch2()
            firstconrep = conrep.returnfirstconrep()
            operation = conrep.returnoperation()
            secondconrep = conrep.returnsecondconrep()
            #確認用
            #print(firstconrep)
            #print(operation)
            #print(secondconrep)
            #print(field1)
            #print(field2)
            #print(result)
            #count=0
            while result=="true":
                variabledicts2=variabledicts
                #print(variabledicts2)
                result3=HarukaZe(field2,variabledicts,funcdicts)
                #print(variabledicts)
                for g in range(len(result3)):
                    printlist.append(result3[g])
                conrep = Conrep(field1,variabledicts,firstconrep,secondconrep,operation)
                result = conrep.conditionrepete()
                #print(result)
                #print(variabledicts["number"])
                #count+=1
                #if count==3:
                    #break

        elif com == "関数定義":
            func = Func(field1,variabledicts)
            field1 = func.function()
            funcname = func.returnfuncname()
            funcmain = func.returnfuncmain()
            funcdict = {funcname:funcmain}
            funcdicts.update(funcdict)
            #print(funcdicts)

        elif com in funcdicts:
            field3=funcdicts[com]
            if field3:
                result3=HarukaZe(field3,variabledicts,funcdicts)
                #print(result3)
                for g in range(len(result3)):
                    printlist.append(result3[g])






        #上の条件がelifになっているか確認
        else:
            result="error"
            break

        #count +=1
        #print(count)
    return printlist

#HarukaZe(code)



if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
