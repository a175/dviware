def read_words_as_str(file,l):
    """
    function to read 4*l bytes from file as a string.
    """
    bb=file.read(4*l)
    return bb.decode()

def read_words_as_bytes(file,l):
    """
    function to read 4*l bytes from file as bytes
    """
    bb=file.read(4*l)
    return (bb)

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
    function to read 4 bytes from file as an unsigned int.
    """
    bb=file.read(4)
    return (int.from_bytes(bb,byteorder='big',signed=False))





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

            
        

    @classmethod
    def set_by_file(cls,file):
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
        ne=read_half_word(file)
        np=read_half_word(file)
        header=Header.get_from_file(file,lh)
        charinfo=CharInfo.get_from_file(file,ec-bc+1)
        width=IntegerWords.get_from_file(file,nw)
        height=IntegerWords.get_from_file(file,nh)
        depth=IntegerWords.get_from_file(file,nd)
        italic=IntegerWords.get_from_file(file,ni)
        ligkern=LigKern.get_from_file(file,nl)
        kern=IntegerWords.get_from_file(file,nk)
        exten=IntegerWords.get_from_file(file,ne)
        param=Param.get_from_file(file,np)

        return cls(header,charinfo,width,height,depth,italic,ligkern,kern,exten,param)
        
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
        encodingschema=read_words_as_str(file,10)
        fontfamily=read_words_as_str(file,5)
        seven_bit_safe_flag=read_quarter_word(file)
        x1=read_quarter_word(file)
        x2=read_quarter_word(file)
        face=cls.int_to_face(read_quarter_word(file))
        x3=read_words_as_bytes(file,lh-18)
        return cls(checksum,designsize,encodingschema,fontfamily,seven_bit_safe_flag,x1,x2,face,x3)

class CharInfo:
    def __init__(self,c):
        self.data=c

    @classmethod
    def get_from_file(cls,file,lh):
        c=[]
        for i in range(lh):
            c.append(CharInfoWord.get_from_file(file))
        return cls(c)

class CharInfoWord:
    def __init__(self,width_index,height_index,depth_index,italic_index,tag,remainder):
        self.width_index=width_index
        self.height_index=height_index
        self.depth_index=depth_index
        self.italic_index=italic_index
        self.tag=tag
        self.remainder=remainder
    
    @classmethod
    def int_to_height_depth(cls,d):
        depth=d % 16
        height=(d-depth)//16
        return (height,depth)
    @classmethod
    def int_to_italic_tag(cls,d):
        tag=d % 4
        italic=(d-depth)//4
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

class IntegerWords:
    def __init__(self,data):
        self.data=data

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
        self.next_char
        self.op_byte=op_byte
        self.reminder=reminder
    @classmethod
    def get_from_file(cls,file):
        skip=read_quarter_word(file)
        next_char=read_quarter_word(file)
        op_byte=read_quarter_word(file)
        reminder=read_quarter_word(file)
        return cls(skip,next_char,op_byte,reminder)

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

    @classmethod
    def get_from_file(cls,file,l):
        print(l)
        slant=read_quarter_word(file)
        space=read_quarter_word(file)
        space_stretch=read_quarter_word(file)
        space_shrink=read_quarter_word(file)
        x_height=read_quarter_word(file)
        quad=read_quarter_word(file)
        extra_space=read_quarter_word(file)
        return cls(slant,space,space_stretch,space_shrink,x_height,quad,extra_space)
