import os
from thriftcli import ThriftService, ThriftStruct, ThriftParser

TEST_SERVER_ADDRESS = 'localhost:9090'
TEST_SERVER_ADDRESS2 = 'http://www.somewebsite.net:12201/with/an/unused/path'
TEST_SERVER_ADDRESS3 = 'https://noport.com/with/an/unused/path?and=parameters'
TEST_SERVER_HOSTNAME = 'localhost'
TEST_SERVER_HOSTNAME2 = 'www.somewebsite.net'
TEST_SERVER_HOSTNAME3 = 'noport.com'
TEST_SERVER_PORT = 9090
TEST_THRIFT_PATH = 'somefolder/Something.thrift'
TEST_THRIFT_MODULE_PATH = 'gen-py/Something'
TEST_THRIFT_MODULE_NAME = 'Something'
TEST_THRIFT_NAMESPACE = 'Something'
TEST_SERVER_PORT2 = 12201
TEST_SERVER_PORT3 = None
TEST_THRIFT_STRUCT_NAME = 'SomeStruct'
TEST_THRIFT_STRUCT_NAME2 = 'SomeStruct2'
TEST_THRIFT_STRUCT_NAME3 = 'SomeStruct3'
TEST_THRIFT_STRUCT_REFERENCE = '%s.%s' % (TEST_THRIFT_NAMESPACE, TEST_THRIFT_STRUCT_NAME)
TEST_THRIFT_STRUCT_REFERENCE2 = '%s.%s' % (TEST_THRIFT_NAMESPACE, TEST_THRIFT_STRUCT_NAME2)
TEST_THRIFT_STRUCT_REFERENCE3 = '%s.%s' % (TEST_THRIFT_NAMESPACE, TEST_THRIFT_STRUCT_NAME3)
TEST_THRIFT_STRUCT_FIELDS = {
    'thing_one': ThriftStruct.Field(1, 'string', 'thing_one'),
    'thing_two': ThriftStruct.Field(2, 'double', 'thing_two', default='2.0'),
    'thing_three': ThriftStruct.Field(3, 'bool', 'thing_three', default='False')
}
TEST_THRIFT_STRUCT_FIELDS2 = {
    'thing_one': ThriftStruct.Field(1, 'i8', 'thing_one', required=True),
    'thing_two': ThriftStruct.Field(2, 'i16', 'thing_two', required=False),
    'thing_three': ThriftStruct.Field(3, 'i32', 'thing_three', optional=True),
    'thing_four': ThriftStruct.Field(4, 'i64', 'thing_four', optional=False, default='0'),
    'thing_five': ThriftStruct.Field(5, 'binary', 'thing_five', required=True, optional=False),
    'thing_six': ThriftStruct.Field(6, 'byte', 'thing_six', required=False, optional=True)
}
TEST_THRIFT_STRUCT_FIELDS3 = {
    'thing_one': ThriftStruct.Field(1, 'list<string>', 'thing_one', required=True),
    'thing_two': ThriftStruct.Field(2, 'set<i8>', 'thing_two', optional=True),
    'thing_three': ThriftStruct.Field(3, 'map<string, string>', 'thing_three', required=True),
    'thing_four': ThriftStruct.Field(4, 'list<%s>' % TEST_THRIFT_STRUCT_NAME, 'thing_four'),
    'thing_five': ThriftStruct.Field(5, 'map<%s, %s>' % (TEST_THRIFT_STRUCT_NAME, TEST_THRIFT_STRUCT_NAME2),
                                     'thing_five'),
    'thing_six': ThriftStruct.Field(6, 'set<list<%s>>' % TEST_THRIFT_STRUCT_NAME2, 'thing_six')
}
TEST_THRIFT_STRUCT_DEFINITION = ("""
    struct %s {
        string thing_one,
        double thing_two = 2.0,
        bool thing_three = False;
    }""" % TEST_THRIFT_STRUCT_NAME).lstrip('\n')
