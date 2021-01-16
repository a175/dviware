import sys
import os

"""
denominator of fixed word
"""
DEN=2**12

def read_words_as_str(file,l):
    """
    function to read 4*l bytes from file as a string.
    """
    n=read_quarter_word(file)
    bb=file.read(4*l-1)
    return (bb[:n].decode(),n)

def read_words_as_bytes(file,l):
    """
    function to read 4*l bytes from file as bytes
    """
    bb=file.read(4*l)
    return (bb)

def read_three_quarter_word_as_jfm_endian(file):
    """
    function to read 3 bytes from file as an unsigned int with endian such that 0xABcdfe for cdfeAB.
    """
    bb=file.read(3)
    bbb=bb[2:]+bb[:2]
    return (int.from_bytes(bbb,byteorder='big',signed=False))

def read_quarter_word(file):
    """
    function to read 1 bytes from file as an unsigned int.
    """
    bb=file.read(1)
    return (int.from_bytes(bb,byteorder='big',signed=False))

def read_half_word(file):
    """
    function to read 2 bytes from file as an unsigned int.
    """
    bb=file.read(2)
    return (int.from_bytes(bb,byteorder='big',signed=False))

def read_word(file):
    """
    function to read 4 bytes from file as an signed int.
    """
    bb=file.read(4)
    return (int.from_bytes(bb,byteorder='big',signed=True))


class ZeroTfm:
    def __init__(self,fontname,design_size):
        self.fontname=fontname
        self.design_size=design_size

    def get_design_size_sp(self):
        return (0,(1,1))
    
    def get_width_sp(self,c):
        return (0,(1,1))

    def get_minimum_space_between_word_sp(self):
        return (0,(1,1))

    def get_checksum(self):
        return 0

    def get_bc(self):
        return 0

    def get_len(self):
        return 0

class Tfm:
    def __init__(self,header,charinfo,width,height,depth,italic,ligkern,kern,exten,param):
        self.header=header
        self.charinfo=charinfo
        self.width=width
        self.height=height
        self.depth=depth
        self.italic=italic
        self.ligkern=ligkern
        self.kern=kern
        self.exten=exten
        self.param=param

    def get_design_size_sp(self):
        """
        returns pair of designsize and (num,den)
        such that designsize*num/den is design size in sp.
        """
        ds=self.header.get_design_size()
        return (ds,(1,DEN))
    
    def get_width_sp(self,c):
        """
        returns pair of width and (num,den)
        such that width*num/den is width of character c in sp.
        """
        wi=self.charinfo.get_width_index(c)
        w=self.width.get_data_at(wi)
        (ds,scale)=self.get_design_size_sp()
        (num,den)=scale
        return (w,(ds*num,den*DEN))

    def get_minimum_space_between_word_sp(self):
        """
        returns pair of width and (num,den)
        such that width*num/den is width of minimum space in sp.
        """
        (ds,scale)=self.get_design_size_sp()
        (num,den)=scale
        return (self.param.space-self.param.space_shrink,(ds*num,den*DEN))

    def get_tag(self,c):
        t=self.charinfo.get_tag(c)
        return t

    def get_checksum(self):
        return self.header.get_checksum()

    def get_bc(self):
        return self.charinfo.bc

    def get_len(self):
        return self.charinfo.get_len()

    @classmethod
    def get_from_file(cls,file,first_half_word=None):
        if first_half_word == None:
            lf=read_half_word(file)
        else:
            lf=first_half_word

        lh=read_half_word(file)
        
        bc=read_half_word(file)
        ec=read_half_word(file)
        
        nw=read_half_word(file)
        nh=read_half_word(file)
        
        nd=read_half_word(file)
        ni=read_half_word(file)
        
        nl=read_half_word(file)
        nk=read_half_word(file)
        
        ne=read_half_word(file)
        np=read_half_word(file)
        
        header=Header.get_from_file(file,lh)
        charinfo=CharInfo.get_from_file(file,bc,ec)
        width=IntegerWords.get_from_file(file,nw)
        height=IntegerWords.get_from_file(file,nh)
        depth=IntegerWords.get_from_file(file,nd)
        italic=IntegerWords.get_from_file(file,ni)
        ligkern=LigKern.get_from_file(file,nl)
        kern=IntegerWords.get_from_file(file,nk)
        exten=IntegerWords.get_from_file(file,ne)
        if header.encodingschema.startswith("TeX math symbols"):
            param=ParamTeXMathSymbols.get_from_file(file,np)
        elif header.encodingschema.startswith("TeX math extension"):
            param=ParamTeXMathExtension.get_from_file(file,np)
        else:
            param=Param.get_from_file(file,np)

        return cls(header,charinfo,width,height,depth,italic,ligkern,kern,exten,param)

