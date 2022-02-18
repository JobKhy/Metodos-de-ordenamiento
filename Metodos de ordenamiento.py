
repm="si"
while repm=="si":
    try:
        op=int(input("Teclea '1' para utilizar el metodo de ordenamiento Burbuja ó teclea '2' para utilizar el metodo de ordenamiento QuickSort. "))

        if op == 1:
            rep="si"
            while rep=="si":
                try:
                    cant= int(input("Ingresa la cantidad de numeros que deseas colocar en la lista a ordenar por metodo Burbuja: "))
                    nums = []
                    x = 0

                    while x < cant :

                        numero = int(input("Introduce el numero: "))
                        nums.append(numero)
                        x+=1

                    largo = len(nums)

                    for y in range(largo):

                        for i in range(largo - 1):
                        
                            if nums[i] > nums[ i + 1]:

                                aux = nums[i]
                                nums[i] = nums[i + 1]
                                nums[i + 1] = aux

                    print("Lista de numeros ordenados por metodo de burbuja: ", nums)
                except:
                    print("Ingresa datos correctos")

                rep=input("Deseas repetir la opción? ")

        elif op == 2:
            rep="si"
            while rep=="si":
                try:
                    cant= int(input("Ingresa la cantidad de numeros que deseas colocar en la lista a ordenar por metodo QuickSort: "))
                    nums = []
                    x = 0

                    while x < cant :

                        numero = int(input("Introduce el numero: "))
                        nums.append(numero)
                        x+=1

                    def div(nums):

                        menores = []
                        centro = []
                        mayonesa = []

                        if len(nums) > 1:

                            pivote = nums[0]

                            for i in nums:

                                if i < pivote:
                                    menores.append(i)

                                elif i == pivote:
                                    centro.append(i)

                                elif i > pivote:
                                    mayonesa.append(i)

                            return div(menores)+centro+div(mayonesa)
                            
                        else:
                                return nums

                    print("Lista de numeros ordenados por metodo QickSort: ", div(nums))

                except:
                    print("Ingresa datos correctos")

                rep=input("Deseas repetir la opción? ")   


        elif op!=1 or op!=2:
            print("ingresa una opcion de ordenamiento valida")


    except:
        print("Ingresa datos correctos")

    repm=input("Deseas repetir el los metodos de ordenamiento? ")
