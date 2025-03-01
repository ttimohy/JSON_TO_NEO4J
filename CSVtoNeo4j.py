import csv

company_writer = csv.writer(open('nodes/company.csv','w',newline=''))
award_writer = csv.writer(open('nodes/award.csv','w',newline=''))
agency_writer = csv.writer(open('nodes/agency.csv','w',newline=''))
program_writer = csv.writer(open('nodes/program.csv','w',newline=''))
PI_writer = csv.writer(open('nodes/PI.csv','w',newline=''))
POC_writer = csv.writer(open('nodes/POC.csv','w',newline=''))
project_writer = csv.writer(open('nodes/project.csv','w',newline=''))

applies_to_writer = csv.writer(open('relationships/applies_to.csv','w',newline=''))
partners_with_writer = csv.writer(open('relationships/partners_with.csv','w',newline=''))
funds_writer = csv.writer(open('relationships/funds.csv', 'w', newline=''))
offers_writer = csv.writer(open('relationships/offers.csv', 'w', newline=''))
administered_by_writer = csv.writer(open('relationships/administered_by.csv', 'w', newline=''))
generates_writer = csv.writer(open('relationships/generates.csv', 'w', newline=''))
funded_by_writer = csv.writer(open('relationships/funded_by.csv', 'w', newline=''))
has_writer = csv.writer(open('relationships/has.csv', 'w', newline=''))
hosts_writer = csv.writer(open('relationships/hosts.csv', 'w', newline=''))
leads_writer = csv.writer(open('relationships/leads.csv', 'w', newline=''))
employed_by_writer = csv.writer(open('relationships/employed_by.csv', 'w', newline=''))
represents_writer = csv.writer(open('relationships/represents.csv', 'w', newline=''))

added_companies = []
num_companies = 0
def add_company(row):
    global num_companies
    global added_companies
    company_name = row[1]
    if company_name not in added_companies:
        newRow = [num_companies, company_name, *row[13:24]]
        company_writer.writerow(newRow)
        added_companies.append(company_name)
        num_companies += 1
        return num_companies - 1
    return added_companies.index(company_name)

num_awards = 0
def add_award(row):
    global num_awards
    newRow = [num_awards, row[2], *row[5:13], row[24]]
    award_writer.writerow(newRow)
    num_awards += 1
    return num_awards - 1

added_agencies = []
num_agencies = 0
def add_agency(row):
    global num_agencies
    global added_agencies
    agency_name = row[3]
    branch = row[4]
    if agency_name + branch not in added_agencies:
        newRow = [num_agencies, agency_name, branch]
        agency_writer.writerow(newRow)
        added_agencies.append(agency_name + branch)
        num_agencies += 1
        return num_agencies - 1
    return added_agencies.index(agency_name + branch)

added_programs = []
num_programs = 0
def add_program(row):
    global num_programs
    global added_programs
    program = row[6]
    phase = row[5]
    if program + phase not in added_programs:
        newRow = [num_programs, program, phase]
        program_writer.writerow(newRow)
        added_programs.append(program + phase)
        num_programs += 1
        return num_programs - 1
    return added_programs.index(program + phase)

added_POCs = []
num_POC = 0
def add_POC(row):
    global num_POC
    global added_POCs
    POC_name = row[26]
    if POC_name = '':
        return -1
    POC_number = row[28]
    if POC_name+POC_number not in added_POCs:
        newRow = [num_POC, POC_name, POC_number, row[27], row[29]]
        POC_writer.writerow(newRow)
        added_POCs.append(POC_name+POC_number)
        num_POC += 1
        return num_POC - 1
    return added_POCs.index(POC_name+POC_number)

added_PIs = []
num_PI = 0
def add_PI(row):
    global num_PI
    global added_PIs
    PI_name = row[30]
    PI_phone = row[32]
    if PI_name+PI_phone not in added_PIs:
        newRow = [num_PI, PI_name, PI_phone, row[31], row[34]]
        PI_writer.writerow(newRow)
        added_PIs.append(PI_name+PI_phone)
        num_PI += 1
        return num_PI - 1
    return added_PIs.index(PI_name+PI_phone)

added_RIs = []
num_RI = 0
def add_RI(row):
    global num_RI
    global added_RIs
    RI_name = row[34]
    if RI_name == '':
        return -1
    RI_contact_name = row[35]
    RI_contact_phone = row[36]
    if RI_contact_name == '':
        if RI_name not in added_RIs:
            newRow = [num_RI, RI_name]
            research_institution_writer.writerow(newRow)
            added_RIs.append(RI_name)
            num_RI += 1
            return num_RI - 1
        return added_RI.index(RI_name)
    else if RI_name+RI_contact_name+RI_contact_phone not in added_RI_contacts:
        newRow = [num_RI, RI_name, RI_contact_name, RI_contact_phone]
        RI_contact_writer.writerow(newRow)
        added_RIs.append(RI_name+RI_contact_name+RI_contact_phone)
        num_RI += 1
        return num_RI - 1
    return added_RI.index(RI_name+RI_contact_name+RI_contact_phone)

added_projects = []
num_project = 0
def add_project(row):
    global num_project
    global added_projects
    award_title = row[2]
    if award_title = '':
        return -1
    abstract = row[25]
    if abstract = 'N/A':
        return -1
    research_area_keywords = row[24]
    if award_title not in added_projects:
        newRow = [num_project, award_title, abstract, research_area_keywords]
        project_writer.writerow(newRow)
        added_projects.append(award_title)
        num_project += 1
        return num_project - 1
    return addded_projects.index(award_title)

def addRelationships(companyID, awardID, agencyID, programID, pocID, piID, riID, projectID):
    applies_to_writer.writerow([companyID, agencyID])
    if riID != -1:
        partners_with_writer.writerow([companyID, riID])
        conducts_writer.writerow([riID, projectID])
    granted_to_writer.writerow([awardID, companyID])
    funds_writer.writerow([awardID, projectID])
    offers_writer.writerow([agencyID, programID])
    administered_by_writer.writerow([programID, agencyID])
    generates_writer.writerow([programID, awardID])
    funded_by_writer.writerow([projectID, awardID])
    if projectID != -1:
        if piID != -1:
            has_writer.writerow([projectID, piID])
        if pocID != -1:
            has_writer.writerow([projectID, pocID])
        hosts_writer.writerow([projectID, companyID])
    if piID != -1:
        if projectID != -1:
            leads_writer.writerow([piID, projectID])
        employed_by_writer.writerow([piID, companyID])
    if pocID != -1:
        represents_writer.writerow([pocID, companyID])

if __name__ == "__main__":
    reader = csv.reader(open('data/SBIR_awards_cleaned.csv', 'r'))
    header = reader.__next__()
    for i in range(100):
        row = reader.__next__()
        companyID = add_company(row)
        awardID = add_award(row)
        agencyID = add_agency(row)
        programID = add_program(row)
        pocID = add_POC(row)
        piID = add_PI(row)
        projectID = add_project(row)
        addRelationships(companyID, awardID, agencyID, programID, pocID, piID, riID, projectID)

