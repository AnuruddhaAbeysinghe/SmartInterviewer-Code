from py2neo import Graph
from py2neo import Node, Relationship


graph = Graph("http://neo4j:Sepalika1993@127.0.0.1:7474/db/data")

def validationAnswer(answer, lable):

  if lable == "why":
    if answer !="":
      return 1
    else:
      return None
  else:
    exist = "MATCH (a:User{Id:'U0002',"+lable+":'" + answer + "'})  RETURN 1"
    validationValue = graph.run(exist).evaluate()
    return validationValue

def createQtable1():
    exist = "MATCH (n:language) return n.qtable"
    qtableValue = graph.run(exist).evaluate()
    return qtableValue


# this is to send and update values
def createQtable(R):
    exist = "MATCH (n:language) SET n.qtable = $R RETURN n"
    qtableValue = graph.run(exist)

# another method
def edit_username(R):
    person = graph.merge_one('language', 'qtable')
    person['qtable'] = R
    person.push()



