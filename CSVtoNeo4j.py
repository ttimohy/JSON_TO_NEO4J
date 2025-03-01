import csv
import neo4j 
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
database = "neo4j"

user = "neo4j" #default username, you can find your info in the neo4j browser by typing :  `show current user`
password = "pass" #change this accroding to your info


driver = GraphDatabase.driver(uri, auth=(user, password))

'''

=======================================================================================================
Hello! This is the node creation script. It is used to create nodes and relationships in the database.

To run this script you will need all of the .csv files that you generated using your data extraction python notebook.

To run this script, you will need to uncomment the function calls at the bottom of the script.

This script will merge the data from the .csv files into the database.

If you have any questions, please reach out to me on Teams.

Thanks!😊
=======================================================================================================

'''


def create_company_node(tx):
    tx.run('''
           LOAD CSV WITH HEADERS FROM 'file:///company.csv' AS row
              CREATE (c:Company {
               id: toInteger(row.id),
               name: row.Company,
               Dun_Bradstreet_num: row.Dun_Bradstreet_num,
               HUBZone_Owned: row.`HUBZone Owned`,
               Socially_and_Economically_Disadvantaged: row.`Socially and Economically Disadvantaged`,
               Women_Owned: row.`Women Owned`,
               Number_Employees: toInteger(row.`Number Employees`),
               Company_Website: row.`Company Website`,
               Address1: row.Address1,
               Address2: row.Address2,
               City: row.City,
               State: row.State,
               Zip_Code: row.`Zip Code`,
               Contact_Name: row.`Contact Name`,
               Contact_Title: row.`Contact Title`,
               Contact_Phone: row.`Contact Phone`,
               Contact_Email: row.`Contact Email`
           })
           ''')
    
def create_project_node(tx):
    tx.run('''
            LOAD CSV WITH HEADERS FROM 'file:///project.csv' AS row
            CREATE (p:Project {
                id: toInteger(row.id),
                Award_Title: row.`Award Title`,
                Abstract: row.Abstract,
                PI_Name: row.`PI Name`,
                PI_Title: row.`PI Title`,
                PI_Phone: row.`PI Phone`,
                PI_Email: row.`PI Email`
            })
            ''')

def create_award_node(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///award.csv' AS row
        CREATE (a:Award {
            Award_Title: row.`Award Title`,
            Phase: row.Phase,
            Proposal_Award_Date: row.`Proposal Award Date`,
            Solicitation_Number: row.`Solicitation Number`,
            Solicitation_Year: row.`Solicitation Year`,
            Solicitation_Close_Date: row.`Solicitation Close_Date`,
            Award_Year: row.`Award Year`,
            Award_Amount: toInteger(row.`Award Amount`),
            id: toInteger(row.id)
           })
            ''')

def create_scheme_node(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///scheme.csv' AS row
        CREATE (s:Scheme {
            id: toInteger(row.id),
            Program: row.Program
        })
        ''')
    
def create_agency_node(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///agency.csv' AS row
        CREATE (a:Agency {
            id: toInteger(row.id),
            Agency: row.Agency,
            Branch: row.Branch
        })
        ''')
    
def create_research_institution_node(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///reasearch_institution.csv' AS row
        CREATE (ri:ResearchInstitution {
            id: toInteger(row.id),
            RI_Name: row.`RI Name`,
            RI_POC_Name: row.`RI POC Name`,
            RI_POC_Phone: row.`RI POC Phone`
        })
        ''')




    
def create_awarded_by_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///awarded_by.csv' AS row
        MATCH (a:Award {id: toInteger(row.Award_ID)}), (s:Scheme {id: toInteger(row.Program_ID)})
        MERGE (a)-[:AWARDED_BY]->(s)
        ''')

def create_awards_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///awards.csv' AS row
        MATCH (s:Scheme {id: toInteger(row.Program_ID)}), (a:Award {id: toInteger(row.Award_ID)})
        MERGE (s)-[:AWARDS]->(a)
        ''')

def create_beneficiary_of_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///beneficiary_of.csv' AS row
        MATCH (c:Company {id: toInteger(row.Company_ID)}), (a:Award {id: toInteger(row.Award_ID)})
        MERGE (c)-[:BENEFICIARY_OF]->(a)
        ''')

def create_finances_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///finances.csv' AS row
        MATCH (a:Award {id: toInteger(row.Award_ID)}), (p:Project {id: toInteger(row.Project_ID)})
        MERGE (a)-[:FINANCES]->(p)
        ''')

