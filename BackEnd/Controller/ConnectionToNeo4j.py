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

def cvQuestionGen(id):
  query = "MATCH (j:CV{id:"+ id+"}) RETURN j.topic"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question




def session_Node_Count(session):
  # session ="2"
  query = "MATCH (a:CV{session: " +session+ "}) RETURN count(*)"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  return  gen_count


def get_node_id(session):
  query = "MATCH (a:CV{session: " + session + "}) RETURN a.id"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  return gen_count
# get_node_id("3")



def technical_question_keyword(table,id):
  val = "1"


  query = "MATCH(a:language{Name:'"+table+"'}) - [r: has]->(b:sub{id:'"+id+"'})RETURN b.Name"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question
# table ="java"
# technical_question_keyword(table)

def getTechNodeCount(db):
  query = "MATCH(a:language{Name:'"+db+"'}) - [r: has]->(b:sub{})RETURN count(*)"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  return gen_count



