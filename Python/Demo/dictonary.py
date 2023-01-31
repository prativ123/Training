#dictonary are known as object in other programming language and they always come in key value pair
student={"first_name" : "Prativ", "last_name":"Shrestha","age":22,"height":"5,10"}
print(type(student))
print(student["first_name"])
print(student["age"])

item = {
    "value":15,
    "value1":[1,2,3,4,5],
    "value2":[5,4,3,2,1],
}
print(item)
print(item["value1"])
print(item["value1"][2])

#nested dictionary -> dictionary inside dictonary
#all element in dictionary can be a value
nest_dict={
    "key1":{
        "nestKey":{"subnestKey":"finalValue"}
        },

    "key2":{
        "nestKey2":{"subnestKey2":"dinalValue2"}
    }
}
print(nest_dict["key1"]["nestKey"]["subnestKey"])
print(nest_dict["key1"]["nestKey"])


d={}
d["fruits"]="apple"
d["age"]=22
print(d)

#basic dictonary methods
#keys() -> it only prints the key of the dictionary.
#value()-> it only prints the value.
print(nest_dict.keys())
print(nest_dict.values())