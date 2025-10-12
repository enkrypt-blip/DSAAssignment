import numpy as np

class DSAStack():
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.queue = np.empty(capacity, dtype=object)
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.capacity
    
    def push(self, value):
        if self.isFull():
            raise IndexError("Stack is full!")
        else:
            self.queue[self.count] = value
            self.count += 1
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty!")
        else:
            self.count -= 1
            topval = self.queue[self.count]
            self.queue[self.count] == None
            return topval
    
    def top(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            topval = self.queue[self.count - 1]
            return topval
    
    def output(self):
        if self.isEmpty():
            return []
        result = ''
        for i in range(self.count):
            result += str(self.queue[i]) + " "
        form = f"[{result.strip()}]"
        return form

        
class DSAQueue:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.queue = np.empty(capacity, dtype=object)
        self.front = 0
        self.back = 0
        self.count = 0

    def getCount(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.capacity
    
    def enqueue(self, value):
        if self.isFull():
            raise Exception('Queue is full')
        else:
            self.queue[self.back] = value
            self.back += 1
            self.count += 1
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            frontVal = self.queue[self.front]
            self.queue[self.front] = None
            self.front = self.front + 1
            self.count -= 1
            return frontVal
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            frontVal = self.queue[self.front]
            return frontVal
        
    def output(self):
        if self.isEmpty():
            return '[]'
        result = ''
        for n in range(self.count):
            result += str(self.queue[n]) + ' '
        form = f"[{result.strip()}]"
        return form
    
class DSACircular(DSAQueue):
    def __init__(self, capacity=100):
        super().__init__(capacity)
        self.front = 0
        self.back = 0
        self.count = 0

    def enqueue(self, value):
        if self.isFull():
            raise Exception('Queue is full')
        else:
            frontVal = self.queue[self.front]
            self.queue[self.back] = value
            self.back = (self.back + 1) % self.capacity
            self.count += 1
            return frontVal
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            frontVal = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.count -= 1
            return frontVal
        
class ShuffleQueue(DSAQueue):
    def __init__(self, capacity=100):
        super().__init__(capacity)

    def shuffle(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            shuffled = DSAQueue(self.capacity)
            while not self.isEmpty():
                item = self.dequeue()
                shuffled.enqueue(item)
            return shuffled
    
    def order(opp):
        # Declares order by ranking them from 0 to 2
        if opp == '+' or opp == '-':
            return 1
        elif opp == '*' or opp == '/':
            return 2
        else:
            return 0
        
    def execute(op, op1, op2):
        # Function to perform operator actions
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            if op2 == 0:
                # Prevents division by zero
                raise Exception("Division by zero")
            else:
                return op1/op2
        else:
            raise Exception("Unkown opperator")

        
    def infixTopostfix(equation):
        # Creates a postfix queue and operator stack
        postfix = DSAQueue()
        opStack = DSAStack()

        # Automatically puts spaces around brackets to prevent misinputs
        equation = equation.replace("(", " ( ").replace(")", " ) ")

        # Splits the equation into 'chips'
        chips = equation.split()

        # Goes thru each chip and converts to float to check if its a operand
        for chip in chips:
            try:
                num = float(chip)
                postfix.enqueue(num)
            except ValueError:
                # If chip is not a number then must be an operator
                if chip == "(" :
                    opStack.push(chip)
                elif chip == ')':
                    # Pop operators until ')' is found
                    while (not opStack.isEmpty()) and opStack.top() != '(':
                        postfix.enqueue(opStack.pop())
                    if (not opStack.isEmpty()) and opStack.top() == '(':
                        opStack.pop() # Discards the '('
                    else:
                        raise Exception("Incorrect brackets")
                else:
                    # The chip is one of the following operators ( -, +, *, /)
                    # Arranges and pops in order of importance
                    while (not opStack.isEmpty() and opStack.top() != '(' and
                           ShuffleQueue.order(opStack.top()) >= ShuffleQueue.order(chip)):
                        postfix.enqueue(opStack.pop())
                    opStack.push(chip)
        # Pop any more opperators into the postfix queue
        while not opStack.isEmpty():
            topOp = opStack.pop()
            if topOp == '(' or topOp == ')':
                raise Exception("Incorrect Brackets")
            postfix.enqueue(topOp)
        return postfix
    
    def evaluatepostfix(postfix):
        #Create an opperand stack to evaluate postfix
        opStack = DSAStack()

        while not postfix.isEmpty():
            item = postfix.dequeue()
            # If the item is a float, it is a operand
            if isinstance(item, float):
                opStack.push(item)
            else:
                # If the operator is an opperand, then pop two operands
                if opStack.get_count() < 2:
                    raise Exception("Not enough operands")
                op2 = opStack.pop()
                op1 = opStack.pop()
                result = ShuffleQueue.execute(item, op1, op2)
                opStack.push(result)
        
        if opStack.get_count() != 1:
            raise Exception("The expresion is invalid")
        return opStack.pop()
    
if __name__ == '__main__':
    while True:
        print("---Menu---")
        print("1. Stack")
        print('2. Queue')
        print('3. Circular Queue')
        print('4. Shuffled Queue')
        print('5. Equation Solver')
        print('6. Quit')
        choice = input("Enter your choices: ")

        if choice == '1':
            capacity = int(input('Enter the size of the stack: '))
            stack = DSAStack(capacity)
            while True:
                print('---Stack Commands---')
                print('1. Push')
                print('2. Pop')
                print('3. Peek')
                print('4. Display')
                print('5. Back to menu')
                queue_c = input('Choose an operation: ')
                try:
                    if queue_c == '1':
                        val = input('Value to push: ')
                        stack.push(val)
                        print(f'Pushed: {val}')
                    elif queue_c == '2':
                        val = stack.pop()
                        print(f'Popped: {val}')
                    elif queue_c == '3':
                        print(f'Top value: {stack.top()}')
                    elif queue_c == '4':
                        print(stack.output())
                    elif queue_c == '5':
                        break
                    else:
                        print("Invalid choice")
                except Exception as err:
                    print("Error:", err)
            
        elif choice == '2':
            capacity = int(input('Enter the size of the queue: '))
            queue = ShuffleQueue(capacity)
            while True:
                print('---Queue (shuffling) Commands---')
                print('1. Enqueue')
                print('2. Dequeue')
                print('3. Peek')
                print('4. Display')
                print('5. Back to menu')
                queue_c = input('Choose an operation: ')
                try:
                    if queue_c == '1':
                        val = input('Value to enqueue: ')
                        queue.enqueue(val)
                        print(f'Enqueued: {val}')
                    elif queue_c == '2':
                        val = queue.dequeue()
                        print(f'Dequeued: {val}')
                    elif queue_c == '3':
                        print(f'Top value: {queue.peek()}')
                    elif queue_c == '4':
                        print(queue.output())
                    elif queue_c == '5':
                        break
                    else:
                        print("Invalid choice")
                except Exception as err:
                    print("Error:", err)

        elif choice == '3':
            capacity = int(input('Enter the size of the circular queue: '))
            queue = DSACircular(capacity)
            while True:
                print('---Circular Queue Commands---')
                print('1. Enqueue')
                print('2. Dequeue')
                print('3. Peek')
                print('4. Display')
                print('5. Back to menu')
                queue_c = input('Choose an operation: ')
                try:
                    if queue_c == '1':
                        val = input('Value to enqueue: ')
                        queue.enqueue(val)
                        print(f'Enqueued: {val}')
                    elif queue_c == '2':
                        val = queue.dequeue()
                        print(f'Dequeued: {val}')
                    elif queue_c == '3':
                        print(f'Top value: {queue.peek()}')
                    elif queue_c == '4':
                        print(queue.output())
                    elif queue_c == '5':
                        break
                    else:
                        print("Invalid choice")
                except Exception as err:
                    print("Error:", err)
                
        elif choice == '4':
            capacity = int(input('Enter the size of the shuffled queue: '))
            queue = DSAQueue(capacity)
            while True:
                print('---Shuffling Queue Commands---')
                print('1. Enqueue')
                print('2. Dequeue')
                print('3. Peek')
                print('4. Display')
                print('5. Back to menu')
                queue_c = input('Choose an operation: ')
                try:
                    if queue_c == '1':
                        val = input('Value to enqueue: ')
                        queue.enqueue(val)
                        print(f'Enqueued: {val}')
                    elif queue_c == '2':
                        val = queue.dequeue()
                        print(f'Dequeued: {val}')
                    elif queue_c == '3':
                        print(f'Top value: {queue.peek()}')
                    elif queue_c == '4':
                        print(queue.output())
                    elif queue_c == '5':
                        break
                    else:
                        print("Invalid choice")
                except Exception as err:
                    print("Error:", err)

        elif choice == '5':
            equation = input('Enter an equation (please put spaces between characters): ')
            try:
                postfix = ShuffleQueue.infixTopostfix(equation)
                postfixstr = ''
                tempQueue = DSAQueue(100)
                while not postfix.isEmpty():
                    chip = postfix.dequeue()
                    postfixstr += str(chip) + ' '
                    tempQueue.enqueue(chip)
                print('Postfix equation:', postfixstr.strip())
                result = ShuffleQueue.evaluatepostfix(tempQueue)
                print("Evaluated result:", result)
            except Exception as err:
                print("Error: ", err)

        elif choice == '6':
            print('Exiting Program')
            break
        else:
            print("Invalid choice")