class Jfm(Tfm):
    def __init__(self,header,chartype,charinfo,width,height,depth,italic,gluekern,kern,glue,param):
        super().__init__(header,charinfo,width,height,depth,italic,None,kern,None,param)
        self.chartype=chartype
        self.gulekern=gluekern
        self.glue=glue
    
    def get_width_sp(self,c):
        """
        returns pair of width of character c and (num,den)
        such that width*num/den is width in sp.
        """
        cx=c % 16777216
        ctype=self.chartype.get_chartype(cx)
        wi=self.charinfo.get_width_index(ctype)
        w=self.width.get_data_at(wi)
        ds=self.header.get_design_size()
        return (w,ds)

    def get_minimum_space_between_word_sp(self):
        """
        returns pair of width and (num,den)
        such that width*num/den is width of minimum space in sp.
        Usually Japanese language has no space between words.
        """
        kk=self.param.kanji_space+self.param.kanji_space_stretch
        ke=self.param.xkanji_space+self.param.xkanji_space_stretch
        (ds,scale)=self.get_design_size_sp()
        (num,den)=scale
        return (max(kk,ke)+2*den*DEN,(ds*num,den*DEN))

    @classmethod
    def get_from_file(cls,file,first_half_word = None):
        if first_half_word == None:
            jfm_id=read_half_word(file)
        else:
            jfm_id=first_half_word

        jfm_nt = read_half_word(file)
        
        lf=read_half_word(file)
        lh=read_half_word(file)
        
        bc=read_half_word(file)
        ec=read_half_word(file)
        
        nw=read_half_word(file)
        nh=read_half_word(file)
        
        nd=read_half_word(file)
        ni=read_half_word(file)
        
        nl=read_half_word(file)
        nk=read_half_word(file)
        
        ng=read_half_word(file)
        np=read_half_word(file)

        header=Header.get_from_file(file,lh)
        chartype=CharType.get_from_file(file,jfm_nt)
        charinfo=CharInfo.get_from_file(file,bc,ec)
        width=IntegerWords.get_from_file(file,nw)
        height=IntegerWords.get_from_file(file,nh)
        depth=IntegerWords.get_from_file(file,nd)
        italic=IntegerWords.get_from_file(file,ni)        
        gluekern=GlueKern.get_from_file(file,nl)
        kern=IntegerWords.get_from_file(file,nk)
        glue=Glue.get_from_file(file,ng)
        param=JfmParam.get_from_file(file,np)

        return cls(header,chartype,charinfo,width,height,depth,italic,gluekern,kern,glue,param)
    
