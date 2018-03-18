class AndGate: 

    def __init__(self, input0, input1): 
        self._input0 = input0 
        self._input1 = input1 
        self._output = False 
        self._name = "YaAndGate" 

    def show(self): 
        print(self._name+" hat folgendes Ergebnis ermittelt: ")
        print(AndGate.__str__(self)) 

    def execute(self): 
        if self._input0 == self._input1 == True: 
            self._output = True
        else: 
            self._output = False 

    def __str__(self): 
      return str(self._input0)+"+"+str(self._input1)+"="+str(self._output)

    @property
    def input0(self):
        return self._input0
    def input0(self, value):
        if isinstance(value, (bool)):
            self._input0 = value

    @property
    def input1(self):
        return self._input1
    def input1(self, value):
        if isinstance(value, (bool)):
            self._input1 = value

    @property
    def output(self):
        return self._ouput
    def ouput(self, value):
        if isinstance(value, (bool)):
            self._ouput = value

    @property
    def name(self):
        return self._name
    def name(self):
        self._name = str(value)