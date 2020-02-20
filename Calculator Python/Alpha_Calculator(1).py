
from tkinter import *
pi=3.1415
926535897932384650288
from tangent import sin
from tangent import cos
from tangent import tan
from all_functions import sqr
from all_functions import cube
from all_functions import power
from all_functions import sqrroot
from all_functions import cuberoot
from all_functions import root
from all_functions import percent
from all_functions import invr
from all_functions import exp
from all_functions import mod
from log_antilog import log
from log_antilog import antilog
from log_antilog import ln
from hyperbolic import sinh
from hyperbolic import cosh
from hyperbolic import tanh
from permutation import nCr
from permutation import nPr
from permutation import factorial
from quadratic_eq import quad
from inverse import com
from inverse import arcsin
from inverse import arccos
from inverse import arctan
from binary4 import oct_dec
from binary4 import bin_dec
from binary4 import hex_dec
from binary4 import dec_bin
from binary4 import dec_oct
from binary4 import dec_hex
from e_power import exp_e
from e_power import summation
from conversion1 import conv1
from conversion1 import conv2
from conversion1 import conv3
from conversion1 import conv4
from conversion1 import conv5
from conversion1 import conv6
from conversion1 import conv7
from conversion1 import conv8
from conversion1 import conv9
from conversion1 import conv10
from conversion1 import conv11
from conversion1 import conv12
from conversion1 import conv13
from conversion1 import conv14
from conversion1 import conv15
from conversion1 import conv16
from conversion1 import conv17
from conversion1 import conv18
from conversion1 import conv19
from conversion1 import conv20


def type1(number):
    global var
    var=var+str(number)
    txt.set(var)
def cls():
    global var
    var=""
    txt.set("")
def Equal():
    global var
    calculation=str(eval(var))
    txt.set(calculation)
    var=""

            

cal=Tk()
cal.title("Alpha Calculator")
var=""
txt=StringVar()
Screen=Entry(cal,font=("arial",40,"bold"),textvariable=txt,insertwidth=6,bd=20,bg="black",fg="white"
             ).grid(columnspan="30")
b1=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="7",command=lambda:type1(7)).grid(row=1,column=0)
b2=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="8",command=lambda:type1(8)).grid(row=1,column=1)
b3=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="9",command=lambda:type1(9)).grid(row=1,column=2)
b4=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="4",command=lambda:type1(4)).grid(row=2,column=0)
b5=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="5",command=lambda:type1(5)).grid(row=2,column=1)
b6=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="6",command=lambda:type1(6)).grid(row=2,column=2)
b7=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="1",command=lambda:type1(1)).grid(row=3,column=0)
b8=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="2",command=lambda:type1(2)).grid(row=3,column=1)
b9=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="3",command=lambda:type1(3)).grid(row=3,column=2)
b0=Button(cal,width=5,height=1,fg="white",bg="gray",font=("arial",20,"bold"),text="0",command=lambda:type1(0)).grid(row=4,column=1)
bpoint=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text=".",command=lambda:type1(".")).grid(row=4,column=2)
bsub=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="-",command=lambda:type1("-")).grid(row=1,column=3)
badd=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="+",command=lambda:type1("+")).grid(row=2,column=3)
bmul=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="x",command=lambda:type1("*")).grid(row=3,column=3)
bdiv=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="/",command=lambda:type1("/")).grid(row=3,column=4)
bclr=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="Clr",command=lambda:cls()).grid(row=1,column=4)
bequal=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="=",command=lambda:Equal()).grid(row=10,column=4)
bsin=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="sinθ",command=lambda:type1("sin(")).grid(row=8,column=0)
bcos=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="cosθ",command=lambda:type1("cos(")).grid(row=8,column=1)
btan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="tanθ",command=lambda:type1("tan(")).grid(row=8,column=2)
bsin=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="x^y",command=lambda:type1("power(")).grid(row=11,column=3)
bsin=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="√",command=lambda:type1("sqrroot(")).grid(row=6,column=0)
bsin=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="∛",command=lambda:type1("cuberoot(")).grid(row=6,column=1)
bbopen=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="(",command=lambda:type1("(")).grid(row=5,column=1)
bbclose=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text=")",command=lambda:type1(")")).grid(row=5,column=2)
bfac=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="!",command=lambda:type1("factorial(")).grid(row=10,column=3)
bsqr=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="x^2",command=lambda:type1("sqr(")).grid(row=11,column=1)
bcube=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="x^3",command=lambda:type1("cube(")).grid(row=11,column=2)
bcomma=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text=",",command=lambda:type1(",")).grid(row=5,column=0)
bpercnt=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="%",command=lambda:type1("percent(")).grid(row=2,column=4)
broot=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="x^(1/y)",command=lambda:type1("root(")).grid(row=6,column=2)
bexp=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="x*10^y",command=lambda:type1("exp(")).grid(row=8,column=4)
bmod=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="| |",command=lambda:type1("mod(")).grid(row=5,column=3)
blog=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="log",command=lambda:type1("log(")).grid(row=4,column=3)
bantlog=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="antilog",command=lambda:type1("antilog(")).grid(row=4,column=4)
bln=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="ln",command=lambda:type1("ln(")).grid(row=5,column=3)
bsinh=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="sinhθ",command=lambda:type1("sinh(")).grid(row=10,column=0)
bcosh=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="coshθ",command=lambda:type1("cosh(")).grid(row=10,column=1)
btanh=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="tanhθ",command=lambda:type1("tanh(")).grid(row=10,column=2)
bnCr=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="nCr",command=lambda:type1("nCr(")).grid(row=6,column=3)
bnPr=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="nPr",command=lambda:type1("nPr(")).grid(row=6,column=4)
be=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="e",command=lambda:type1(2.718281828)).grid(row=4,column=0)
bquad=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="Quad",command=lambda:type1("quad(")).grid(row=11,column=0)
basin=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="asin",command=lambda:type1("arcsin(")).grid(row=9,column=0)
bacos=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="acos",command=lambda:type1("arccos(")).grid(row=9,column=1)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="atan",command=lambda:type1("arctan(")).grid(row=9,column=2)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="∑",command=lambda:type1("summation(")).grid(row=8,column=3)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="D-B",command=lambda:type1("dec_bin(")).grid(row=7,column=0)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="D-O",command=lambda:type1("dec_oct(")).grid(row=7,column=1)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="D-H",command=lambda:type1("dec_hex(")).grid(row=7,column=2)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="B-D",command=lambda:type1("bin_dec(")).grid(row=7,column=3)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="O-D",command=lambda:type1("oct_dec(")).grid(row=7,column=4)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="(2x2)",command=lambda:type1("mat2(")).grid(row=9,column=3)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="(3x3)",command=lambda:type1("mat3(")).grid(row=9,column=4)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="Conv",command=lambda:type1("conv")).grid(row=11,column=4)
batan=Button(cal,width=5,height=1,fg="white",bg="black",font=("arial",20,"bold"),text="H-D",command=lambda:type1("hex_dec(")).grid(row=5,column=4)

