TEST_THRIFT_STRUCT_DEFINITION2 = ("""
    struct %s {
        1:required i8 thing_one,
        2:i16 thing_two,
        3:optional i32 thing_three,
        4:required i64 thing_four = 0,
        5:required binary thing_five,
        6:optional byte thing_six
    }""" % TEST_THRIFT_STRUCT_NAME2).lstrip('\n')
TEST_THRIFT_STRUCT_DEFINITION3 = ("""
    struct %s {
        1:required list<string> thing_one,
        2:optional set<i8> thing_two,
        3:required map<string, string> thing_three,
        4:list<%s> thing_four,
        5:map<%s, %s> thing_five,
        6:set<list<%s>> thing_six
    }""" % (TEST_THRIFT_STRUCT_NAME3,
            TEST_THRIFT_STRUCT_NAME,
            TEST_THRIFT_STRUCT_NAME,
            TEST_THRIFT_STRUCT_NAME2,
            TEST_THRIFT_STRUCT_NAME2)).lstrip('\n')
TEST_THRIFT_STRUCT = ThriftStruct(TEST_THRIFT_STRUCT_REFERENCE, TEST_THRIFT_STRUCT_FIELDS)
TEST_THRIFT_STRUCT2 = ThriftStruct(TEST_THRIFT_STRUCT_REFERENCE2, TEST_THRIFT_STRUCT_FIELDS2)
TEST_THRIFT_STRUCT3 = ThriftStruct(TEST_THRIFT_STRUCT_REFERENCE3, TEST_THRIFT_STRUCT_FIELDS3)
TEST_THRIFT_SERVICE_NAME = 'SomeService'
TEST_THRIFT_SERVICE_NAME2 = 'SomeService2'
TEST_THRIFT_SERVICE_NAME3 = 'SomeService3'
TEST_THRIFT_SERVICE_REFERENCE = '%s.%s' % (TEST_THRIFT_NAMESPACE, TEST_THRIFT_SERVICE_NAME)
TEST_THRIFT_SERVICE_REFERENCE2 = '%s.%s' % (TEST_THRIFT_NAMESPACE, TEST_THRIFT_SERVICE_NAME2)
TEST_THRIFT_SERVICE_REFERENCE3 = '%s.%s' % (TEST_THRIFT_NAMESPACE, TEST_THRIFT_SERVICE_NAME3)
TEST_THRIFT_SERVICE_ENDPOINTS = {
    'ping': ThriftService.Endpoint('void', 'ping'),
    'doSomething1': ThriftService.Endpoint('i32', 'doSomething1', {
        'num1': ThriftStruct.Field(1, 'i32', 'num1'),
        'num2': ThriftStruct.Field(2, 'i32', 'num2'),
        'op': ThriftStruct.Field(3, 'Operation', 'op')
    }),
    'useSomeStruct': ThriftService.Endpoint('void', 'useSomeStruct', {
        'someStruct': ThriftStruct.Field(1, 'SomeStruct', 'someStruct')
    }, oneway=True)
}
TEST_THRIFT_SERVICE_ENDPOINTS2 = {
    'ping': ThriftService.Endpoint('void', 'ping'),
    'doSomething2': ThriftService.Endpoint('string', 'doSomething2', {
        'num1': ThriftStruct.Field(1, 'i32', 'num1')
    }),
    'useSomeStruct2': ThriftService.Endpoint('void', 'useSomeStruct2', {
        'someStruct': ThriftStruct.Field(1, 'SomeStruct2', 'someStruct')
    })
}
TEST_THRIFT_SERVICE_ENDPOINTS3 = {
    'ping': ThriftService.Endpoint('void', 'ping'),
    'passMap': ThriftService.Endpoint('MapType', 'passMap', {
        'myMap': ThriftStruct.Field(1, 'MapType', 'myMap')
    }),
    'passSetOfLists': ThriftService.Endpoint('set<list<%s>>' % TEST_THRIFT_STRUCT_REFERENCE, 'passSetOfLists', {
        'setOfLists': ThriftStruct.Field(1, 'set<list<%s>>' % TEST_THRIFT_STRUCT_REFERENCE, 'setOfLists')
    })
}
TEST_THRIFT_SERVICE_DEFINITION = ("""
    service %s {
        void ping(),
        i32 doSomething1(i32 num1, i32 num2, Operation op),
        oneway void useSomeStruct(1:SomeStruct someStruct);
    }""" % TEST_THRIFT_SERVICE_NAME).lstrip('\n')
