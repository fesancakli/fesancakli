class Stack():
    def __init__(self):
        self.data = []

    def pop(self):
        return self.data.pop() if self.data else None

    def push(self, value):
        self.data.append(value)
    def isempty(self):
        if len(self.data)==0:
            return 1
        return 0
stack1=Stack()
stack2=Stack()
stack3=Stack()
stack1.push("1")
stack1.push("2")
stack1.push("3")
dictM={"1":stack1,
       "2":stack2,
       "3":stack3}
def TakeInput():
    while True:
        a = input("Hangı kovadan aktarmak istiyorsun : ")
        if a not in dictM or dictM[a].isempty():
            print("Geçersiz giriş veya boş kova seçildi. Lütfen geçerli bir kova seçin.")
            continue
        b = input("Hangı kovaya aktarmak istiyorsun : ")
        if b not in dictM or a == b:
            print("Geçersiz giriş veya aynı kova seçildi. Lütfen geçerli bir kova seçin.")
            continue
        return a, b
def game():
    while iswin():
        Print_basket()
        a,b=TakeInput()
        temp=dictM[a].pop()
        dictM[b].push(temp)
    print("Kazandın !!!")
def iswin():
    if len(stack3.data)==3 and stack3.data==sorted(stack3.data):
        return 0
    return 1
def Print_basket():
    for i in range(3):
        stack1_val = stack1.data[2 - i] if len(stack1.data) > 2 - i else " "
        stack2_val = stack2.data[2 - i] if len(stack2.data) > 2 - i else " "
        stack3_val = stack3.data[2 - i] if len(stack3.data) > 2 - i else " "
        print("| {} |  | {} |  | {} |".format(stack1_val, stack2_val, stack3_val))
game()
def print_items(self):
    for i in range(num_disks):
      val1 = stacks[i].value if stacks[i].value != None else " "
      val2 = stacks[i].value if stacks[i].value != None else " "
      val3 = stacks[i].value if stacks[i].value != None else " "
      print("| {} |  | {} |  | {} |")
