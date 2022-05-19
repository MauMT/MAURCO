# lógica de enteros 0 es False,
# cualquier otro valor es True

semantic = {
  'int': {
    '+' : {
        'int':'int',
        'float':'float',
        'char':'error'
    },
    '-':{
        'int':'int',
        'float':'float',
        'char':'error'
    },
    #checar asignación entre int y float
    '=':{
        'int':'int',
        'float':'error',
        'char':'error'
    },
    '*':{
        'int':'int',
        'float':'float',
        'char':'error'
    },
    '/':{
        'int':'float',
        'float':'float',
        'char':'error'
    },
    '<':{
        'int':'int',
        'float':'int',
        'char':'error'
    },
    '>':{
        'int':'int',
        'float':'int',
        'char':'error'
    },
    '==':{
        'int':'int',
        'float':'int',
        'char':'error'
    },
    '!=':{
        'int':'int',
        'float':'int',
        'char':'error'
    }
},

 'float': {
    '+' : {
        'int':'float',
        'float':'float',
        'char':'error'
    },
    '-':{
        'int':'float',
        'float':'float',
        'char':'error'
    },
    '=':{
        'int':'float',
        'float':'float',
        'char':'error'
    },
    '*':{
        'int':'float',
        'float':'float',
        'char':'error'
    },
    '/':{
        'int':'float',
        'float':'float',
        'char':'error'
    },
    '.':{
        'int':'float',
        'float':'float'
    },
    '<':{
        'int':'int',
        'float':'int'
    },
    '>':{
        'int':'int',
        'float':'int'
    },
    '==':{
        'int':'int',
        'float':'int',
        'char':'error'
    },
    '!=':{
        'int':'int',
        'float':'int',
        'char':'error'
    }
},

 'char': {
    '=' : {
        'char':'char'
    },
    '==':{
        'char':'int'
    },
    '!=':{
        'char':'int'
    }
 }