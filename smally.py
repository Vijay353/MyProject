fn=[]
r3=[]
lin_num=0
count_l=0
count_if=0

scope={}		
def execute(x,y): #Function for evaluating values of  elements of dictionary
	r1=""
	r1=x.strip()
	r=[]
	k=""
	j=1
	sol=0
	for i in range(len(r1)):
		if r1[i]==" ":
			continue
		elif r1[i] in "+-*%/()":
			r.append(k)
			r.append(r1[i])
			k=""
			r3.append(r1[i])
		else:
			k+=r1[i]
			
	if "()" not in r1:
		r.append(k)
	for i in range(len(r)):
		if r[i] in d4:
			r[i]=d4[r[i]]
	ss="".join(r)
	x1=ss.count('(')
	x2=ss.count(')')
	if x1>x2:
		print("REJECTED!!")
		print("Line %d\nError : missing ')' in the statement!!"%lin_num)
		quit()
	elif x1<x2:
		print("REJECTED!!")
		print("Line %d\nError : missing '(' in the statement!!"%lin_num)
		quit()
	try:
		sol=eval(ss)
	except:
		print("REJECTED!!")
		print("Line: %d \nError : undefined asignment to idetifier \' Can't evaluate\'\n\'may be wrong operation on string\' OR\t\'may be Zero Div.Error \'" %lin_num)
		quit()
	d4[y]=str(sol)
	for i in r3:
		d5[i]="<op>"
		
		
def Print(ch1,s3,lin_num):

	i=0
	if len(ch1)==0:
		print(s3)
		return 0
	if ch1[i:i+2]=="+\"" or s3=="":
		if ch1[i]=="+":
			i+=1
		
		if ch1[i]=="\"":
		
			if "\"" not in ch1[i+1:]:
				print("REJECTED!!")
				print("Line:  \n Error:it seems \'\"\' missing in the line!!")
				quit()
			i+=1
			while ch1[i]!="\"":
				s3+=ch1[i]
				i+=1
		
			p=Print(ch1[i+1:],s3,lin_num)
			
	elif i+1==len(ch1):
		print("REJECTED!!")
		print("Line %d\nError : undefined EOF at the end of statement"%lin_num)
		print("\t\'"+ch1+'\'')
		quit()
	elif ch1[i]=="+" and s3!="":
		s4=""
		i=1
		j=len(ch1)
		while ch1[i]:
			s4+=ch1[i]
			i+=1
			if i==j:
				break;
			if ch1[i]=="+":
				break;
			
		if s4 in d4:
			
			s3+=d4[s4]
			p=Print(ch1[i:],s3,lin_num)
		else:
			print("REJECTED!!")
			print("Line %d\nError : Typed vaiable not declared!!" %lin_num)
			quit()
		
		
	else:
		print("REJECTED!!")
		print("Line %d \nError : \nInvalid Syntex \nError: '\"' or '+' missing in the statement inside ' out $ '!!"%lin_num)
		print("\'"+ch1+"\'")
		quit()	
	
	
def check_identifier(st,n): #Function for checking identifier in a list
	flag=0
	p=0
	temp=st
	if temp[0].isalpha()==True or temp[0]=='_':
		for j in temp[1:n]:
			if j.isalnum()==True or j=='_':
				continue
			else:
				p=1
		if p==1:
			return 0
	else:
		return 0
	return 1
	
	
