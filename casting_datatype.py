# dgn Casting dapat merubah index data type pertama ke data type yg lain
#type data = int,float,str,bool

# tipe int ke type data float,str,bool
data_int: int
data_int = 9 #buat juga contoh 0 ,-1,-1
print("data = ", data_int,"type =",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)
print("data = ", data_float,"type =",type(data_float))
print("data = ", data_str,"type =",type(data_str))
print("data = ", data_bool,"type =",type(data_bool))

data_int = 0
print("data = ", data_int,"type =",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)
print("data = ", data_float,"type =",type(data_float))
print("data = ", data_str,"type =",type(data_str))
print("data = ", data_bool,"type =",type(data_bool))


# tipe float ke type data int,str dan bool
data_float = 9 
print("data = ", data_float,"type =",type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool  = bool(data_float)
print("data = ", data_int,"type =",type(data_int))
print("data = ", data_str,"type =",type(data_str))
print("data = ", data_bool,"type =",type(data_bool))


# tipe str ke data type int,float dan bool
data_int = 9 
print("data = ", data_str,"type =",type(data_str))

data_float = float(data_str)
data_int   = int(data_str)
data_bool  = bool(data_str)
print("data = ", data_float,"type =",type(data_float))
print("data = ", data_int,"type =",type(data_int))
print("data = ", data_bool,"type =",type(data_bool))


# tipe bool ke data type int,str dan float
data_int = 9 
print("data = ", data_bool,"type =",type(data_bool))

data_float = float(data_bool)
data_str   = str(data_bool)
data_int   = int(data_bool)
print("data = ", data_float,"type =",type(data_float))
print("data = ", data_str,"type =",type(data_str))
print("data = ", data_int,"type =",type(data_int))