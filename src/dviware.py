import sys
import fontenc

class DVI:
    """
    constants for DVI and pDVI.
    """
    set_char_MIN = 0
    set_char_MAX = 127
    fnt_num_MIN = 171
    fnt_num_MAX = 234

    set_char_0 = 0
    set_char_1 = 1
    set_char_2 = 2
    set_char_3 = 3
    set_char_4 = 4
    set_char_5 = 5
    set_char_6 = 6
    set_char_7 = 7
    set_char_8 = 8
    set_char_9 = 9
    set_char_10 = 10
    set_char_11 = 11
    set_char_12 = 12
    set_char_13 = 13
    set_char_14 = 14
    set_char_15 = 15
    set_char_16 = 16
    set_char_17 = 17
    set_char_18 = 18
    set_char_19 = 19
    set_char_20 = 20
    set_char_21 = 21
    set_char_22 = 22
    set_char_23 = 23
    set_char_24 = 24
    set_char_25 = 25
    set_char_26 = 26
    set_char_27 = 27
    set_char_28 = 28
    set_char_29 = 29
    set_char_30 = 30
    set_char_31 = 31
    set_char_32 = 32
    set_char_33 = 33
    set_char_34 = 34
    set_char_35 = 35
    set_char_36 = 36
    set_char_37 = 37
    set_char_38 = 38
    set_char_39 = 39
    set_char_40 = 40
    set_char_41 = 41
    set_char_42 = 42
    set_char_43 = 43
    set_char_44 = 44
    set_char_45 = 45
    set_char_46 = 46
    set_char_47 = 47
    set_char_48 = 48
    set_char_49 = 49
    set_char_50 = 50
    set_char_51 = 51
    set_char_52 = 52
    set_char_53 = 53
    set_char_54 = 54
    set_char_55 = 55
    set_char_56 = 56
    set_char_57 = 57
    set_char_58 = 58
    set_char_59 = 59
    set_char_60 = 60
    set_char_61 = 61
    set_char_62 = 62
    set_char_63 = 63
    set_char_64 = 64
    set_char_65 = 65
    set_char_66 = 66
    set_char_67 = 67
    set_char_68 = 68
    set_char_69 = 69
    set_char_70 = 70
    set_char_71 = 71
    set_char_72 = 72
    set_char_73 = 73
    set_char_74 = 74
    set_char_75 = 75
    set_char_76 = 76
    set_char_77 = 77
    set_char_78 = 78
    set_char_79 = 79
    set_char_80 = 80
    set_char_81 = 81
    set_char_82 = 82
    set_char_83 = 83
    set_char_84 = 84
    set_char_85 = 85
    set_char_86 = 86
    set_char_87 = 87
    set_char_88 = 88
    set_char_89 = 89
    set_char_90 = 90
    set_char_91 = 91
    set_char_92 = 92
    set_char_93 = 93
    set_char_94 = 94
    set_char_95 = 95
    set_char_96 = 96
    set_char_97 = 97
    set_char_98 = 98
    set_char_99 = 99
    set_char_100 = 100
    set_char_101 = 101
    set_char_102 = 102
    set_char_103 = 103
    set_char_104 = 104
    set_char_105 = 105
    set_char_106 = 106
    set_char_107 = 107
    set_char_108 = 108
    set_char_109 = 109
    set_char_110 = 110
    set_char_111 = 111
    set_char_112 = 112
    set_char_113 = 113
    set_char_114 = 114
    set_char_115 = 115
    set_char_116 = 116
    set_char_117 = 117
    set_char_118 = 118
    set_char_119 = 119
    set_char_120 = 120
    set_char_121 = 121
    set_char_122 = 122
    set_char_123 = 123
    set_char_124 = 124
    set_char_125 = 125
    set_char_126 = 126
    set_char_127 = 127

    set1 = 128
    set2 = 129
    set3 = 130
    set4 = 131
    set_rule = 132
    put1 = 133
    put2 = 134
    put3 = 135
    put4 = 136
    put_rule = 137
    nop = 138
    bop = 139
    eop = 140
    push = 141
    pop = 142
    right1 = 143
    right2 = 144
    right3 = 145
    right4 = 146
    w0 = 147
    w1 = 148
    w2 = 149
    w3 = 150
    w4 = 151
    x0 = 152
    x1 = 153
    x2 = 154
    x3 = 155
    x4 = 156
    down1 = 157
    down2 = 158
    down3 = 159
    down4 = 160
    y0 = 161
    y1 = 162
    y2 = 163
    y3 = 164
    y4 = 165
    z0 = 166
    z1 = 167
    z2 = 168
    z3 = 169
    z4 = 170

    fnt_num_0 = 171
    fnt_num_1 = 172
    fnt_num_2 = 173
    fnt_num_3 = 174
    fnt_num_4 = 175
    fnt_num_5 = 176
    fnt_num_6 = 177
    fnt_num_7 = 178
    fnt_num_8 = 179
    fnt_num_9 = 180
    fnt_num_10 = 181
    fnt_num_11 = 182
    fnt_num_12 = 183
    fnt_num_13 = 184
    fnt_num_14 = 185
    fnt_num_15 = 186
    fnt_num_16 = 187
    fnt_num_17 = 188
    fnt_num_18 = 189
    fnt_num_19 = 190
    fnt_num_20 = 191
    fnt_num_21 = 192
    fnt_num_22 = 193
    fnt_num_23 = 194
    fnt_num_24 = 195
    fnt_num_25 = 196
    fnt_num_26 = 197
    fnt_num_27 = 198
    fnt_num_28 = 199
    fnt_num_29 = 200
    fnt_num_30 = 201
    fnt_num_31 = 202
    fnt_num_32 = 203
    fnt_num_33 = 204
    fnt_num_34 = 205
    fnt_num_35 = 206
    fnt_num_36 = 207
    fnt_num_37 = 208
    fnt_num_38 = 209
    fnt_num_39 = 210
    fnt_num_40 = 211
    fnt_num_41 = 212
    fnt_num_42 = 213
    fnt_num_43 = 214
    fnt_num_44 = 215
    fnt_num_45 = 216
    fnt_num_46 = 217
    fnt_num_47 = 218
    fnt_num_48 = 219
    fnt_num_49 = 220
    fnt_num_50 = 221
    fnt_num_51 = 222
    fnt_num_52 = 223
    fnt_num_53 = 224
    fnt_num_54 = 225
    fnt_num_55 = 226
    fnt_num_56 = 227
    fnt_num_57 = 228
    fnt_num_58 = 229
    fnt_num_59 = 230
    fnt_num_60 = 231
    fnt_num_61 = 232
    fnt_num_62 = 233
    fnt_num_63 = 234

    fnt1 = 235
    fnt2 = 236
    fnt3 = 237
    fnt4 = 238
    xxx1 = 239
    xxx2 = 240
    xxx3 = 241
    xxx4 = 242
    fnt_def1 = 243
    fnt_def2 = 244
    fnt_def3 = 245
    fnt_def4 = 246
    pre = 247
    post = 248
    post_post = 249
    dir = 255


