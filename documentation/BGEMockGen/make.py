from bs4 import BeautifulSoup
import requests, os

#Configuration Variables
search_refs = True
build_path = "API"
API_URL = "https://pythonapi.upbge.org/"

#Further addons
headers = {"bge" + os.sep + "types.py" : """
import mathutils

inf = 0
class CListValue:
    def __init__(self, ctype):
        self.__ret__ = ctype
        self.__i__ = None
        self.__itf__ = False

    def __instanceme__(self):
        if self.__i__ == None:
            self.__i__ = self.__ret__()
        return self.__i__

    def __getitem__(self, key): return self.__instanceme__()
    def __setitem__(self, key, val): return self.__instanceme__()
    def get(self, key): return self.__instanceme__()

    def __iter__(self): return self
    def __next__(self):
        self.__itf__ = not self.__itf__
        if self.__itf__: return self.__instanceme__()
        else: raise StopIteration
""",
"bge" + os.sep + "logic.py" :
"""globalDict = {}
keyboard = None
mouse = None
joysticks = []
"""}

erase = {"bge" + os.sep + "logic.py" : [
"""globalDict = None
keyboard = None
mouse = None
joysticks = None"""]}

fixes = {
"RandomMusic": [(", transition=(5)", ", transition=(5,0,0))")]
}

def dataToPath(dp):
    i = dp.rfind(".")
    return os.path.normpath(dp[:len(dp) if i == -1 else i].replace(".", "/") + ".py")

