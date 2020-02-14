import csv
def testfunction1():
    count=0
    with open('Clothing.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            if "Bachmann" in row["brand"]:
                count+=1
        return(count)

def testfunction2():
    max_cost=0
    max_cost_id=0
    with open('Clothing.csv', 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                if row["price"] > max_cost:
                    max_cost=row["price"]
                    max_cost_id=row["id"]
            return(max_cost_id)

def testfunction3():
    max_quantity=0
    max_quantity_product="test"
    with open('Clothing.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            if row["quantity"] > max_quantity:
                max_quantity=row["quantity"]
                max_quantity_product=row["product"]
        return(max_quantity_product)

def testfunction4():
    products={}
    finallist=[]
    with open('Clothing.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            if len(products) == 0:
                if row["productRating"] > 2:
                    if row["product"] != products:
                        products.update({row["productRating"]:1})
            for i in products:
                if row["productRating"] > 2:
                    if row["product"] != i:
                        i.update({row["productRating"]:1})
                    else:
                        i.value(i.value()+1)
        for x in products:
            if x.values > 2:
                finallist.append(x)
        return (finallist)

def testfunction5():
    repeat_s={
        "male":0
        "female":0
    }
    with open('Clothing.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            if row["size"]=="S"

testfunction4()