class DviInterpreter:
    def __init__(self,file,dvimachine):
        self.file=file
        self.dvimachine=dvimachine
        
    def read_u(self,l):
        """
        function to read l bytes from file as an unsigned int.
        """
        bb=self.file.read(l)
        return (int.from_bytes(bb,byteorder='big',signed=False),bb)
    
    def read_ux(self,code,base):
        """
        function to read code-base+1 bytes from file as an unsigned int.
        returns the pair of int and length of bytes.
        """
        len_param=code-base+1
        (c,bb)=self.read_u(len_param)
        return (c,len_param,bb)

    def read_d(self,l):
        """
        function to read l bytes from file as a dimension.
        """
        bb=self.file.read(l)
        return (int.from_bytes(bb,byteorder='big',signed=True),bb)
    
    def read_dx(self,code,base):
        """
        function to read code-base+1 bytes from file as a dimension.
        returns the pair of dimension and length of bytes.
        """
        len_param=code-base+1
        (b,bb)=self.read_d(len_param)
        return (b,len_param,bb)
    
    def read_p(self):
        """
        function to read 4 bytes from file as a pointer.
        """
        bb=self.file.read(4)
        return (int.from_bytes(bb,byteorder='big',signed=True),bb)
    
    def read_str(self,l):
        """
        function to read l bytes from file as a string.
        """
        bb=self.file.read(l)
        return (bb.decode(),bb)

    def readCodeAndArgFromFile(self):
        """
        function to read one code and its parameters.
        """
        (code,bb)=self.read_u(1)
        if DVI.set_char_MIN <= code and code <= DVI.set_char_MAX:
            return(code, [code],0,bb) 
        elif DVI.set1 <= code and code <= DVI.set4:
            (c,len_param,bb1)=self.read_ux(code,DVI.set1)
            return(code, [c],len_param,bb+bb1)
        elif code == DVI.set_rule:
            (a,bb1)=self.read_d(4)
            (b,bb2)=self.read_d(4)
            return(code,[a,b],0,bb+bb1+bb2)
        elif DVI.put1 <= code and code <= DVI.put4:
            (c,len_param,bb1)=self.read_ux(code,DVI.put1)
            return(code,[c],len_param,bb+bb1)
        elif code == DVI.put_rule:
            (a,bb1)=self.read_d(4)
            (b,bb2)=self.read_d(4)
            return(code,[a,b],0,bb+bb1+bb2)
        elif code == DVI.nop:
            return(code,[],0,bb)
        elif code == DVI.bop:
            (c0,bb0)=self.read_d(4)
            (c1,bb1)=self.read_d(4)
            (c2,bb2)=self.read_d(4)
            (c3,bb3)=self.read_d(4)
            (c4,bb4)=self.read_d(4)
            (c5,bb5)=self.read_d(4)
            (c6,bb6)=self.read_d(4)
            (c7,bb7)=self.read_d(4)
            (c8,bb8)=self.read_d(4)
            (c9,bb9)=self.read_d(4)
            (p,bb10)=self.read_p()
            return(code,[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,p],0,bb+bb0+bb1+bb2+bb3+bb4+bb5+bb6+bb7+bb8+bb9+bb10)
        elif code == DVI.eop:
            return(code,[],0,bb)
        elif code == DVI.push:
            return(code,[],0,bb)
        elif code == DVI.pop:
            return(code,[],0,bb)
        elif DVI.right1 <= code and code <= DVI.right4:
            (b,len_param,bb1)=self.read_dx(code,DVI.right1)
            return(code,[b],len_param,bb+bb1)
        elif code == DVI.w0:
            return(code,[0],0,bb)
        elif DVI.w1 <= code and code <= DVI.w4:
            (b,len_param,bb1)=self.read_dx(code,DVI.w1)
            return(code,[b],len_param,bb+bb1)
        elif code == DVI.x0:
            return(code,[0],0,bb)
        elif DVI.x1 <= code and code <= DVI.x4:
            (b,len_param,bb1)=self.read_dx(code,DVI.x1)
            return(code,[b],len_param,bb+bb1)
        elif DVI.down1 <= code and code <= DVI.down4:
            (b,len_param,bb1)=self.read_dx(code,DVI.down1)
            return(code,[b],len_param,bb+bb1)
        elif code == DVI.y0:
            return(code,[0],0,bb)
        elif DVI.y1 <= code and code <= DVI.y4:
            (b,len_param,bb1)=self.read_dx(code,DVI.y1)
            return(code,[b],len_param,bb+bb1)
        elif code == DVI.z0:
            return(code,[0],0,bb)
        elif DVI.z1 <= code and code <= DVI.z4:
            (b,len_param,bb1)=self.read_dx(code,DVI.z1)
            return(code,[b],len_param,bb+bb1)
        elif DVI.fnt_num_MIN <= code and code <= DVI.fnt_num_MAX: 
            return(code,[code-DVI.fnt_num_MIN],0,bb)
        elif DVI.fnt1 <= code and code <= DVI.fnt4:
            (k,len_param,bb1)=self.read_ux(code,DVI.fnt1)
            return(code,[k],len_param,bb+bb1)
        elif DVI.xxx1 <= code and code <= DVI.xxx4:
            (k,len_param,bb1)=self.read_ux(code,DVI.xxx1)
            (x,bb2)=self.read_str(k)
            return(code,[k,x],len_param,bb+bb1+bb2)
        elif DVI.fnt_def1 <= code and code <= DVI.fnt_def4:
            (k,len_param,bb1)=self.read_ux(code,DVI.fnt_def1)
            (c,bb2)=self.read_u(4)
            (s,bb3)=self.read_d(4)
            (d,bb4)=self.read_d(4)
            (a,bb5)=self.read_u(1)
            (l,bb6)=self.read_u(1)
            (n,bb7)=self.read_str(a+l)
            return(code,[k,c,s,d,a,l,n],len_param,bb+bb1+bb2+bb3+bb4+bb5+bb6+bb7)
        elif code == DVI.pre:
            (i,bb1)=self.read_u(1)
            (num,bb2)=self.read_u(4)
            (den,bb3)=self.read_u(4)
            (mag,bb4)=self.read_u(4)
            (k,bb5)=self.read_u(1)
            (x,bb6)=self.read_str(k)
            return(code,[i,num,den,mag,k,x],0,bb+bb1+bb2+bb3+bb4+bb5+bb6)
        elif code == DVI.post:
            (p,bb1)=self.read_p()
            (num,bb2)=self.read_u(4)
            (den,bb3)=self.read_u(4)
            (mag,bb4)=self.read_u(4)
            (l,bb5)=self.read_d(4)
            (u,bb6)=self.read_d(4)
            (s,bb7)=self.read_u(2)
            (t,bb8)=self.read_u(2)
            return(code,[p,num,den,mag,l,u,s,t],0,bb+bb1+bb2+bb3+bb4+bb5+bb6+bb7+bb8)
        elif code == DVI.post_post:
            (q,bb1)=self.read_p()
            (i,bb2)=self.read_u(1)
            return(code,[q,i],0,bb+bb1+bb2)
        elif code == DVI.dir:
            (d,bb1)=self.read_u(1)
            return(code,[d],0,bb+bb1)
        return(code,None,None,bb)
    
    def readCodeAndArg(self):
        """
        function to read and do one code.
        """
        r=None
        (code,arg,version,bb)=self.readCodeAndArgFromFile()
        if DVI.set_char_MIN <= code and code <= DVI.set4:
            r=self.dvimachine.set(arg[0],version,bb)
        elif code == DVI.set_rule:
            r=self.dvimachine.set_rule(arg[0],arg[1],bb)
        elif DVI.put1 <= code and code <= DVI.put4:
            r=self.dvimachine.put(arg[0],version,bb)
        elif code == DVI.put_rule:
            r=self.dvimachine.put_rule(arg[0],arg[1],bb)
        elif code == DVI.nop:
            r=self.dvimachine.nop(bb)
        elif code == DVI.bop:
            r=self.dvimachine.bop(arg[0:10],arg[10],bb)
        elif code == DVI.eop:
            r=self.dvimachine.eop(bb)
        elif code == DVI.push:
            r=self.dvimachine.push(bb)
        elif code == DVI.pop:
            r=self.dvimachine.pop(bb)
        elif DVI.right1 <= code and code <= DVI.right4:
            r=self.dvimachine.right(arg[0],version,bb)
        elif DVI.w0 <= code and code <= DVI.w4:
            r=self.dvimachine.w(arg[0],version,bb)
        elif DVI.x0 <= code and code <= DVI.x4:
            r=self.dvimachine.x(arg[0],version,bb)
        elif DVI.down1 <= code and code <= DVI.down4:
            r=self.dvimachine.down(arg[0],version,bb)
        elif DVI.y0 <= code and code <= DVI.y4:
            r=self.dvimachine.y(arg[0],version,bb)
        elif DVI.z0 <= code and code <= DVI.z4:
            r=self.dvimachine.z(arg[0],version,bb)
        elif DVI.fnt_num_MIN <= code and  code <= DVI.fnt4:
            r=self.dvimachine.fnt(arg[0],version,bb)
        elif DVI.xxx1 <= code and code <= DVI.xxx4:
            r=self.dvimachine.xxx(arg[0],arg[1],version,bb)
        elif DVI.fnt_def1 <= code and code <= DVI.fnt_def4:
            r=self.dvimachine.fnt_def(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],arg[6],version,bb)
        elif code == DVI.pre:
            r=self.dvimachine.pre(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],bb)
        elif code == DVI.post:
            r=self.dvimachine.post(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],arg[6],arg[7],bb)
        elif code == DVI.post_post:
            r=self.dvimachine.post_post(arg[0],arg[1],bb)
        elif code == DVI.dir:
            r=self.dvimachine.d(arg[0],bb)
        return (code,arg,version,r,bb)

    def readCodes(self):
        while True:
            (code,arg,version,r,bb)=self.readCodeAndArg()
            if code==DVI.post_post:
                break

        
