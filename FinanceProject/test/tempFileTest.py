from tempfile import TemporaryFile,NamedTemporaryFile
#用文件描述符来操作临时文件
f = TemporaryFile()
f.write(b'abcdef')
f.seek(0)
f.read(100)
ntf = NamedTemporaryFile()
#返回文件路径
print(ntf.name)
f.close()