TEST_THRIFT_SERVICE_DEFINITION2 = ("""
    service %s {
        void ping(),
        string doSomething2(1:i32 num1),
        void useSomeStruct2(1:SomeStruct2 someStruct)
    }""" % TEST_THRIFT_SERVICE_NAME2).lstrip('\n')
TEST_THRIFT_SERVICE_DEFINITION3 = ("""
    service %s {
        void ping(),
        MapType passMap(1:MapType myMap),
        set<list<%s>> passSetOfLists(1:set<list<%s>> setOfLists)
    }""" % (TEST_THRIFT_SERVICE_NAME3, TEST_THRIFT_STRUCT_NAME, TEST_THRIFT_STRUCT_NAME)).lstrip('\n')
TEST_THRIFT_SERVICE = ThriftService(TEST_THRIFT_SERVICE_REFERENCE, TEST_THRIFT_SERVICE_ENDPOINTS)
TEST_THRIFT_SERVICE2 = ThriftService(TEST_THRIFT_SERVICE_REFERENCE2, TEST_THRIFT_SERVICE_ENDPOINTS2)
TEST_THRIFT_SERVICE3 = ThriftService(TEST_THRIFT_SERVICE_REFERENCE3, TEST_THRIFT_SERVICE_ENDPOINTS3)
TEST_THRIFT_ENUM_NAME = 'SomeEnum'
TEST_THRIFT_ENUM_NAME2 = 'SomeEnum2'
TEST_THRIFT_ENUM_DEFINITION = ("""
    enum %s {
        A,
        B,
        C,
        D
    }""" % TEST_THRIFT_ENUM_NAME).lstrip('\n')
TEST_THRIFT_ENUM_DEFINITION2 = ("""
    enum %s {
        W,
        X = 4,
        Y = 0xf2a,
        Z
    }""" % TEST_THRIFT_ENUM_NAME2).lstrip('\n')
TEST_THRIFT_ENUM_REFERENCE = '%s.%s' % (TEST_THRIFT_NAMESPACE, TEST_THRIFT_ENUM_NAME)
TEST_THRIFT_ENUM_REFERENCE2 = '%s.%s' % (TEST_THRIFT_NAMESPACE, TEST_THRIFT_ENUM_NAME2)
TEST_THRIFT_TYPEDEF_DEFINITION = 'typedef i64 UserId'
TEST_THRIFT_TYPEDEF_DEFINITION2 = 'typedef map<string, string> MapType'
TEST_THRIFT_TYPEDEF_DEFINITION3 = 'typedef list<SomeStruct> SomeStructs'
TEST_THRIFT_TYPEDEFS = {
    '%s.UserId' % TEST_THRIFT_NAMESPACE: 'i64',
    '%s.MapType' % TEST_THRIFT_NAMESPACE: 'map<string, string>',
    '%s.SomeStructs' % TEST_THRIFT_NAMESPACE: 'list<%s.SomeStruct>' % TEST_THRIFT_NAMESPACE
}
TEST_THRIFT_CONTENT = '\n'.join([
    TEST_THRIFT_ENUM_DEFINITION,
    TEST_THRIFT_ENUM_DEFINITION2,
    TEST_THRIFT_TYPEDEF_DEFINITION,
    TEST_THRIFT_TYPEDEF_DEFINITION2,
    TEST_THRIFT_TYPEDEF_DEFINITION3,
    TEST_THRIFT_STRUCT_DEFINITION,
    TEST_THRIFT_STRUCT_DEFINITION2,
    TEST_THRIFT_STRUCT_DEFINITION3,
    TEST_THRIFT_SERVICE_DEFINITION,
    TEST_THRIFT_SERVICE_DEFINITION2,
    TEST_THRIFT_SERVICE_DEFINITION3
])
TEST_THRIFT_STRUCTS = {
    TEST_THRIFT_STRUCT_REFERENCE: TEST_THRIFT_STRUCT,
    TEST_THRIFT_STRUCT_REFERENCE2: TEST_THRIFT_STRUCT2,
    TEST_THRIFT_STRUCT_REFERENCE3: TEST_THRIFT_STRUCT3
}
TEST_THRIFT_SERVICES = {
    TEST_THRIFT_SERVICE_REFERENCE: TEST_THRIFT_SERVICE,
    TEST_THRIFT_SERVICE_REFERENCE2: TEST_THRIFT_SERVICE2,
    TEST_THRIFT_SERVICE_REFERENCE3: TEST_THRIFT_SERVICE3
}
TEST_THRIFT_ENUMS = {TEST_THRIFT_ENUM_REFERENCE, TEST_THRIFT_ENUM_REFERENCE2}
TEST_THRIFT_PARSE_RESULT = ThriftParser.Result(
    TEST_THRIFT_STRUCTS, TEST_THRIFT_SERVICES, TEST_THRIFT_ENUMS, TEST_THRIFT_TYPEDEFS)
