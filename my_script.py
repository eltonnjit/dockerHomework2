#Sample taken from pyStrich Github repository
#https://github.com/mmulqueen/pyStrich
from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamartix_test.png')
print(encoder.get_ascii())