class Header:
    ROMAN=0
    ITALIC=1
    MEDIUM=0
    BOLD=2
    LIGHT=4
    REGULAR=0
    CONDENSED=6
    EXTENDED=12

    
    def __init__(self,checksum,designsize,encodingschema,fontfamily,seven_bit_safe_flag,x1,x2,face,x3):
        self.checksum=checksum
        self.designsize=designsize
        self.encodingschema=encodingschema
        self.fontfamily=fontfamily
        self.seven_bit_safe_flag=seven_bit_safe_flag
        self.x1=x1
        self.x2=x2
        self.face=face
        self.x3=x3

    def get_design_size(self):
        return self.designsize

    def get_checksum(self):
        return self.checksum
    
    @classmethod
    def int_to_face(cls,d):
        if d % 2 == 0:
            slope=cls.ROMAN
            d=d//2
        else:
            slope=cls.ITALIC
            d=(d-1)//2
        if d % 3 == 0:
            weight = cls.MEDIUM
            d=d//3
        elif d % 3 == 1:
            weight = cls.BOLD
            d=(d-1)//3
        else:
            weight = cls.LIGHT
            d=(d-2)//3
        if d % 3 == 0:
            expansion=cls.REGULAR
        elif d % 3 == 1:
            expansion=cls.CONDENSED
        else:
            expansion=cls.EXTENDED
        return (weight, slope, expansion)

    @classmethod
    def get_from_file(cls,file,lh):
        checksum=read_word(file)
        designsize=read_word(file)
        (encodingschema,le)=read_words_as_str(file,10)
        (fontfamily,lf)=read_words_as_str(file,5)
        seven_bit_safe_flag=read_quarter_word(file)
        x1=read_quarter_word(file)
        x2=read_quarter_word(file)
        face=cls.int_to_face(read_quarter_word(file))
        x3=read_words_as_bytes(file,lh-18)
        return cls(checksum,designsize,encodingschema,fontfamily,seven_bit_safe_flag,x1,x2,face,x3)

class CharInfo:
    def __init__(self,c,bc):
        self.data=c
        self.bc=bc

    def get_width_index(self,c):
        ci=self.data[c-self.bc]
        return ci.get_width_index()
        
    def get_tag(self,c):
        ci=self.data[c-self.bc]
        return ci.get_tag()

    def get_len(self):
        return len(self.data)

    @classmethod
    def get_from_file(cls,file,bc,ec):
        l=ec-bc+1
        c=[]
        for i in range(l):
            c.append(CharInfoWord.get_from_file(file))
        return cls(c,bc)

class CharInfoWord:
    def __init__(self,width_index,height_index,depth_index,italic_index,tag,remainder):
        self.width_index=width_index
        self.height_index=height_index
        self.depth_index=depth_index
        self.italic_index=italic_index
        self.tag=tag
        self.remainder=remainder

    def get_width_index(self):
        return self.width_index
        
    def get_tag(self):
        return self.tag
        
    @classmethod
    def int_to_height_depth(cls,d):
        depth=d % 16
        height=(d-depth)//16
        return (height,depth)
    @classmethod
    def int_to_italic_tag(cls,d):
        tag=d % 4
        italic=(d-tag)//4
        return (italic,tag)

    @classmethod
    def get_from_file(cls,file):
        width_index=read_quarter_word(file)
        hd=read_quarter_word(file)
        (height_index,depth_index)=cls.int_to_height_depth(hd)
        it=read_quarter_word(file)
        (italic_index,tag)=cls.int_to_italic_tag(it)
        remainder=read_quarter_word(file)
        return cls(width_index,height_index,depth_index,italic_index,tag,remainder)

class CharType:
    def __init__(self,data):
        self.data=data

    def get_chartype(self,c):
        for ctw in self.data:
            if ctw.is_for(c):
                return ctw.get_ctype()
        return 0

    @classmethod
    def get_from_file(cls,file,l):
        d=[]
        for i in range(l):
            d.append(CharTypeWord.get_from_file(file))
        return cls(d)


class CharTypeWord:
    def __init__(self,c,ctype):
        self.c=c
        self.ctype=ctype

    def is_for(self,c):
        if self.c==c:
            return True
        else:
            return False

    def get_ctype(self):
        return self.c

    @classmethod
    def get_from_file(cls,file):
        c=read_three_quarter_word_as_jfm_endian(file)
        ctype=read_quarter_word(file)
        return cls(c,ctype)
    
