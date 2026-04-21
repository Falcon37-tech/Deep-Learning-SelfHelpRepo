
'''Open Neo4j using Cypher Query'''

# get a free indtance on 

#pen and create instance

#Import and run the dataset(Northwind dataset)

#get to know the database

#Run first query - 
MATCH (n:Product) RETURN n LIMIT 25;  '''There you’ll see how many nodes you have and all their labels, the number of relationships and their types, and also a list of all the property keys present in the database. '''

 ''' Executing queries with graph results '''

MATCH path=(:Product)-[:PART_OF]->(c:Category)
WHERE c.categoryName = 'Produce'
RETURN path;
 '''Here you can see Product nodes with PART_OF relationships to the Category with name Produce. '''


#showing tabular results
 '''The query uses variables, c and p, for the category and the product as you will want to refer to them later. '''

MATCH (p:Product)-[:PART_OF]->(c:Category)
WHERE c.categoryName = 'Produce'
RETURN p.productName,c.categoryName;

###Use basic Cypher to answer questions

CALL db.schema.visualization() #Besides the sidebar with the overview, a quick way to show the current graph schema is to CALL this procedure

#Let’s take a look at the different companies supplying Northwind with products and see which supplier provides products from which categories:
MATCH (s:Supplier)-->(:Product)-->(c:Category)
RETURN s.companyName as company, collect(distinct c.categoryName) as categories

#Maybe you are interested only in suppliers of a certain category, say Condiments
MATCH (s:Supplier)-->(:Product)-->(c:Category)
WHERE c.categoryName = 'Condiments'
RETURN DISTINCT s.companyName as condimentsSuppliers


#Since you are not interested in the Product nodes, nor the exact types of the relationships between the nodes here, you don’t have to specify them.

###Write more advanced Cypher for problem solving
#Assume that you want to see which product categories are typically co-ordered with other product categories and how frequently.
#This might help you understand which products to promote alongside others.

''' which categories are the products of an order in '''
MATCH (o:Order)-[:ORDERS]->(:Product)-[:PART_OF]->(c:Category)
''' retain same ordering of categories '''
WITH o, c ORDER BY c.categoryName
 ''' aggregate categories by order into a list of names '''
WITH o, collect(DISTINCT c.categoryName) as categories
 ''' only orders with more than one category '''
WHERE size(categories) > 1
 ''' count how frequently the pairings occur '''
RETURN categories, count(*) as freq
 ''' order by frequency '''
ORDER BY freq DESC
LIMIT 50

#You find the "peer-groups" of our customers, which then can be used for product recommendations (people who bought X also bought) or segmentation into clusters of your customer base.

 ''' pattern from customer purchasing products to another customer purchasing the same products '''
MATCH (c:Customer)-[:PURCHASED]->(:Order)-[:ORDERS]->(p:Product)<-[:ORDERS]-(:Order)<-[:PURCHASED]-(c2:Customer)
 ''' don't want the same customer pair twice '''
WHERE c < c2
 ''' sort by the top-occuring products '''
WITH c, c2, p, count(*) as productOccurrence
ORDER BY productOccurrence DESC
 ''' return customer pairs ranked by similarity and the top 5 products '''
RETURN c.companyName, c2.companyName, sum(productOccurrence) as similarity, collect(distinct p.productName)[0..5] as topProducts
ORDER BY similarity DESC LIMIT 10

#Now you could create relationships for all customers that score more than 50 in your similarity score and see how they cluster.

MATCH (c:Customer)-[:PURCHASED]->(:Order)-[:ORDERS]->(p:Product)<-[:ORDERS]-(:Order)<-[:PURCHASED]-(c2:Customer)
WHERE c < c2
 ''' find similar customers '''
WITH c, c2, count(*) as similarity
 ''' with at least 50 shared product purchases '''
WHERE similarity > 50
 ''' create a relationship between the two without specifying direction '''
MERGE (c)-[sim:SIMILAR_TO]-(c2)
 ''' set relationship weight from similairity '''
ON CREATE SET sim.weight = similarity

#The new relationship shows up in your sidebar (after refresh at the bottom) and graph model and you can use it to show clusters of our customers.
#If you style the relationship SIMILAR_TO with the weight as caption you can see the strength of the similarity.

MATCH path=()-[:SIMILAR_TO]->() RETURN path #This should give you a good starting point to see the power of graph queries.

# [Cypher Online Courses](https://neo4j.com/docs/cypher-manual/5/clauses/use/)
# [Cypher Manual]
# [Cypher Cheat-Sheet](https://neo4j.com/docs/cypher-cheat-sheet/5/all/).