class File:
    done_files = []
    done_urls = []
    registred_class = {}

    def __init__(self, url, recursive=False, prefix=""):
        self.current_class = ""
        self.current_module = ""
        self.recursive = recursive

        self.makePage(url, recursive=recursive, prefix=prefix)

    def getType(self, dl, noerror=False):
        if dl==None: raise Exception("dl should not be None")
        if type(dl)!=str:
            try: t = dl.dd.table.tbody.tr.td.get_text()
            except Exception: return "None"
        else: t=dl
        t=t.replace("\t", "")
        t=t.replace("‘s", "")

        #Correctors
        if t == "MeshProxy": t = "KX_MeshProxy"
        if t == "boolen": t = "bool"

        #Registred
        if t == self.current_class: return "self"
        if t in File.registred_class.keys():
            m = File.registred_class[t]
            if self.current_module == m: return t + "()"
            else: return m + '.' + t +"()"
        for k, v in File.registred_class.items():
            m = v+'.'+k
            if m == t: return m + "()"

        #Direct addressing
        if t in ["float", "int", "bool"]: return t + "()"
        if t in ["boolean", "boolean.", "bool"]: return "bool()"
        if t == "double": return "float()"
        if t in ["integer", "bitfield"]: return "int()"
        if t in ["string", "str"]: return "str()"
        if t in ["matrix", "Matrix", "mathutils.Matrix"]:
            if self.current_module != "mathutils": return "mathutils.Matrix()"
            else: return "Matrix()"
        if t in ["vector", "Vector", "mathutils.Vector"]:
            if self.current_module != "mathutils": return "mathutils.Vector()"
            else: return "Vector()"
        if t == "list" and not noerror: return "list()"
        if t == "dict" and not noerror: return "dict()"
        if t == "tuple" and not noerror: return "tuple()"
        if t == "Quaternion":
            if self.current_module != "mathutils": return "mathutils.Quaternion()"
            else: return "Quaternion()"

        #Special cases
        if t == "list of functions and/or methods": return "list()"
        if t == "3d vector.": return "mathutils.Vector()"
        if t == "3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))": return "(float, (0,0,0), (0,0,0))"
        if t.startswith("\n3-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz))"):
            return "(KX_GameObject, (0,0,0), (0,0,0), KX_PolyProxy, (0,0))"
        if t == "list [x, y]": return "[0,0]"
        if t in ["(integer, integer)", "(int,int)", "(int, int)"]: return "(0,0)"
        if t == "list [str]": return "[str()]"
        if t == "list [r, g, b]": return "[0,0,0]"
        if t == "list[x, y, z]": return "[0,0,0]"
        if t == "(Vector, float) pair": return "(Vector(), float())"
        if t == "Matrix4x4 (read only)": return "mathutils.Matrix()"
        if t == "tuple of two ints": return "(0,0)"
        if t == "sequence of two ints": return "[0,0]"
        if t == "sequence of two floats": return "[0.0,0.0]"
        if t == "sequence of three ints": return "[0,0,0]"
        if t == "sequence of four sequences of two ints": return "[[0,0],[0,0],[0,0],[0,0]]"
        if t == "sequence of four sequences of five ints": return "[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]"
        if t == "Buffer\n": return "bgl.Buffer()"
        if t == "sequence supporting index/string lookups and iteration.": return "dict()"

        #Addressing of containers
        for st in ["list of ", "CListValue of "]:
            if t.startswith(st):
                h=self.getType(t[len(st):], True)
                if h != "None":
                    if h.endswith("()"): h=h[:-2]
                    if h=="self": h=self.current_class
                    if self.current_module == "bge.types":
                        return "CListValue(" + h + ")"
                    else: return "bge.types.CListValue(" + h + ")"

        if t.startswith("Vector"):
            if self.current_module != "mathutils": return "mathutils.Vector()"
            else: return "Vector()"

        #Last chances to get it right
        for ch in ['\n', ' ', ',']:
            if ch in t:
                for x in t.split(ch):
                    h=self.getType(x, True)
                    if h!="None": return h

        for x in ["non-negative", "None"]:
            if x in t: return "None"

        if not noerror:
            if type(dl) != str and search_refs:
                links = dl.dd.table.tbody.tr.td.find_all("a")
                url = File.done_urls[-1]
                base_url = url[:url.rfind("/")+1]
                for l in links:
                    link = l["href"]
                    if not "CListValue" in link:
                        link = base_url + link[:link.rfind("#")]
                        File(link, recursive=True)
                        return self.getType(dl, noerror)

            print("Unknown type:", t)

        return "None"

    def getReturnType(self, o):
        if o.dd.table == None: return "None"
        for tr in o.dd.table.tbody.find_all("tr"):
            if tr.th.string=="Return type:":
                return self.getType(tr.td.get_text())
        return "None"

    def makePage(self, url, tab='', recursive=False, prefix=""):
        if url in File.done_urls: return
        else: File.done_urls.append(url)

        if not url.endswith(".html"):
            print("Skipped:", url)
            return

        print("Building page: ", url)

        r = requests.get(url).text
        soup = BeautifulSoup(r, "html.parser")

        body = soup.body.find("h1").parent
        if body.p.get_text().startswith("base class"):
            link = body.p.a["href"]
            link = url[:url.rfind("/")+1] + link[:link.rfind("#")]
            if recursive==True:
                File(link, recursive)

        #Get current module, autodetect class vs module using case sensitive.
        self.current_module = prefix + url[url.rfind('/')+1:url.rfind(".html")]
        i = self.current_module.rfind(".")
        if i != -1:
            if not self.current_module.split(".")[-1][0:1].islower():
                self.current_module = self.current_module[:i]
                dest = url[url.rfind('/')+1:url.rfind(".html")]
            else: dest = self.current_module + "."
        else: dest = self.current_module + "."

        #Identify Class or Module level data
        code = ""
        for dl in soup.find_all("dl"):
            dtype=dl.get("class")
            if dtype[0]=="class":
                code += '\n' + self.makePythonClass(dl) + '\n'

            if dtype[0]=="data":
                name = dl.dt["id"]
                #Make sure it's at module level
                if len(name.split('.')) == len(self.current_module.split('.'))+1:
                    value = "None"
                    for th in dl.find_all("th"):
                        if th.get_text() == "Value:":
                            value = th.parent.td.get_text()
                    code += name.split('.')[-1] + " = " + value + "\n"

            if dtype[0]=="function":
                name = dl.dt["id"]
                if len(name.split('.')) == len(self.current_module.split('.'))+1:
                    code += self.writeFunction(dl, False, '')


        #Write the file
        odest =  dataToPath(dest)
        dest = build_path + os.sep + odest

        if os.sep in dest:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
        if dest in File.done_files:
            with open(dest, "a+", encoding="utf-8") as out: out.write(code)
        else:
            try: code = headers[odest] + code
            except KeyError: pass

            try:
                for x in erase[odest]: code=code.replace(x, "")
            except KeyError: pass

            with open(dest, "w", encoding="utf-8") as out: out.write(code)
            File.done_files.append(dest)

    def makePythonClassTitle(self, dt):
        cn = dt["id"]
        self.current_class = cn[cn.rfind(".")+1:]
        File.registred_class[self.current_class] = self.current_module
        code = "class " + self.current_class + '('
        for x in dt.find_all("em"):
            if x.get("class"): continue
            if not x.string[0].isupper(): continue
            if x.string in ["A", "B", "C", "D", "E", "F"]: continue
            code += x.string + ','
        if code.endswith(","): return code[:-1] + '):\n'
        else: return code [:-1]+ ":\n"

    def makePythonClass(self, dl, tab=''):
        tab+='\t'
        docstring = '"""' + dl.dd.p.get_text() + '"""'
        code = self.makePythonClassTitle(dl.dt) + tab + docstring + '\n\n'

        temp_code = tab + "def __init__(self, "

        for x in dl.dt.find_all("em"):
            if x.get("class"): continue
            if not x.string[0].islower() and not x.string in ["A", "B", "C", "D", "E", "F"]: continue
            if not "=" in x.string: temp_code += x.string+"=None, "
            else:
                if x.string.split("=")[1][0]== '<':
                    temp_code += x.string.split("=")[0] + "=None, "
                else:
                    temp_code += x.string + ', '

        temp_code = temp_code[:-2] + "):\n"
        tab+='\t'

        for o in dl.dd.find_all("dl"):
            if o["class"][0]=="data":
                temp_code += tab + "self." + o.dt.code.string + " = int()\n"
            if o["class"][0]=="attribute":
                temp_code += tab + "self." + o.dt.code.string + " = " + self.getType(o) + '\n'

        if not temp_code.endswith(":\n"): code += temp_code

        tab=tab[:-1]
        for o in dl.dd.find_all("dl"):
            if o["class"][0]=="method":
                code += self.writeFunction(o, True, tab)

        if self.current_class in fixes:
            for el in fixes[self.current_class]:
                x, y = el
                code = code.replace(x, y)

        return code

    def writeFunction(self, o, is_method=True, tab='\t'):
        if is_method:
            code = '\n' + tab + "def " + o.dt.code.string + "(self, "
        else:
            code = '\n' + tab + "def " + o.dt.find_all("code")[-1].string + "("

        for arg in o.dt.find_all("em"):
            m = arg.string.split("=")
            if len(m)>1 and any([m[1].startswith(x) for x in ["KX_", "IMB_"]]):
                 code += m[0] + '=None, '
            else: code += arg.string + ', '
        if code.endswith("("): code += "):"
        else: code = code[:-2]+"):"

        try:
            docstring = '"""' + o.dd.p.get_text() + '"""'
            code += '\n' + tab + '\t' + docstring + '\n'
        except Exception: code += " pass\n"

        rt = self.getReturnType(o)
        if rt != "None":
            if code.endswith(" pass\n"): code=code[:-len(" pass\n")]+"\n"
            tab+='\t'
            if "bge." in rt: code += tab + "import bge\n"
            code += tab + "return " + rt + '\n'
            tab=tab[:-1]

        if "deprecated" in code or "Deprecated" in code: return ""
        return code