class IntegerWords:
    def __init__(self,data):
        self.data=data

    def get_data_at(self,i):
        return self.data[i]
    
    @classmethod
    def get_from_file(cls,file,l):
        d=[]
        for i in range(l):
            d.append(read_word(file))
        return cls(d)

    
class LigKern:
    def __init__(self,d):
        self.data=d

    @classmethod
    def get_from_file(cls,file,l):
        c=[]
        for i in range(l):
            c.append(LigKernWord.get_from_file(file))
        return cls(c)
    
class LigKernWord:
    def __init__(self,skip,next_char,op_byte,reminder):
        self.skip=skip
        self.next_char=next_char
        self.op_byte=op_byte
        self.reminder=reminder
    @classmethod
    def get_from_file(cls,file):
        skip=read_quarter_word(file)
        next_char=read_quarter_word(file)
        op_byte=read_quarter_word(file)
        reminder=read_quarter_word(file)
        return cls(skip,next_char,op_byte,reminder)

class GlueKern:
    def __init__(self,d):
        self.data=d

    @classmethod
    def get_from_file(cls,file,l):
        c=[]
        for i in range(l):
            c.append(GlueKernWord.get_from_file(file))
        return cls(c)

class GlueKernWord:
    def __init__(self,skip,char_type,op_byte,reminder):
        self.skip=skip
        self.char_type=char_type
        self.op_byte=op_byte
        self.reminder=reminder
    @classmethod
    def get_from_file(cls,file):
        skip=read_quarter_word(file)
        char_type=read_quarter_word(file)
        op_byte=read_quarter_word(file)
        reminder=read_quarter_word(file)
        return cls(skip,char_type,op_byte,reminder)