class DVIStackMemory:
    """
    This class implements a stack and a register for DVIware.
    """
    def __init__(self,cc,p):
        """
        cc is a list of c0,..,c9 and p is p give as args of bop.
        """
        self.stack=[]
        self.h=0
        self.v=0
        self.w=0
        self.x=0
        self.y=0
        self.z=0
        self.f=-1
        self.shipout_cc=cc
        self.previous_bop=p
        self.direction=0

    def set_direction(d):
        """
        Set direction for pDVI.
        """
        self.direction=d

    def add_to_h(self,b):
        if self.direction == 0:
            self.h=self.h+b
        elif self.direction == 1:
            self.v=self.v+b

    def set_w(self,b):
        self.w=b
    
    def set_x(self,b):
        self.x=b
    
    def add_to_v(self,a):
        if self.direction == 0:
            self.v=self.v+a
        elif self.direction == 1:
            self.h=self.h+a
    
    def set_y(self,a):
        self.y=a

    def set_z(self,a):
        self.z=a

    def set_f(self,x):
        self.f=x
        
    def push(self):
        """
        push (h,v,w,x,y,z) to stack
        """
        data=(self.h,self.v,self.w,self.x,self.y,self.z)
        self.stack.append(data)

    def pop(self):
        """
        pop (h,v,w,x,y,z) from stack
        """
        data=self.stack.pop()
        (self.h,self.v,self.w,self.x,self.y,self.z)=data

