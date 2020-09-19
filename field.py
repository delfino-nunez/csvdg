class Field():
    '''
    Data field
    Attributes:
        name    Field name
        type    Field type
    '''
    def __init__(self, name, type):
        '''
        Initialize field
        '''
        self.name = name
        self.type = type

    def generate_data(self):
        '''
        Generate random data
        '''
        raise NotImplementedError('Subclass must implement abstract method')

    def __str__(self):
        '''
        Field string representation
        '''
        raise NotImplementedError('Subclass must implement abstract method')

class StringField(Field):
    '''
    String field

    Attributes:
        name    Field name
        length  Random data length
        text    String format for random data
        letters Characters used for random data
    '''

    def __init__(self, name, length, text = None, letters = None):
        '''
        Initialize String field
        '''
        super().__init__(name, 'STRING')
        self.length  = length
        self.text    = text
        self.letters = letters
    
    def __str__(self):
        '''
        Print String field representation
        '''
        return 'Name: {0}\nType: {1}\nLength: {2}\nText: {3}\nLetters: {4}'. \
            format(self.name, \
                   self.type, \
                   self.length, \
                   self.text, \
                   self.letters
                )

    def generate_data(self):
        '''
        Generate random data
        '''
        pass
    
    

class NumberField(Field):
    '''
    Number field
    
    Attributes:
        name    Field name
        text    Text template for random numbers
    '''

    def __init__(self, name, text = None):
        '''
        Initialize number field
        '''
        super().__init__(name, 'NUMBER')
        self.text = text

    def __str__(self):
        '''
        Print Number field representation
        '''
        return 'Name: {0}\nType: {1}\nText: {2}'. \
            format(self.name, \
                   self.type, \
                   self.text
                )

    def generate_data(self):
        '''
        Generate random data
        '''
        pass

class DateTimeField(Field):
    '''
    Date Time field
    
    Attributes:
        name    Field name
        pattern Text template for random datetime
        start   Start date
        end     End date
    '''

    def __init__(self, name, pattern, start = None, end = None):
        '''
        Initialize data time filed
        '''
        super().__init__(name, 'DATETIME')
        self.pattern = pattern
        self.start   = start
        self.end     = end

    def __str__(self):
        '''
        Print DataTime field representation
        '''
        return 'Name: {0}\nType: {1}\nPattern: {2}\nStart: {3}\nEnd: {4}'. \
            format(self.name, \
                   self.type, \
                   self.pattern, \
                   self.start, \
                   self.end
                )

    def generate_data(self):
        '''
        Generate random data
        '''
        pass

class BooleanField(Field):
    '''
    Boolean field
    
    Attributes:
        name    Field name
    '''

    def __init__(self, name):
        '''
        Initialize boolean filed
        '''
        super().__init__(name, 'BOOLEAN')

    def __str__(self):
        '''
        Print Boolean field representation
        '''
        return 'Name: {0}\nType: {1}'. \
            format(self.name, \
                   self.type
                )

    def generate_data(self):
        '''
        Generate random data
        '''
        pass