def check_for(ch):
	flag=0
	count=1
	if ch.count(';')!=2:
		print("REJECTED!!")
		print("Line : %d\nError : Semicolon is missing in \'while\' statement !!!"%lin_num)
		print("\'"+ch+"\'")
		quit()
	if ch[0]!="(" or ch[len(ch)-1]!=")":
		print("REJECTED!!")
		print("Line : %d\nError : \'(\' or \')\' missing in expression !! "%lin_num)
		print("\'"+ch+"\'")
		quit()
	for i in ch[1:]:
		if i!=';':
			count+=1
		else:
			flag=1
			break
	if flag==0:
		quit()
	lst_tmp=ch[1:count].split("=")
	if lst_tmp[0] not in d4:
		print("REJECTED!!")
		print("Line : %d\nError : Identifier not declared above!!" %lin_num)
		quit()
	execute(lst_tmp[1],lst_tmp[0])
	
	s=""
	flag=0
	count+=1
	count_=count
	space=0
	if ch[count].strip()!=";":
		for i in ch[count_:]:
			if i==" ":
				space+=1
				continue
			elif i!=';':
				count+=1
			else:
				flag=1
				break
		if flag==0:
			print("REJECTED!!")
			print("Line: %d \nError: \';\' missing in the statement "%lin_num)
			quit()
		c=0
	
		for i in ch[count_:count]:
			if i==" ":
				space+=1
				continue
			elif i!="<" and i!= ">" and i!= "!" and i != "=":
				s+=i
				c+=1
			else:
				break
	
		if s not in d4:
			print("REJECTED!!")
			print("Line : %d\nError : Unidentified identifier written !!" %lin_num)
			quit()
		s2=d4[s]
		try:
			eval(s2+ch[count_+c:count+space-1])
		except:
			print("REJECTED!!")
			print("Line : %d\nError: Condition statement fetching into unidentified error !!"%lin_num)
			print("\'"+s+ch[count_+c:count+space-1]+"\'")
			quit()
	if(count==len(ch)-2):
		return
	count+=1
	list_f=ch[count:len(ch)-1].split('=')
	execute(list_f[1],list_f[0])
		
	