class FontList:
    def __init__(self):
        self.fonts={}

    def fnt_def(self,k,directory,name,s,d,c):
        """
        add a new font to list.
        """
        self.fonts[k]=FontDictionary(directory,name,s,d,c)

    def get_unicode(self,fnt_num,c):
        """
        returns unicode string of c as fnt_num.
        """
        return self.fonts[fnt_num].get_unicode(c)

    def get_width(self,fnt_num,c):
        """
        returns width of c.
        """
        return self.fonts[fnt_num].get_width(c)


class FontDictionary:
    def __init__(self,directory,name,s,d,c):
        self.directory=directory
        self.name=name
        self.scaledsize=s
        self.designsize=d
        self.checksum=c
        self.fontattribute=fontenc.FontAttribute.get_from_name(name)

    def get_unicode(self,c):
        """
        translate c to unicode.
        """
        return self.fontattribute.get_unicode(c)
        
    def get_width(self,c):
        """
        returns width of c.
        """
        return 0

class DviStackMachine:
    """
    Stack Machine for DVI.
    """
    def __init__(self,debugmode=False):
        self.fonts=FontList()
        self.stackmemory=None
        self.is_debugmode=debugmode
        self.word=""
    
    def log(self,*s):
        """
        print log if is_debugmode
        """
        if self.is_debugmode:
            print(*s)

    def get_dimension_as_float(self,d):
        """
        returns d*mag*num / den (10^-7 m).
        """
        return float(self.mag*self.num*d)/float(self.den)

    def check_version_of_dvi(self,i):
        """
        Check version
        """
        return True

    def draw_box(self,h,v,a,b):
        """
        primitive function to draw a box.
        """
        self.log("%% box at:", h, v)
        self.log("%% box size:", a, b)
        print("box of size ",a,b)
    
    def draw_char(self,h,v,c):
        """
        primitive function to draw a character.
        """
        self.log("%% char at:", h, v)
        string=self.fonts.get_unicode(self.stackmemory.f,c)
        self.log("%% char:", string)

    def add_to_h(self,b):
        """
        add d to stackmemory.add_to_h.
        """
        self.stackmemory.add_to_h(b)
    
    def add_width_to_h(self,c):
        """
        add width of c to stackmemory.add_to_h.
        """
        width=self.fonts.get_width(self.stackmemory.f,c)
        self.stackmemory.add_to_h(width)
    
    def add_to_v(self,a):
        """
        add a to stackmemory.add_to_v.
        """
        self.stackmemory.add_to_v(a)
    
    def set(self,c,version,bb):
        """
        function for DVI.put.
        this function calls self.draw_char().
        """
        self.log("% set", c)
        self.draw_char(self.stackmemory.h,self.stackmemory.v,c)
        self.add_width_to_h(c)
        
    def set_rule(self,a,b,bb):
        """
        function for DVI.set_rule.
        this function calls self.draw_box().
        """
        self.log("% set rule")
        self.draw_box(self.stackmemory.h,self.stackmemory.v,a,b)
        self.add_to_h(b)
    
    def put(self,c,version,bb):
        """
        function for DVI.put.
        this function calls self.draw_char().
        """
        self.log("% put", c)
        self.draw_char(self.stackmemory.h,self.stackmemory.v,c)

    def put_rule(self,a,b,bb):
        """
        function for DVI.put_rule
        this function calls self.draw_box().
        """
        self.log("% put rule")
        self.log("%%",a,b)
        self.draw_box(self.stackmemory.h,self.stackmemory.v,a,b)

    def nop(self,bb):
        """
        function for DVI.nop.
        """
        self.log("% nop")
    
    def bop(self,cc,p,bb):
        """
        functio for DVI.bop.
        """
        self.stackmemory=DVIStackMemory(cc,p)
        
        self.log("% bop")
        self.log("%% counters:",cc)
        self.log("%% previous bop:", p)
        
    def eop(self,bb):
        """
        function for DVI.eop
        """
        self.log("% eop")

    def push(self,bb):
        """
        funtion for stack.
        function for DVI.push.
        """
        self.stackmemory.push()
        self.log("% push")
        
    def pop(self,bb):
        """
        funtion for stack.
        function for DVI.pop
        """
        self.stackmemory.pop()
        self.log("% pop")

    def right(self,b,version,bb):
        """
        funtion for stack.
        function for DVI.right*
        """
        self.add_to_h(b)
        self.log("% right:", b)

    def w(self,b,version,bb):
        """
        funtion for stack.
        function for DVI.w*
        """
        if version==0:
            self.add_to_h(self.stackmemory.w)
        else:
            self.stackmemory.set_w(b)
            self.add_to_h(b)
        self.log("% w:", self.stackmemory.w)
        
    def x(self,b,version,bb):
        """
        funtion for stack.
        function for DVI.x*
        """
        if version==0:
            self.add_to_h(self.stackmemory.x)
        else:
            self.stackmemory.set_x(b)
            self.add_to_h(b)
        self.log("% x:", self.stackmemory.x)

    def down(self,a,version,bb):
        """
        funtion for stack.
        function for DVI.down*
        """
        self.add_to_v(a)
        self.log("% down:", a)

    def y(self,a,version,bb):
        """
        funtion for stack.
        function for DVI.y*
        """
        if version==0:
            self.add_to_v(self.stackmemory.y)
        else:
            self.stackmemory.set_y(a)
            self.add_to_v(a)
        self.log("% y:", self.stackmemory.y)

    def z(self,a,version,bb):
        """
        funtion for stack.
        function for DVI.z*
        """
        if version==0:
            self.add_to_v(self.stackmemory.z)
        else:
            self.stackmemory.set_z(a)
            self.add_to_v(a)
        self.log("% z:", self.stackmemory.z)
    
    def fnt(self,x,version,bb):
        """
        function for DVI.fnt*
        """
        self.stackmemory.set_f(x)
        self.log("% fnt:", self.stackmemory.f)


    def xxx(self,k,x,version,bb):
        """
        function for DVI.xxx*
        function for spetial
        """
        self.log("%spetial", x)


    def fnt_def(self,k,c,s,d,a,l,n,version,bb):
        """
        function for DVI.fnt_def**
        """
        self.log("% fnt_def")
        self.log("%% font_num =",k)
        self.log("%% check_sum =",c)
        self.log("%% scaled size =",s)
        self.log("%% design size =",d)
        self.log("%% dir :",n[:a])
        self.log("%% name :",n[a:])
        self.fonts.fnt_def(k,n[:a],n[a:],s,d,c)

    def pre(self,i,num,den,mag,k,x,bb):
        """
        function for DVI.pre.
        read preamble and check the version of dvi.
        """
        self.version=i
        self.num=num
        self.den=den
        self.mag=mag
        self.comment=x
        self.log("% pre")
        self.log("%% version :",i)
        self.log("%% mag * num * 1000 / den = ",self.mag,"*",self.num,"*1000/",self.den)
        self.log("%% Comment :",self.comment)
        return self.check_version_of_dvi(i)
        
    def post(self,p,num,den,mag,l,u,s,t,bb):
        """
        function for DVI.post.
        read postamble.
        """
        self.num=num
        self.den=den
        self.mag=mag
        self.max_height_depth=l
        self.max_width=u
        self.max_depth_of_stack=s
        self.total_pages=t
        self.log("% post")
        self.log("%% mag * num * 1000 / den = ",self.mag,"*",self.num,"*1000/",self.den)

        self.log("%% max height+depth =", self.max_height_depth)
        self.log("%% max width =", self.max_width)
        self.log("%% max depth of stack =", self.max_depth_of_stack)
        self.log("%% num of pages =", self.total_pages)
        self.log("%% previous bop =", p)
    
    def post_post(self,q,i,bb):
        """
        function for DVI.post_post.
        read postamble.
        """
        self.version=i
        self.log("% post_post")
        self.log("%% post =",q)
        self.log("%% self =",self.version)
        return self.check_version_of_dvi(i)

    def d(self,d,bb):
        """
        function for DVI.d for pDVI format.
        """
        self.stackmemory.set_direction(d)
        self.log("% d:", d)

def test():
    if len(sys.argv)<2:
        print("usage: python3 "+sys.argv[0]+" dvifile")
        return
    filename=sys.argv[1]
    with open(filename, mode='r+b') as file:
        dvistackmachine=DviStackMachine(debugmode=True)
        #dvistackmachine=DviStackMachine(debugmode=False)
        dviinterpreter=DviInterpreter(file,dvistackmachine)
        dviinterpreter.readCodes()

if __name__=="__main__":
    test()