def create_funded_by_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///funded_by.csv' AS row
        MATCH (a:Agency {id: toInteger(row.Agency_ID)}), (aw:Award {id: toInteger(row.Award_ID)})
        MERGE (aw)-[:FUNDED_BY]->(a)
        ''')

def create_funds_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///funds.csv' AS row
        MATCH (a:Agency {id: toInteger(row.Agency_ID)}), (aw:Award {id: toInteger(row.Award_ID)})
        MERGE (a)-[:FUNDS]->(aw)
        ''')

def create_has_beneficiary_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///has_beneficiary.csv' AS row
        MATCH (a:Award {id: toInteger(row.Award_ID)}), (c:Company {id: toInteger(row.Company_ID)})
        MERGE (a)-[:HAS_BENEFICIARY]->(c)
        ''')

def create_has_participant_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///has_participant.csv' AS row
        MATCH (p:Project {id: toInteger(row.Project_ID)}), (c:Company {id: toInteger(row.Company_ID)})
        MERGE (p)-[:HAS_PARTICIPANT]->(c)
        ''')

def create_has_participant2_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///has_participant2.csv' AS row
        MATCH (p:Project {id: toInteger(row.Project_ID)}), (ri:ResearchInstitution {id: toInteger(row.RI_ID)})
        MERGE (p)-[:HAS_PARTICIPANT]->(ri)
        ''')

def create_implemented_by_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///implemented_by.csv' AS row
        MATCH (a:Agency {id: toInteger(row.Agency_ID)}), (s:Scheme {id: toInteger(row.Program_ID)})
        MERGE (s)-[:IMPLEMENTED_BY]->(a)
        ''')

def create_implements_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///implements.csv' AS row
        MATCH (ri:ResearchInstitution {id: toInteger(row.RI_ID)}), (c:Company {id: toInteger(row.Company_ID)})
        MERGE (ri)-[:IMPLEMENTS]->(c)
        ''')

def create_participated_in_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///participated_in.csv' AS row
        MATCH (c:Company {id: toInteger(row.Company_ID)}), (p:Project {id: toInteger(row.Project_ID)})
        MERGE (c)-[:PARTICIPATED_IN]->(p)
        ''')

def create_participated_in2_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///participated_in2.csv' AS row
        MATCH (ri:ResearchInstitution {id: toInteger(row.RI_ID)}), (p:Project {id: toInteger(row.Project_ID)})
        MERGE (ri)-[:PARTICIPATED_IN]->(p)
        ''')

def create_recipient_of_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///recipient_of.csv' AS row
        MATCH (p:Project {id: toInteger(row.Project_ID)}), (a:Award {id: toInteger(row.Award_ID)})
        MERGE (p)-[:RECIPIENT_OF]->(a)
        ''')

def create_partners_with_relationship(tx):
    tx.run('''
        LOAD CSV WITH HEADERS FROM 'file:///partners_with.csv' AS row
        MATCH (ri:ResearchInstitution {id: toInteger(row.RI_ID)}), (c:Company {id: toInteger(row.Company_ID)})
        MERGE (ri)<-[:PARTNERS_WITH]->(c)
        ''')
    
with driver.session(database=database) as session:
    # session.write_transaction(create_company_node)
    # session.write_transaction(create_project_node)
    # session.write_transaction(create_award_node)
    # session.write_transaction(create_scheme_node)
    # session.write_transaction(create_agency_node)
    # session.write_transaction(create_research_institution_node)


    # session.write_transaction(create_awarded_by_relationship)
    # session.write_transaction(create_awards_relationship)
    # session.write_transaction(create_beneficiary_of_relationship)
    # session.write_transaction(create_finances_relationship)
    # session.write_transaction(create_funded_by_relationship)
    # session.write_transaction(create_funds_relationship)
    # session.write_transaction(create_has_beneficiary_relationship)
    # session.write_transaction(create_has_participant_relationship)
    # session.write_transaction(create_has_participant2_relationship)
    # session.write_transaction(create_implemented_by_relationship)
    # session.write_transaction(create_implements_relationship)
    # session.write_transaction(create_participated_in_relationship)
    # session.write_transaction(create_participated_in2_relationship)
    # session.write_transaction(create_recipient_of_relationship)
    # session.write_transaction(create_partners_with_relationship)
    print("Done!")

driver.close()
