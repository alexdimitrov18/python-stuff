import json
import random

# Define the companies, employees, and couriers
companies = {1: 'DHL', 2: 'Discordia', 5: 'Express', 4: 'komp', 3: 'Speedy'}
employees = {1: 1, 2: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 2, 22: 2, 23: 2, 24: 2, 25: 2, 26: 3, 27: 3, 28: 3, 29: 3, 30: 4, 31: 4, 32: 4, 33: 4, 34: 4, 35: 4, 36: 5, 37: 5, 38: 5, 39: 5, 40: 5, 41: 5, 42: 5, 43: 3, 44: 3, 45: 4, 46: 4, 47: 5, 48: 5, 49: 1, 50: 1}
couriers = [[2, 1], [43, 5], [44, 5], [45, 4], [46, 4], [47, 2], [48, 2], [49, 1], [50, 1]]

# User information table
user_info = {
    1: ['alex', 1, '123456789'],
    18: ['DPS', 1, '1234567689'],
    20: ['Tony', 1, '1234567689'],
    16: ['pepi', 1, '1234567689'],
    17: ['godzi', 1, '1234567689'],
    15: ['kasier', 1, '1234567689'],
    19: ['Lili', 1, '1234567689'],
    23: ['Krasi', 2, '1234567689'],
    22: ['Bobby', 2, '1234567689'],
    25: ['Nena', 2, '1234567689'],
    24: ['Gosho', 2, '1234567689'],
    21: ['Toncho', 2, '1234567689'],
    29: ['user789', 3, '1234567890'],
    28: ['user456', 3, 'securepass789'],
    26: ['Rusen', 3, '1234567689'],
    27: ['user123', 3, 'password123'],
    30: ['user101', 4, 'pass123456'],
    32: ['user103', 4, 'mypass123'],
    33: ['user104', 4, 'nikpass123'],
    31: ['user102', 4, '987654321'],
    34: ['user105', 4, 'svet123456'],
    35: ['user106', 4, 'dragopass123'],
    40: ['user111', 5, 'asenpass123'],
    41: ['user112', 5, 'vazrazhdanepass123'],
    39: ['user110', 5, 'dimitpass123'],
    38: ['user109', 5, 'boykopass123'],
    42: ['user113', 5, 'svetlapass123'],
    36: ['user107', 5, 'elenapass123'],
    37: ['user108', 5, 'vasilpass123']
}

# Filter employees and couriers by company
def filter_by_company(company_id):
    return [e for e, c in employees.items() if c == company_id], [c for c, _ in couriers if _ == company_id]

# Generate JSON data
def generate_json(departureAddress, arrivalAddress, weight, senderId, receiverId, sentDate, companyId):
    employee_list, courier_list = filter_by_company(companyId)
    if not employee_list or not courier_list:
        return None
    generated_json = json.dumps({
        "departureAddress": departureAddress,
        "arrivalAddress": arrivalAddress,
        "weight": weight,
        "senderId": senderId,
        "receiverId": receiverId,
        "employeeId": random.choice(employee_list),
        "sentDate": sentDate,
        "courierId": random.choice(courier_list),
        "companyId": companyId
    }, indent=4)
    user_id = random.choice(list(user_info.keys()))
    username, _, password = user_info[user_id]
    info = f"\nUser Info: (id: {user_id}, username: {username}, company_id: {companyId}, password: {password})"
    return generated_json + info

# Generate the first example for DHL employees
print(generate_json("XXXXX", "YYYY", 100, 37, 35, "2024-03-01T19:17:51", 1))

# Generate the next 4 examples randomly
for _ in range(4):
    print(generate_json("XXXXX", "YYYY", 100, 37, 35, "2024-03-01T19:17:51", random.choice(list(companies.keys()))))
