from getNumericData import getNumericData
from graphics import graphics
from Map import showMaps

URL = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217443&type=222'
data = getNumericData(URL)

graphics(data)
showMaps(data)
