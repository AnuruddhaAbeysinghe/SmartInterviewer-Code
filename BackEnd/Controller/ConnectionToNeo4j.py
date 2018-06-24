from py2neo import Graph
from py2neo import Node, Relationship


graph = Graph()

def validationAnswer(answer, lable):

  if lable == "why":
    if answer !="":
      return 1
  else:
    exist = "MATCH (a:User{Id:'U0002',"+lable+":'" + answer + "'})  RETURN 1"
    validationValue = graph.run(exist).evaluate()
    return validationValue