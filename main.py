class process:
    def __init__(self,id,cpu_state,memory,scheduling_information,accounting_information,process_state,parent,children,open_files,other_resources,
                 arrival_time,CPU_required,Quantum,ContextSwitch):
        #int
        self.id = id
        #int
        self.cpu_state = cpu_state
        #int
        self.memory = memory
        #int
        self.scheduling_information = scheduling_information
        #int
        self.accounting_information = accounting_information
        #string
        self.process_state = process_state
        #pointer
        self.parent = parent
        #pointer
        self.children = children
        #pointer - null(?)
        self.open_files = open_files
        #string
        self.other_resources = other_resources
        #int
        self.arrival_time = arrival_time
        #int
        self.CPU_required = CPU_required
        #int
        self.quantum = Quantum
        #int
        self.ContextSwitch = ContextSwitch

    def returnId(self):
        return self.id

    def returnCPUstate(self):
        return self.cpu_state
    
    def returnMemory(self):
        return self.memory
    def returnSched_info(self):
        return self.scheduling_information
    def returnAccounting_info(self):
        return self.accounting_information
    def returnProcess_state(self):
        return self.process_state
    def returnParent(self):
        return self.parent
    def returnChildren(self):
        return self.children
    def returnOpen_files(self):
        return self.open_files
    def returnOther_resources(self):
        return self.other_resources
    def returnArrival_time(self):
        return self.arrival_time
    def returnCpu_required(self):
        return self.CPU_required
    def returnQuanutm(self):
        return self.quantum
    def returnContext_swtich(self):
        return self.ContextSwitch

#reading files: 
def ProcessReader(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        values = line.split(',')

        id=int(values[0])
        CPU_state=int(values[1])
        memory=int(values[2])
        sched_info=int(values[3])
        acc_info=int(values[4])
        process_state =(values[5])
        parent=0 #need to fix this but i dont want to do that rn
        children=0 #need to fix this but i dont want to do that rn
        open_files=0#need to fix this but i dont want to do that rn
        other_resources=(values[9])
        arrival_time=int(values[10])
        CPU_required=int(values[11])
        quantum=int(values[12])
        contextSwitch=int(values[13])

        return process(id,CPU_state,memory,sched_info,acc_info,process_state,parent,
        children,open_files,other_resources,arrival_time,CPU_required,quantum,contextSwitch)


#testing --seems to work!
processTest = ProcessReader('exampleData1.txt')
print(processTest.returnId())


