import docx
import sys
import dviware

class DviDocxStackMachine(dviware.DviStackMachine):
    def __init__(self,debugmode=False):
        super().__init__(debugmode)
        self.document = docx.Document()
        self.p = None
        self.r = None
        self.is_mathmode = False

    def bop(self,cc,p):
        """
        functio for DVI.bop.
        """
        ans=super().bop(cc,p)
        if self.p:
            document.add_page_break()

    def draw_char(self,h,v,c):
        """
        add a character to paragraph as new run.
        """
        ans=super().draw_char(h,v,c)
        string=self.fonts.get_unicode(self.stackmemory.f,c)
        if not self.is_mathmode:
            if self.r:
                self.r.add_text(string)
            else:
                self.p=self.document.add_paragraph()
                self.r=self.p.add_run(string)
        return(ans)

    def add_to_h(self,b,call_from_set=False):
        """
        add d to stackmemory.add_to_h.
        """
        super().add_to_h(b)
        if not call_from_set:
            if b>0:
                if self.p:
                    if b>100000:
                        self.r.add_text(" ")

    def add_to_v(self,a):
        """
        add a to stackmemory.add_to_v.
        """
        super().add_to_v(a)
        if a > 0:
            if self.p:
                self.r.add_text(" ")
    def xxx(self,k,x,version):
        """
        function for spectial
        """
        ans=super().xxx(k,x,version)
        if x.startswith("texstructure:"):
            lit=x[13:]
            if lit=="begin_par":
                self.p = self.document.add_paragraph()
                self.r=self.p.add_run()
            elif lit.startswith("begin_math"):
                mathnum=lit[10:]
                self.is_mathmode=True
                self.r=self.p.add_run()
                self.r.add_text("[inline math"+mathnum+"]")
            elif lit=="end_math":
                self.is_mathmode=False
                self.r=self.p.add_run()
            elif lit=="begin_display":
                mathnum=lit[13:]
                self.is_mathmode=True
                self.r=self.p.add_run()
                self.r.add_text("[display math"+mathnum+"]")
            elif lit=="end_display":
                self.is_mathmode=False
                self.r=self.p.add_run()
        return(ans)
    
def test():
    if len(sys.argv)<2:
        print("usage: python3 "+sys.argv[0]+" dvifile")
        return
    filename=sys.argv[1]
    with open(filename, mode='r+b') as file:
        #dvistackmachine=DviDocxStackMachine(debugmode=True)
        dvistackmachine=DviDocxStackMachine(debugmode=False)
        dviinterpreter=dviware.DviInterpreter(file,dvistackmachine)
        dviinterpreter.readCodes()
        dvistackmachine.document.save(sys.argv[1]+'.docx')
        
if __name__=="__main__":
    test()