d7={}
ii=2
po=1
ff=2.4
def body(ch,fp,lin_num,count_l,count_if):
	ii=1
	flag_if=False
	fn_nm=ch
	while ch:
		ch=fp.readline()
		lin_num+=1
		ch=ch.strip()
		if "=" in ch and "for"not in ch and "$" not in ch and "if(" not in ch :	
			lst=ch.split("=")
			fl=check_identifier(lst[0],len(lst[0]))
			if fl!=1:
				print("REJECTED!!")
				print("Line %d \nError : Invalid identifier name!!" %lin_num)
				quit()
			d5[lst[0]]="<id>"
			scope[lst[0]]=fn_nm
			d5["="]="<op>"
			execute(lst[1],lst[0])
		elif "end"==ch:
			
		#if fp.tell()!=len(data):
		#	print("REJECTED!!")
		#	print("Error \nCannot write sentences after keyword \'end\'!!")
		#	quit()
		#print("\nToken\'s Table :")
		#for j in d5:
		#	print(j+"\t"+d5[j])
		#print("\n\t\"ACCEPTED\"")
			if fp.tell()==len(data):
				print("\nToken\'s Table :\n")
				print('_'*80)
				print("\nName\tValue\tType \tData-Type\t Operations Associated\t Scope_function\n")
				print('_'*80)
				for j in d5:
					print("\n")
					if(d5[j]=="<id>"):
						
						try:
							d6[j]=type(eval(d4[j]))
							if '.' not in d4[j]:
								d7[j]='ADD SUB MUL DIV REM TYPE < > ='
							else:
								d7[j]=dir(ff)
								d7[j]='ADD SUB MUL DIV REM TYPE'
							print(j+"\t"+d4[j]+"\t"+d5[j]+"\t"),
						except:
							d6[j]="<type \'str\'>"
							d7[j]='<,>,='
							ii=1
							print(j+"\t\'"+d4[j]+"\'\t"+d5[j]+"\t"),
							
						print(d6[j]),
						print("\t"),
						print(d7[j]),
						if ii==1:
							print("\t\t\t"),
							ii=2
						print("\t"),
						print(scope[j])
					else:
						print(j+"\t\t"+d5[j])
					
			print('_'*80)
			print("\n\t\"ACCEPTED\"")
				
				
			quit()
		
		elif "out $" in ch:
			ch=ch[5:]
			p=Print(ch.strip(),"",lin_num)
		
		elif("for"==ch[0:3]):
			count_l+=1
			check_for(ch[3:].strip())
			loop_st.append(fp.tell())
			loop_tr.append(ch[8:-1])
			ch=fp.readline()
			lin_num+=1
			ch=ch.strip()
			if len(ch) != 1 :
				print("REJECTED!!")
				print("Line : %d\nError:'for()' should start with '{' !! " %lin_num)
				quit()
			if ch[0]!="{":
				print("REJECTED!!")
				print("Line : %d\nError:'for()' should start with '{' !! " %lin_num)
				quit()
			d5["{"]="<prnth>"
			body(ch[1:].strip(),fp,lin_num,count_l,count_if)
		
		elif("while" in ch):
			ch=ch[5:]
			ch=ch.strip()
			check_while(ch,fp)
			ch=fp.readline()
			lin_num+=1
			ch=ch.strip()
			if len(ch) != 1 :
				print("REJECTED!!")
				print("Line : %d\nError:'while()' should start with '{' !! " %lin_num)
				quit()
			if ch[0]!="{":
				print("REJECTED!!")
				print("Line : %d\nError:'while()' should start with '{' !! " %lin_num)
				quit()
			count_l+=1
			d5["{"]="<prnth>"
			body(ch[1:].strip(),fp,lin_num,count_l,count_if)
		elif("}"==ch):
			d5["}"]="<prnth>"
			#if count_l<=0:
			#	print("REJECTED!!")
			#	print("Line : %d\nError : \'}\' doesn't match any previous \'{\'" %lin_num)
			#	quit()
			#count_l-=1
			if len(loop_tr)==0:
				print("Er")
				return
			else:
				print("Er")
				execute(loop_tr[-1][-1].split('+')[0],loop_tr[-1][0].split('+')[1])
				if(po<3):
					fp.seek(loop_st[0])
					po+=1
					
				
				else:
					loop_tr.pop(-1)
					po=-1
					continue
				
		elif "{" ==ch:
			continue
		elif len(ch.strip())==0:
			ch=" "
			continue
		elif "if" == ch[0:2]:
			count_if+=1
			if check_if(ch[2:].strip()) :
				flag_if=True
				ch=fp.readline()
				lin_num+=1
				ch=ch.strip()
				if len(ch) != 1 :
					print("REJECTED!!")
					print("Line : %d\nError:'if' should start with '{' !! " %lin_num)
					quit()
				#if ch[0]!="{":
				#	print("REJECTED!!")
				#	print("Line : %d\nError:'if' should start with '{' !! " %lin_num)
				#	quit()
				d5["{"]="<prnth>"
				count_l+=1
				body(ch[1:].strip(),fp,lin_num,count_l,count_if)
			else:
				flag_if=False
				while ch!="}":
					ch=fp.readline().strip()
					lin_num+=1
		elif "else if" == ch[0:7]:
			if count_if<1:
				print("REJECTED  !!")
				print("Line : %d\n\'else if \' without previous \'if\' "%lin_num)
				print(ch)
				quit()
			if flag_if==True:
				while(ch!="}"):
					ch=fp.readline().strip()
					lin_num+=1
				
			elif check_if(ch[7:].strip()) :
				flag_if=True
				ch=fp.readline()
				lin_num+=1
				ch=ch.strip()
				if len(ch) != 1 :
					print("REJECTED!!")
					print("Line : %d\nError:'if' should start with '{' !! " %lin_num)
					quit()
				#if ch[0]!="{":
				#	print("REJECTED!!")
				#	print("Line : %d\nError:'if' should start with '{' !! " %lin_num)
				#	quit()
				d5["{"]="<prnth>"
				count_l+=1
				body(ch[1:].strip(),fp,lin_num,count_l,count_if)
			
			
		elif "else"==ch[0:4]:
			if count_if<1:
				print("REJECTED!!")
				print("Line : %d\n\'else\' without previous \'if\' "%lin_num)
			
				quit()
			count_if-=1
			if flag_if==True:
				while(ch!="}"):
					ch=fp.readline().strip()
					lin_num+=1
			else:
				body(ch,fp,lin_num,count_l,count_if);
			
		elif "begin"==ch[0:5]:
			ch=ch[5:]
			ch=ch.strip()
			fn_nm=ch
			p=check_identifier(ch,len(ch))
			if p==0:
				print("REJECTED!!")
				print("Line : %d \nError : Invalid function name!!" %lin_num)
				quit()
			fn.append(ch)
			body(ch,fp,lin_num,count_l,count_if)	
				
		elif "()"==ch[-2:]:
			if ch[:-2] not in fn:
				print("Line : %d\nError : function  \'%s\' doesn\'t exist "%(lin_num,ch[:-2]))
				quit()
		
		else:
			print("REJECTED!!")
			print("Line %d \nError : undefined syntex of sentence written ,Check below sentence!!" %lin_num)
			print(ch)
			quit()	
			
