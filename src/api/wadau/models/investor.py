class Investor:
  def __init__(self, 
    firstname
    , lastname
    , middlename
    , email
    , phone_number
    , dob
    , kra_pin
    , national_id
    , country
    , county
    , city
    , loans
    , investments
    , statetments

  ):
    self.firstname = firstname if firstname !=None else ''
    self.lastname = lastname if lastname !=None else ''
    self.middlename = middlename if middlename !=None else ''
    self.dob = dob if dob !=None else ''
    self.kra_pin = kra_pin if kra_pin !=None else ''
    self.email = email if email !=None else ''
    self.phone_number = phone_number if phone_number !=None else ''
    self.country = country if country !=None else ''
    self.county = county if county !=None else ''
    self.city = city if city !=None else ''
    self.loans = loans if loans !=None else ''
    self.investments = investments if investments !=None else ''
    self.statements = statetments if statetments !=None else ''

def info(self):
    return self.firstname + ' ' + self.lastname

def portfolio(self):
    print("total assets count: 1")
    return 100000