class Glue:
    def __init__(self,d):
        self.data=d

    @classmethod
    def get_from_file(cls,file,l):
        c=[]
        for i in range(l//3):
            c.append(GlueKernWord.get_from_file(file))
        return cls(c)

class GlueTripleWord:
    def __init__(self,width,stretch,shrink):
        self.width=width
        self.stretch=stretch
        self.shrink=shrink

    @classmethod
    def get_from_file(cls,file):
        width=read_quarter_word(file)
        stretch=read_quarter_word(file)
        shrink=read_quarter_word(file)
        return cls(width,stretch,shrink)


class Exten:
    def __init__(self,d):
        self.data=d

    @classmethod
    def get_from_file(cls,file,l):
        c=[]
        for i in range(l):
            c.append(ExtenWord.get_from_file(file))
        return cls(c)

class ExtenWord:
    def __init__(self,t,m,b,r):
        self.top=t
        self.mid=m
        self.bot=b
        self.rep=r

    @classmethod
    def get_from_file(cls,file):
        t=read_quarter_word(file)
        m=read_quarter_word(file)
        b=read_quarter_word(file)
        r=read_quarter_word(file)
        return cls(t,m,b,r)
    
class Param:
    def __init__(self,slant,space,space_strech,space_shrink,x_height,quad,extra_space,xxx):
        self.slant=slant
        self.space=space
        self.space_strech=space_strech
        self.space_shrink=space_shrink
        self.x_height=x_height
        self.quad=quad
        self.extra_space=extra_space
        self.xxx=xxx

    @classmethod
    def get_from_file(cls,file,l):
        if l > 0:
            slant=read_word(file)
        else:
            slant=0
        l=l-1
        if l > 0:
            space=read_word(file)
        else:
            space=0
        l=l-1
        if l > 0:            
            space_stretch=read_word(file)
        else:
            space_stretch=0
        l=l-1
        if l > 0:
            space_shrink=read_word(file)
        else:
            space_shrink=0
        l=l-1
        if l > 0:
            x_height=read_word(file)
        else:
            x_height=0
        l=l-1
        if l > 0:
            quad=read_word(file)
        else:
            quad=0
        l=l-1
        if l > 0:
            extra_space=read_word(file)
        else:
            extra_space=0
        if l>0:
            xxx=None
        else:
            xxx=read_words_as_bytes(file,l)            
        return cls(slant,space,space_stretch,space_shrink,x_height,quad,extra_space,xxx)

class ParamTeXMathSymbols(Param):
    #For TeX math symbols
    def __init__(self,slant,space,space_stretch,space_shrink,x_height,quad,extra_space,num1, num2, num3, demon1, demon2, sup1, sup2, sup3, sub1, sub2, supdrop, subdrop, dimen1, dimen2, axis_height,xxx):
        super().__init__(slant,space,space_stretch,space_shrink,x_height,quad,extra_space,xxx)
        self.math_space=self.extra_space
        self.num1=num1
        self.num2=num2
        self.num3=num3
        self.demon1=demon1
        self.demon2=demon2
        self.sup1=sup1
        self.sup2=sup2
        self.sup3=sup3
        self.sub1=sub1
        self.sub2=sub2
        self.supdrop=supdrop
        self.subdrop=subdrop
        self.dimen1=dimen1
        self.dimen2=dimen2
        self.axis_height=axis_height
    
    @classmethod
    def get_from_file(cls,file,l):
        slant=read_word(file)
        space=read_word(file)
        space_stretch=read_word(file)
        space_shrink=read_word(file)
        x_height=read_word(file)
        quad=read_word(file)
        extra_space=read_word(file)
        num1=read_word(file)
        num2=read_word(file)
        num3=read_word(file)
        demon1=read_word(file)
        demon2=read_word(file)
        sup1=read_word(file)
        sup2=read_word(file)
        sup3=read_word(file)
        sub1=read_word(file)
        sub2=read_word(file)
        supdrop=read_word(file)
        subdrop=read_word(file)
        dimen1=read_word(file)
        dimen2=read_word(file)
        axis_height=read_word(file)
        if l==22:
            xxx=None
        else:
            xxx=read_words_as_bytes(file,l-22)            
        return cls(slant,space,space_stretch,space_shrink,x_height,quad,extra_space,num1, num2, num3, demon1, demon2, sup1, sup2, sup3, sub1, sub2, supdrop, subdrop, dimen1, dimen2, axis_height,xxx)

class ParamTeXMathExtension(Param):
    #For TeX math extension
    def __init__(self,slant,space,space_stretch,space_shrink,x_height,quad,extra_space,default_rule_thickness,big_op_spacing1,big_op_spacing2,big_op_spacing3,big_op_spacing4,big_op_spacing5,xxx):
        super().__init__(slant,space,space_stretch,space_shrink,x_height,quad,extra_space,xxx)
        self.default_rule_thickness=default_rule_thickness
        self.big_op_spacing1=big_op_spacing1
        self.big_op_spacing2=big_op_spacing2
        self.big_op_spacing3=big_op_spacing3
        self.big_op_spacing4=big_op_spacing4
        self.big_op_spacing5=big_op_spacing5

    @classmethod
    def get_from_file(cls,file,l):
        slant=read_word(file)
        space=read_word(file)
        space_stretch=read_word(file)
        space_shrink=read_word(file)
        x_height=read_word(file)
        quad=read_word(file)
        extra_space=read_word(file)
        default_rule_thickness=read_word(file)
        big_op_spacing1=read_word(file)
        big_op_spacing2=read_word(file)
        big_op_spacing3=read_word(file)
        big_op_spacing4=read_word(file)
        big_op_spacing5=read_word(file)
        if l==13:
            xxx=None
        else:
            xxx=read_words_as_bytes(file,l-13)            
        return cls(slant,space,space_stretch,space_shrink,x_height,quad,extra_space,default_rule_thickness,big_op_spacing1,big_op_spacing2,big_op_spacing3,big_op_spacing4,big_op_spacing5,xxx)
        
        
class JfmParam:
    def __init__(self,slant,kanji_space,kanji_space_stretch,kanji_space_shrink,zh,zw,xkanji_space,xkanji_space_stretch,xkanji_space_shrink,xxx):
        self.slant=slant
        self.kanji_space=kanji_space
        self.kanji_space_stretch=kanji_space_stretch
        self.kanji_space_shrink=kanji_space_shrink
        self.zh=zh
        self.zw=zw
        self.xkanji_space=xkanji_space
        self.xkanji_space_stretch=xkanji_space_stretch
        self.xkanji_space_shrink=xkanji_space_shrink
        self.xxx=xxx

    @classmethod
    def get_from_file(cls,file,l):
        slant=read_word(file)
        kanji_space=read_word(file)
        kanji_space_stretch=read_word(file)
        kanji_space_shrink=read_word(file)
        zh=read_word(file)
        zw=read_word(file)
        xkanji_space=read_word(file)
        xkanji_space_stretch=read_word(file)
        xkanji_space_shrink=read_word(file)

        if l==9:
            xxx=None
        else:
            xxx=read_words_as_bytes(file,l-7)            
        return cls(slant,kanji_space,kanji_space_stretch,kanji_space_shrink,zh,zw,xkanji_space,xkanji_space_stretch,xkanji_space_shrink,xxx)



def search_tfm_file_path(tfm,texmfpaths):
    for texmfpath in texmfpaths:
        lsr=os.path.join(texmfpath,"ls-R")
        if os.path.exists(lsr):
            with open(lsr) as file:
                d=""
                for l in file:
                    line=l.strip()
                    if line.startswith("./"):
                        d=line[2:-1]
                    if line==tfm:
                        return(os.path.join(texmfpath,d,tfm))
        else:
            fontdir=os.path.join(texmfpath,"fonts","tfm")
            if os.path.exists(fontdir):
                for d1 in os.listdir(fontdir):
                    fontdir1=os.path.join(fontdir,d1)
                    if os.path.isdir(fontdir1):
                        for d2 in os.listdir(fontdir1):
                            fontdir2=os.path.join(fontdir1,d2)
                            if os.path.isdir(fontdir2):
                                for f in os.listdir(fontdir2):
                                    if f==tfm:
                                        return os.path.join(fontdir2,f)
    return None

def search_and_get_by_name(name,directory,designsize,checksum,texmfpaths):
    fontname=directory+name
    filename=search_tfm_file_path(fontname+".tfm",texmfpaths)
    if filename != None:
        with open(filename, mode='rb') as file:
            fh=read_half_word(file)        
            if fh == 11 or fh == 9:
                tfm=Jfm.get_from_file(file,fh)
            else:
                tfm=Tfm.get_from_file(file,fh)
            cs=tfm.get_checksum()
            if cs==checksum or cs==0 or checksum==0:
                return tfm
    return ZeroTfm(fontname,designsize)

def test():
    if len(sys.argv)<3:
        print("usage: python3 "+sys.argv[0]+" font texmfpath")
        print("e.g.:  cmr10 /usr/share/texlive/texmf-dist/")
        return
    
    tfm=search_and_get_by_name(sys.argv[1],"",10,0,[sys.argv[2]])
    print(tfm,tfm.get_checksum())
    print(tfm.header.fontfamily)
    print(tfm.header.designsize)
    bc=tfm.get_bc()
    for i in range(tfm.get_len()):
        c=bc+i
        print(hex(c),'=',c,tfm.get_width_sp(c),tfm.get_tag(c))
    #print(tfm.param.space,tfm.param.space_strech,tfm.param.space_shrink,tfm.param.x_height,tfm.param.quad,tfm.param.extra_space)
        
if __name__ == "__main__":
    test()

