

molde = [
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1],
    [0,0,0,1]
]

def get_column(vector, position):
    result = []
    for fila in vector:
        result.append(fila[position])
    return result

def validar(fila, column):
    result = 0
    for index in range(len(fila)):
        if (fila[index] ==1 and column[index] ==1):
            result = 1
    return result

def convertir_transitiva( vector):
    # print(vector)
    result =[]
    for fila in vector:
    #   print(fila)
      if len(fila) == 0:
          continue
      new_result= []
      for index in range(len(fila)):
        #  print(index)
         column= get_column(vector, index)
        #  print(column)
        #  print(fila)
         new_result.append(validar(fila, column))
      result.append(new_result)

    return result

def imprimir(result):
    for index in range(len(result)):
        x = ' '.join([ str(elem) for elem in result[index]])
        print(x)


result_final = convertir_transitiva(molde)
imprimir(result_final)