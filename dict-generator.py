#coding=utf-8

from string import digits,letters
import os,sys,time,argparse

if os.name=='nt':
  filename=os.path.realpath(sys.path[0])+'\\'+str(int(time.time()))+'-gen_dicts.txt'
else:
  filename=os.path.realpath(sys.path[0])+'/'+str(int(time.time()))+'-gen_dicts.txt'
  
def calc_size(lists):
  n=0
  for i in lists:
    j=len(i)+2
    n+=j
	
  if n<1024:
    r='{0} bytes'.format(n)
  elif n<1024**2:
    r='{0:.2f} Kb'.format(n/1024.0)
  elif n<1024**3:
    r='{0:.2f} Mb'.format(n/1024.0**2)
  elif n<1024**4:
    r='{0:.2f} Gb'.format(n/1024.0**3)
  elif n<1024**5:
    r='{0:.2f} Tb'.format(n/1024.0**4)

  return r

#生成器函数测试
def t():
  for i in matas:
    for j in matas:
      yield i+j

#生成器函数
def t1(n,matas):
  a, b , c = 0,[],matas
  while a<n:
    yield c
    b, c = c, [i+j for i in matas for j in c]
    a+=1

#tmplist=[i for i in t1(n)]  #len(tmplist)=n

#tar_list=tmplist[n-1]

if __name__=='__main__':
  parser=argparse.ArgumentParser(description='diction-generator, python ver2.7.9, author: shadow008') 
  parser.add_argument('-c','--choose',help='choose meta elements, exam: d for digits [0-9], l for letters [a-zA-Z], a for [0-9a-zA-Z](default)',dest='choose')
  parser.add_argument('-i','--metas',help='define meta elements, exam: 1,2,3,a,b,c,d',dest='metas')
  parser.add_argument('-n','--counts',help='specify number of meta elements, exam: 3',dest='counts',type=int)
  parser.add_argument('-o','--output',help='specify filename to save results, exam: result.txt',dest='output',default='dict.txt')
  result=parser.parse_args()
  choose=result.choose
  meta=result.metas
  counts=result.counts
  filename=result.output if result.output else filename

  if counts==None:
    parser.print_help()
    exit()  
  n=counts

  if choose and meta:
    parser.print_help()
    exit()

  if not (choose or meta):
    parser.print_help()
    exit()

  if choose:	
    if choose in ['','a','A']:
	  matas=list(digits+letters)
    elif choose in ['d','D']:
      matas=list(digits)
    elif choose in ['l','L']:
      matas=list(letters)	

  if meta:
    matas=[i for i in meta.split(',') if i] 
	
  tmplist=[i for i in t1(n,matas)]
	
  tar_list=tmplist[n-1]

  tatal=len(tar_list)
  
  filesize=calc_size(tar_list)

  print('Generates {0} passwords, filesize(if saved):{1}'.format(tatal,filesize))
  
  ans=raw_input('Do you want to print the results? Y(yes) or N(no, default):')
  
  if ans in ['y','Y']:
    for i in tar_list:print(i)

  ans=raw_input('Do you want to save the results? Y(yes) or N(no, default):')
	
  if ans in ['y','Y']:
    with open(filename,'w') as f:
      for i in tar_list:	
        f.write('{0}\n'.format(i))
    print('results saved in file:{0}'.format(filename))
    