TEST_THRIFT_INCLUDE_STATEMENT = 'include "Included.thrift"'
TEST_THRIFT_INCLUDED_NAMESPACE = 'Included'
TEST_THRIFT_INCLUDED_ENUM_NAME = 'SomeIncludedEnum'
TEST_THRIFT_INCLUDED_ENUM_DEFINITION = ("""
    enum %s {
        THIS_STUFF,
        THAT_STUFF,
        MORE_STUFF
    }
""" % TEST_THRIFT_INCLUDED_ENUM_NAME).lstrip('\n')
TEST_THRIFT_INCLUDED_ENUM_REFERENCE = '%s.%s' % (TEST_THRIFT_INCLUDED_NAMESPACE, TEST_THRIFT_INCLUDED_ENUM_NAME)
TEST_THRIFT_INCLUDED_STRUCT_NAME = 'SomeIncludedStruct'
TEST_THRIFT_INCLUDED_STRUCT_REFERENCE = '%s.%s' % (TEST_THRIFT_INCLUDED_NAMESPACE, TEST_THRIFT_INCLUDED_STRUCT_NAME)
TEST_THRIFT_INCLUDED_STRUCT_DEFINITION = ("""
    struct %s {
        1:string some_string,
        2:%s my_enum
    }
""" % (TEST_THRIFT_INCLUDED_STRUCT_NAME, TEST_THRIFT_INCLUDED_ENUM_NAME)).lstrip('\n')
TEST_THRIFT_INCLUDED_STRUCT_FIELDS = {
    'some_string': ThriftStruct.Field(1, 'string', 'some_string'),
    'my_enum': ThriftStruct.Field(2, TEST_THRIFT_INCLUDED_ENUM_REFERENCE, 'my_enum')
}
TEST_THRIFT_INCLUDED_STRUCT = ThriftStruct('%s.%s' % (TEST_THRIFT_INCLUDED_NAMESPACE, TEST_THRIFT_INCLUDED_STRUCT_NAME),
                                           TEST_THRIFT_INCLUDED_STRUCT_FIELDS)
TEST_THRIFT_INCLUDED_SERVICE_NAME = 'SomeIncludedService'
TEST_THRIFT_INCLUDED_SERVICE_REFERENCE = '%s.%s' % (TEST_THRIFT_INCLUDED_NAMESPACE, TEST_THRIFT_INCLUDED_SERVICE_NAME)
TEST_THRIFT_INCLUDED_SERVICE_DEFINITION = ("""
    service %s {
        %s passSomeStuff(1:%s someStuff),
    }""" % (
    TEST_THRIFT_INCLUDED_SERVICE_NAME, TEST_THRIFT_INCLUDED_STRUCT_NAME, TEST_THRIFT_INCLUDED_STRUCT_NAME)).lstrip('\n')
