some_list  = [1,2,3]
def func(some_list):
    some_list.append(22)
    def func2():
        print(some_list)
    func2()
func(some_list)
#print(some_list)