def build(url): File(url, recursive=True, prefix="core." if "api/" in url else "")
def build_bge(url):
    build(url + "mathutils.html")
    build(url + "bge.types.KX_MeshProxy.html")
    build(url + "bge.types.KX_CharacterWrapper.html")
    build(url + "bge.types.KX_VehicleWrapper.html")
    build(url + "bge.types.SCA_PythonController.html")
    build(url + "bge.types.KX_Scene.html")
    build(url + "bge.logic.html")
    build(url + "bge.texture.html")
    build(url + "bge.events.html")
    build(url + "bge.app.html")
    build(url + "bge.constraints.html")

    init="from . import logic, types, texture, events, app, constraints"
    init_path = build_path + os.sep + "bge" + os.sep + "__init__.py"
    with open(init_path, "w", encoding="utf-8") as out: out.write(init)

def build_core(url):
    build(url + "api/media.html")
    build(url + "api/event.html")
    build(url + "api/sequencer.html")
    build(url + "api/utils.html")

    init="from . import media, event, utils, sequencer\nmedia.music=media.AudioFile()"
    init_path = build_path + os.sep + "core" + os.sep + "__init__.py"
    with open(init_path, "w", encoding="utf-8") as out: out.write(init)


def test():
    test_bge()
    test_core()

def test_bge():
    import traceback
    sys.path.append(build_path)

    try:
        import mathutils, bge
        v=mathutils.Vector()
        m=mathutils.Matrix()
        scn = bge.logic.getCurrentScene()
        o = scn.objects["some"]
        a=o.isPlayingAction()
        b=o.parent.addDebugProperty("LOL")
        o.endObject()

        print("Test BGE: OK")
    except Exception: traceback.print_exc()

def test_core():
    import traceback
    sys.path.append(build_path)

    try:
        import core
        core.media.music.filepath = ""

        print("Test CORE: OK")
    except Exception: traceback.print_exc()


build_path = os.path.normpath(build_path)

import sys
if len(sys.argv) == 1:
    build_bge(API_URL)
    build_core("http://coredoc.royalwebhosting.net/")
    test()
    print("Done.")

if len(sys.argv) == 2:
    if sys.argv[1] == "-test": test()