def check_while(ch,fp):
	flag=0
	s=""
	s1=""
	s2=""
	
	if ch[0]!="(" or ch[len(ch)-1]!=")":
		print("REJECTED!!")
		print("Line : %d\nError : \'(\' or \')\' missing in expression !! "%lin_num)
		print("\'"+ch+"\'")
		quit()
	count = 1
	for i in ch[1:]:
		if i==" ":
			continue
		elif i != ")":
			count+=1
		else :
			break
	
	c=0
	for i in ch[1:count]:
		if i==" ":
			continue
		elif i!="<" and i!= ">" and i!= "!" and i != "=":
			s+=i
			c+=1
	
		else:
			break
	for i in ch[1:count]:
			if i==" ":
				continue
			elif i=="<" or i== ">" or i== "!" or i == "=":
				s1+=i
				c+=1
	
	if s not in d4:
		print("REJECTED!!")
		print("Line :  \nError : Identifier is not declared Check this identifier in condition !!")
		print("\'"+s+"\'")
		quit()
	if ch[1+c:len(ch)-1] in d4:
		s3=d4[ch[1+c:len(ch)-1]]
	else:
		s3=ch[1+c:len(ch)-1]
		
	s2=d4[s]
	try:
		eval(s2+s1+s3)
	except:
		print("REJECTED!!")
		print("Line :  \nError: Can't Execute Condition!!\n Check it\n")
		print(s2+s1+s3)
		quit()
		
		
def check_if(ch):
	if(ch[0]!="(" or ch[len(ch)-1]!=")"):
		print("REJECTED!!")
		print("Line : %d\nNo matching of ( or ) in expression "%lin_num);
		quit()
	s=""
	s1=""
	c=1
	s2=""
	for i in ch[1:]:
		if i==" ":
			continue
		elif i!="<" and i!= ">" and i!= "!" and i != "=":
			s+=i
			c+=1
	
		else:
			break
	for i in ch[1:]:
			if i==" ":
				continue
			elif i=="<" or i== ">" or i== "!" or i == "=":
				s1+=i
				c+=1
	
	if s in d4:
		s=d4[s]
	s2=ch[c:len(ch)-1]
	if ch[c:len(ch)-1] in d4:
		s2=d4[ch[c:len(ch)-1]]
	try:
		eval(s+s1+s2)
	except:
		print("REJECTED!!")
		print("Line : %d\nError in expression "%lin_num)
		quit()
	
	return eval(s+s1+s2)
	
fp=open("input.txt","r")
data=fp.read()
fp.seek(0)
templ=[]
lin=0
i=""
dlin=[]
c=fp.readline().strip()
while c!="end":

	if len(c)==0:
		c=fp.readline().strip()
		lin+=1
		continue
	i=c[0]
	lin+=1
	
	if i=="{":
		dlin.append(lin)
		templ.append(i)
	
	elif i=="}":
		
		if (len(templ)==0):
			print("REJECTED!!")
			print("Line: %d\nError:\'}\' doesn\'t have any previous matching "%lin)
			quit()
		dlin.pop()
		templ.pop()

	c=fp.readline().strip()
if(len(dlin)!=0):
	print("REJECTED!!")
	print("Line: %d\nError:\'{\' doesn\'t have any matching " %dlin[0])
	quit()	
	
fp.seek(0)
ch=fp.readline()
lin_num+=1
ch=ch.strip()
d4={}
fl=0
p=0
d5={}
lst1=[]

lst2=[]
count_l=0
if "begin"!=ch[0:5]:
	print("REJECTED!!")
	print("Line %d \nError : Invalid function declaration!!" %lin_num)
	quit()