TEST_THRIFT_INCLUDED_SERVICE_ENDPOINTS = {
    'passSomeStuff': ThriftService.Endpoint(TEST_THRIFT_INCLUDED_STRUCT_REFERENCE, 'passSomeStuff', {
        'someStuff': ThriftStruct.Field(1, TEST_THRIFT_INCLUDED_STRUCT_REFERENCE, 'someStuff')
    })
}
TEST_THRIFT_INCLUDED_SERVICE = ThriftStruct(TEST_THRIFT_INCLUDED_SERVICE_NAME, TEST_THRIFT_INCLUDED_SERVICE_ENDPOINTS)
TEST_THRIFT_INCLUDED_STRUCTS = {
    TEST_THRIFT_INCLUDED_STRUCT_REFERENCE: TEST_THRIFT_INCLUDED_STRUCT
}
TEST_THRIFT_INCLUDED_SERVICES = {
    TEST_THRIFT_INCLUDED_SERVICE_REFERENCE: TEST_THRIFT_INCLUDED_SERVICE
}
TEST_THRIFT_INCLUDED_ENUMS = {TEST_THRIFT_INCLUDED_ENUM_REFERENCE}
TEST_THRIFT_INCLUDED_TYPEDEF_DEFINITION = 'typedef i64 Id'
TEST_THRIFT_INCLUDED_TYPEDEF_DEFINITION2 = 'typedef list<Id> Ids'
TEST_THRIFT_INCLUDED_TYPEDEFS = {
    '%s.Id' % TEST_THRIFT_INCLUDED_NAMESPACE: 'i64',
    '%s.Ids' % TEST_THRIFT_INCLUDED_NAMESPACE: 'list<%s.Id>' % TEST_THRIFT_INCLUDED_NAMESPACE,
}
TEST_THRIFT_INCLUDED_PARSE_RESULT = ThriftParser.Result(TEST_THRIFT_INCLUDED_STRUCTS, TEST_THRIFT_INCLUDED_SERVICES,
                                                        TEST_THRIFT_INCLUDED_ENUMS, TEST_THRIFT_INCLUDED_TYPEDEFS)
TEST_THRIFT_INCLUDED_CONTENT = '\n'.join([
    TEST_THRIFT_INCLUDED_ENUM_DEFINITION,
    TEST_THRIFT_INCLUDED_STRUCT_DEFINITION,
    TEST_THRIFT_INCLUDED_SERVICE_DEFINITION
])
TEST_THRIFT_INCLUDING_NAMESPACE = 'Including'
TEST_THRIFT_INCLUDING_ENUM_NAME = 'SomeIncludingEnum'
TEST_THRIFT_INCLUDING_ENUM_DEFINITION = ("""
    enum %s {
        ONE,
        TWO,
        THREE
    }""" % TEST_THRIFT_INCLUDING_ENUM_NAME).lstrip('\n')
TEST_THRIFT_INCLUDING_ENUM_REFERENCE = '%s.%s' % (TEST_THRIFT_INCLUDING_NAMESPACE, TEST_THRIFT_INCLUDING_ENUM_NAME)
TEST_THRIFT_INCLUDING_ENUMS = {TEST_THRIFT_INCLUDED_ENUM_REFERENCE, TEST_THRIFT_INCLUDING_ENUM_REFERENCE}
TEST_THRIFT_INCLUDING_STRUCT_NAME = 'SomeIncludingStruct'
TEST_THRIFT_INCLUDING_STRUCT_REFERENCE = '%s.%s' % (TEST_THRIFT_INCLUDING_NAMESPACE, TEST_THRIFT_INCLUDING_STRUCT_NAME)
TEST_THRIFT_INCLUDING_STRUCT_DEFINITION = ("""
    struct %s {
        1:%s included_enum,
        2:%s included_struct,
        3:%s my_enum
    }""" % (TEST_THRIFT_INCLUDING_STRUCT_NAME, TEST_THRIFT_INCLUDED_ENUM_REFERENCE,
            TEST_THRIFT_INCLUDED_STRUCT_REFERENCE, TEST_THRIFT_INCLUDING_ENUM_REFERENCE)).lstrip('\n')
