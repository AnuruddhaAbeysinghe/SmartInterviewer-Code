from py2neo import Graph

graph = Graph()


def ontologyQuestionGen(id):
  query = "MATCH (j:Java{id:"+ id+"}) RETURN j.topic"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question

# ontologyQuestionGen("1")


def getValueFromdb(subsection):

    subsection = ""+subsection
    exist = "MATCH(a: language) - [r: has]->(b:sub{Name:'"+subsection+"'})RETURN b.Details"
    print(exist)
    validationValue = graph.run(exist).evaluate()
    print(validationValue)
    return validationValue