if "end" not in data:
	print("REJECTED!!")
	print("End of program missing!!\n'end' missing at the end")
	quit()
ch=ch[5:]
ch=ch.strip()
fn_nm=[]
fn_nm=ch
p=check_identifier(ch,len(ch))
if p==0:
	print("REJECTED!!")
	print("Line : %d \nError : Invalid function name!!" %lin_num)
	quit()
fn_name=ch
fn.append(ch)
d6={}
d5[ch]='<fn_name>'
flag_if=False
loop_st=[]
loop_ter=''
loop_tr=[]
while ch:
	
	ch=fp.readline()
	lin_num+=1
	ch=ch.strip()
	if "=" in ch and "for"not in ch and "$" not in ch and "if(" not in ch :	
		lst=ch.split("=")
		fl=check_identifier(lst[0],len(lst[0]))
		if fl!=1:
			print("REJECTED!!")
			print("Line %d \nError : Invalid identifier name!!" %lin_num)
			quit()
		d5[lst[0]]="<id>"
		scope[lst[0]]=fn_nm
		d5["="]="<op>"
		execute(lst[1],lst[0])
	elif "end"==ch:
		#if fp.tell()!=len(data):
		#	print("REJECTED!!")
		#	print("Error \nCannot write sentences after keyword \'end\'!!")
		#	quit()
		#print("\nToken\'s Table :")
		#for j in d5:
		#	print(j+"\t"+d5[j])
		#print("\n\t\"ACCEPTED\"")
		if fp.tell()==len(data):
			print("\nToken\'s Table :\n")
			print('_'*80)
			print("\nName\tValue\tType \tData-Type\t Operations Associated\t  Scope_function\n")
			print('_'*80)
			for j in d5:
				print("\n")
				if(d5[j]=="<id>"):
						
					try:
						d6[j]=type(eval(d4[j]))
						if '.' not in d4[j]:
							d7[j]='ADD SUB MUL DIV REM TYPE'
						else:
							d7[j]=dir(ff)
							d7[j]='ADD SUB MUL DIV REM TYPE'
						print(j+"\t"+d4[j]+"\t"+d5[j]+"\t"),
					except:
						d6[j]="<type \'str\'>"
						d7[j]='<,>,='
						ii=1
						print(j+"\t\'"+d4[j]+"\'\t"+d5[j]+"\t"),
							
					print(d6[j]),
					print("\t"),
					print(d7[j]),
					if ii==1:
						print("\t\t\t"),
						ii=2
					print("\t"),
					print(scope[j])
				else:
					print(j+"\t\t"+d5[j])
					
			print('_'*80)
			print("\n\t\"ACCEPTED\"")
				
			
			quit()
			
		
	elif "begin"==ch[0:5]:
		ch=ch[5:]
		ch=ch.strip()
		fn_nm=ch
		p=check_identifier(ch,len(ch))
		if p==0:
			print("REJECTED!!")
			print("Line : %d \nError : Invalid function name!!" %lin_num)
			quit()
		fn_name=ch
		fn.append(ch)
		d5[ch]='<fn_name>'
		body(ch,fp,lin_num,count_l,count_if)
		
	elif "out $" in ch:
		ch=ch[5:]
		p=Print(ch.strip(),"",lin_num)
		
	elif("for"==ch[0:3]):
		count_l+=1
		check_for(ch[3:].strip())
		loop_ter=ch[8:-1]
		loop_tr.append(loop_ter.split(';'))
		print(loop_tr)
		loop_st.append(fp.tell())
		ch=fp.readline()
		lin_num+=1
		ch=ch.strip()
		if len(ch) != 1 :
			print("REJECTED!!")
			print("Line : %d\nError:'for()' should start with '{' !! " %lin_num)
			quit()
		if ch[0]!="{":
			print("REJECTED!!")
			print("Line : %d\nError:'for()' should start with '{' !! " %lin_num)
			quit()
		d5["{"]="<prnth>"
		body(ch[1:].strip(),fp,lin_num,count_l,count_if)
		
	elif("while" in ch):
		ch=ch[5:]
		ch=ch.strip()
		check_while(ch,fp)
		ch=fp.readline()
		lin_num+=1
		ch=ch.strip()
		if len(ch) != 1 :
			print("REJECTED!!")
			print("Line : %d\nError:'while()' should start with '{' !! " %lin_num)
			quit()
		if ch[0]!="{":
			print("REJECTED!!")
			print("Line : %d\nError:'while()' should start with '{' !! " %lin_num)
			quit()
		count_l+=1
		d5["{"]="<prnth>"
		body(ch[1:].strip(),fp,lin_num,count_l,count_if)
	elif("}"==ch):
		d5["}"]="<prnth>"
		#if count_l<=0:
		#	print("REJECTED!!")
		#	print("Line : %d\nError : \'}\' doesn't match any previous \'{\'" %lin_num)
		#	quit()
		count_l-=1
		d5["}"]="<prnth>"
			#if count_l<=0:
			#	print("REJECTED!!")
			#	print("Line : %d\nError : \'}\' doesn't match any previous \'{\'" %lin_num)
			#	quit()
			#count_l-=1
		if len(loop_tr)==0:
			print("Er")
			continue
		else:
			print("Er4")
			lst1=loop_tr[-1][-1].split('=')
			execute(lst1[1],lst[0])
			if(po<3):
				fp.seek(loop_st[-1])
				po+=1
				
			else:
				loop_tr.pop(-1)
				po=-3
				continue
	#	continue
	elif "{" ==ch:
		continue
	elif len(ch.strip())==0:
		ch=" "
		continue
	elif "if" == ch[0:2]:
		count_if+=1
	#	print(count_if)
		if check_if(ch[2:].strip()) :
			flag_if=True
			ch=fp.readline()
			lin_num+=1
			ch=ch.strip()
			if len(ch) != 1 :
				print("REJECTED!!")
				print("Line : %d\nError:'if' should start with '{' !! " %lin_num)
				quit()
			#if ch[0]!="{":
			#	print("REJECTED!!")
			#	print("Line : %d\nError:'if' should start with '{' !! " %lin_num)
			#	quit()
			d5["{"]="<prnth>"
			count_l+=1
			body(ch[1:].strip(),fp,lin_num,count_l,count_if)
		else:
			flag_if=False
			while ch!="}":
				ch=fp.readline().strip()
				lin_num+=1
	elif "else if" == ch[0:7]:
		
		if count_if<1:
			print("REJECTED !!")
			print("Line : %d\n\'else if\' without previous \'if\' "%lin_num)
			print(ch)
			quit()
		if flag_if==True:
			while(ch!="}"):
				ch=fp.readline().strip()
				lin_num+=1
			continue
		
		elif check_if(ch[7:].strip()) :
			flag_if=True
			ch=fp.readline()
			
			lin_num+=1
			ch=ch.strip()
			if len(ch) != 1 :
				print("REJECTED!!")
				print("Line : %d\nError:'if' should start with '{' !! " %lin_num)
				quit()
			#if ch[0]!="{":
			#	print("REJECTED!!")
			#	print("Line : %d\nError:'if' should start with '{' !! " %lin_num)
			#	quit()
			d5["{"]="<prnth>"
			count_l+=1
			body(ch[1:].strip(),fp,lin_num,count_l,count_if)
		else :
		 	while(ch!="{"):
					ch=fp.readline().strip()
					lin_num+=1
			
	elif "else"==ch[0:]:
		if count_if<0:
			print("REJECTED!!")
			print("Line : %d\n\'else\' without previous \'if\' "%lin_num)
			print(ch)
			quit()
		count_if-=1
		if flag_if==True:
			while(ch!="}"):
				ch=fp.readline().strip()
				lin_num+=1
		else:
			body(ch,fp,lin_num,count_l,count_if);
	
	elif "()"==ch[-2:]:
		if ch[:-2] not in fn:
			print("Line : %d\nError : function  \'%s\' doesn\'t exist "%(lin_num,ch[:-2]))
			quit()
	else:
		print("REJECTED!!")
		print("Line %d \nError : undefined syntex of sentence written ,Check below sentence!!" %lin_num)
		print(ch)
		print(fn)
		quit()		
fp.close()