TEST_THRIFT_INCLUDING_STRUCT_FIELDS = {
    'included_enum': ThriftStruct.Field(1, TEST_THRIFT_INCLUDED_ENUM_REFERENCE, 'included_enum'),
    'included_struct': ThriftStruct.Field(2, TEST_THRIFT_INCLUDED_STRUCT_REFERENCE, 'included_struct'),
    'my_enum': ThriftStruct.Field(3, TEST_THRIFT_INCLUDING_ENUM_REFERENCE, 'my_enum')
}
TEST_THRIFT_INCLUDING_STRUCT = ThriftStruct(TEST_THRIFT_INCLUDING_STRUCT_REFERENCE, TEST_THRIFT_INCLUDING_STRUCT_FIELDS)
TEST_THRIFT_INCLUDING_SERVICE_NAME = 'SomeIncludingService'
TEST_THRIFT_INCLUDING_SERVICE_REFERENCE = '%s.%s' % (TEST_THRIFT_INCLUDING_NAMESPACE,
                                                     TEST_THRIFT_INCLUDING_SERVICE_NAME)
TEST_THRIFT_INCLUDING_SERVICE_DEFINITION = ("""
    service %s extends %s {
        %s passIncludedStruct(1:%s includedStruct),
        %s passMyStruct(1:%s myStruct),
    }""" % (TEST_THRIFT_INCLUDING_SERVICE_NAME, TEST_THRIFT_INCLUDED_SERVICE_REFERENCE,
            TEST_THRIFT_INCLUDED_STRUCT_REFERENCE, TEST_THRIFT_INCLUDED_STRUCT_REFERENCE,
            TEST_THRIFT_INCLUDING_STRUCT_NAME, TEST_THRIFT_INCLUDING_STRUCT_NAME)).lstrip('\n')
TEST_THRIFT_INCLUDING_SERVICE_ENDPOINTS = {
    'passIncludedStruct': ThriftService.Endpoint(
        TEST_THRIFT_INCLUDED_STRUCT_REFERENCE,
        'passIncludedStruct',
        {
            'includedStruct': ThriftStruct.Field(
                1, TEST_THRIFT_INCLUDED_STRUCT_REFERENCE, 'includedStruct')
        }),
    'passMyStruct': ThriftService.Endpoint(
        TEST_THRIFT_INCLUDING_STRUCT_REFERENCE,
        'passMyStruct',
        {
            'myStruct': ThriftStruct.Field(
                1, TEST_THRIFT_INCLUDING_STRUCT_REFERENCE, 'myStruct')
        })
}
TEST_THRIFT_INCLUDING_SERVICE = ThriftService(TEST_THRIFT_INCLUDING_SERVICE_REFERENCE,
                                              TEST_THRIFT_INCLUDING_SERVICE_ENDPOINTS)
TEST_THRIFT_INCLUDING_SERVICES = {
    TEST_THRIFT_INCLUDING_SERVICE_REFERENCE: TEST_THRIFT_INCLUDING_SERVICE
}
TEST_THRIFT_INCLUDING_STRUCTS = {
    TEST_THRIFT_INCLUDED_STRUCT_REFERENCE: TEST_THRIFT_INCLUDED_STRUCT,
    TEST_THRIFT_INCLUDING_STRUCT_REFERENCE: TEST_THRIFT_INCLUDING_STRUCT
}
TEST_THRIFT_INCLUDING_TYPEDEF_DEFINITION = 'typedef bool Bool'
TEST_THRIFT_INCLUDING_TYPEDEFS = {
    '%s.Bool' % TEST_THRIFT_INCLUDING_NAMESPACE: 'bool'
}
TEST_THRIFT_INCLUDING_TYPEDEFS.update(TEST_THRIFT_INCLUDED_TYPEDEFS.copy())
TEST_THRIFT_INCLUDING_PARSE_RESULT = ThriftParser.Result(TEST_THRIFT_INCLUDING_STRUCTS, TEST_THRIFT_INCLUDING_SERVICES,
                                                         TEST_THRIFT_INCLUDING_ENUMS, TEST_THRIFT_INCLUDING_TYPEDEFS)
TEST_THRIFT_ENDPOINT_NAME = 'SomeService.useSomeStruct'
TEST_THRIFT_METHOD_NAME = 'useSomeStruct'
