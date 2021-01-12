
class Tfm:
    def __init__(self):
        self.preamble=Preamble()
        self.header=Header()
        self.char_info=CharInfo()
        self.width=IntegerWords()
        self.height=IntegerWords()
        self.depth=IntegerWords()
        self.italic=IntegerWords()
        self.lig_kern=LigKern()
        self.kern=IntegerWords()
        self.exten=Exten()
        self.param=Param()


class IntegerWords:
    def __init__(self):
        self.words=[]

    def append_from_file(cls,file):
        self.word.append()

class Preamble:
    def __init__(self):
        pass

    def set(self,lf,lh,bc,ec,nw,nh,nd,ni,nl,nk,ne,np):
        self.lf=lf
        self.lh=lh
        self.bc=bc
        self.ec=ec
        self.nw=nw
        self.nh=nh
        self.nd=nd
        self.ni=ni
        self.nl=nl
        self.nk=nk
        self.ne=ne
        self.np=np
    
class Header:
    def __init__(self):
        pass
    
    def set(self,checksum,designsize,encodingschema,fontfamily,seven_bit_safe_flag,x1,x2,face,x3):
        self.checksum=checksum
        self.designsize=designsize
        self.encodingschema=encodingschema
        self.fontfamily=fontfamily
        self.seven_bit_safe_flag=seven_bit_safe_flag
        self.x1=x1
        self.x2=x2
        self.face=face
        self.x3=x3


class CharInfo:
    def __init__(self):
        self.charinfowords=[]
    def appendCharInfoWord(self,charinfoword):
        self.charinfowords.append(charinfoword)

class CharInfoWord:
    def __init__(self,width_index,height_index,depth_index,italic_index,tag,remainder):
        self.width_index=width_index
        self.height_index=height_index
        self.depth_index=depth_index
        self.italic_index=italic_index
        self.tag=tag
        self.remainder=remainder

class LigKern:
    def __init__(self):
        self.data=[]

    
class LigKernWord:
    def __init__(self,skip,next_char,op_byte,reminder):
        self.skip=skip
        self.next_char
        self.op_byte=op_byte
        self.reminder=reminder

class Exten:
    def __init__(self):
        self.data=[]


class ExtenWord:
    def __init__(self,h,m,b,c):
        self.h=h
        self.m=m
        self.b=b
        self.c=c

class Param:
    def __init__(self,slant,space,space_stretch,space_shrink,x_height,quad,extra_space):
        self.slant=slant
        self.space=space
        self.space_stretch=space_stretch
        self.space_shrink=space_shrink
        self.x_height=x_height
        self.quad=quad
        self.extra_space=extra_space
        #For TeX math symbols
        #num1, num2, num3, demon1. demon2, sup1, sup2, sup3, sub1, sub2, supdrop, subdrop, dimen1, dimen2, axis_height
        #For TeX math extension
        #default_rule_thickness, big_op_spacing1, big_op_spacing5

