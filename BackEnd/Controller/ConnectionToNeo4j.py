from py2neo import Graph

graph = Graph("http://neo4j:Sepalika1993@127.0.0.1:7474/db/data")


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
<<<<<<< HEAD
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



=======
    print(validationValue)
    return validationValue

def cvQuestionGen(db,id):
  query = "MATCH (j:"+db+"{id:"+ id+"}) RETURN j.topic"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question

def cvQuestionProjectGen(db,pid):
  query = "MATCH (j:"+db+"{pid:'"+ pid+"'}) RETURN j.topic"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question

# cvQuestionProjectGen("CV","p1")

def session_Node_Count(db,session):
  # session ="2"
  query = "MATCH (a:"+db+"{session: " +session+ "}) RETURN count(*)"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  return  gen_count


def get_node_id(db,session):
  query = "MATCH (a:"+db+"{session: " + session + "}) RETURN a.id"
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


def getProjects(db,id):
    query = "MATCH (a:"+db+"{id:"+id+"})-[:projects]->(proj) RETURN count(*)"
    # query = "MATCH (a:CV{id:5})-[:projects]->(projects)RETURN count(*)"
    get_projects =graph.run(query).evaluate()
    return get_projects
    # print(get_projects)

def getMatchingTopics(db,topic):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub{Name:'"+topic+"'})RETURN count(b.Name)>0"
    get_availability = graph.run(query).evaluate()
    return get_availability

def getMatchingTopicsNonTech(db):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub)RETURN count(b)>0"
    availability = graph.run(query).evaluate()
    return availability


def cvProjectTech(db,pid):
  query = "MATCH (j:"+db+"{pid:'"+ pid+"'}) RETURN j.technologies"
  gen_Question = graph.run(query).evaluate()
  return gen_Question

# pro = cvProjectTech("CV",'p1')
#
# print(pro)
>>>>>>> 2b5c4e4012b8aeeb2b77407be44e2676622f2818
