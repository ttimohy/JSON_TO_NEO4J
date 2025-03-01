import csv

company_writer = csv.writer(open('nodes/company.csv','w',newline=''))
award_writer = csv.writer(open('nodes/award.csv','w',newline=''))
agency_writer = csv.writer(open('nodes/agency.csv','w',newline=''))
PI_writer = csv.writer(open('nodes/PI.csv','w',newline=''))
POC_writer = csv.writer(open('nodes/POC.csv','w',newline=''))
research_institution_writer = csv.writer(open('nodes/research_institution.csv','w',newline=''))

contact_for_writer = csv.writer(open('relationships/contact_for.csv','w',newline=''))
contact_for_RI_writer = csv.writer(open('relationships/contact_for_RI.csv','w',newline=''))
funded_writer = csv.writer(open('relationships/funded.csv','w',newline=''))
leads_writer = csv.writer(open('relationships/leads.csv','w',newline=''))
recieved_award_writer = csv.writer(open('relationships/recieved_award.csv','w',newline=''))
research_institution_for_writer = csv.writer(open('relationships/research_institution_for.csv','w',newline=''))

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

added_POCs = []
num_POC = 0
def add_POC(row):
    global num_POC
    global added_POCs
    POC_name = row[25]
    POC_number = row[27]
    if POC_name+POC_number not in added_POCs:
        newRow = [num_POC, POC_name, *row[26:29]]
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
    PI_name = row[29]
    PI_phone = row[31]
    if PI_name+PI_phone not in added_PIs:
        newRow = [num_PI, PI_name, *row[30:33]]
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
    RI_name = row[33]
    if RI_name == '':
        return -1
    RI_contact_name = row[34]
    RI_contact_phone = row[35]
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
        added_RI_contacts.append(RI_name+RI_contact_name+RI_contact_phone)
        num_RI += 1
        return num_RI - 1
    return added_RI.index(RI_name+RI_contact_name+RI_contact_phone)

def addRelationships(companyID, awardID, agencyID, pocID, piID, riID, ripocID):
    funded_writer.writerow([agencyID, awardID])
    leads_writer.writerow([piID, awardID])
    recieved_award_writer.writerow([companyID, awardID])
    contact_for_writer.writerow([pocID, companyID])
    if riID != -1:
        research_institution_for_writer.writerow([riID, companyID])
    if ripocID != -1:
        contact_for_RI_writer.writerow([ripocID, riID])


if __name__ == "__main__":
    reader = csv.reader(open('data/SBIR_awards_cleaned.csv', 'r'))
    header = reader.__next__()
    for i in range(100):
        row = reader.__next__()
        companyID = add_company(row)
        awardID = add_award(row)
        agencyID = add_agency(row)
        pocID = add_POC(row)
        piID = add_PI(row)
        riID = add_RI(row)
        ripocID = add_RI_contact(row)
        addRelationships(companyID, awardID, agencyID, pocID, piID, riID, ripocID)

