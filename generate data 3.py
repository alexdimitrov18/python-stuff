import json
import random

# Define the companies, employees, couriers, and user details
companies = {1: 'DHL', 2: 'Discordia', 5: 'Express', 4: 'komp', 3: 'Speedy'}
employees = {1: 1, 2: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 2, 22: 2, 23: 2, 24: 2, 25: 2, 26: 3, 27: 3, 28: 3, 29: 3, 30: 4, 31: 4, 32: 4, 33: 4, 34: 4, 35: 4, 36: 5, 37: 5, 38: 5, 39: 5, 40: 5, 41: 5, 42: 5, 43: 3, 44: 3, 45: 4, 46: 4, 47: 5, 48: 5, 49: 1, 50: 1}
couriers = [[2, 1], [43, 5], [44, 5], [45, 4], [46, 4], [47, 2], [48, 2], [49, 1], [50, 1]]
user_details = {1: ['alex', '123456789'], 2: ['ivo', '123456789'], 4: ['pesho', '1234567689'], 5: ['ivancho', '1234567890'], 6: ['mincho', '1234567890'], 7: ['nasko', '1234567890'], 8: ['milen', '1234567890'], 9: ['tuhlen@abv.bg', '1234567890'], 10: ['krasko@abv.bg', '1234567890'], 11: ['spas@abv.bg', '1234567890'], 12: ['destroyer12@abv.bg', '1234567890'], 13: ['creator000@abv.bg', '1234567890'], 14: ['vinland_saga@abv.bg', '1234567890'], 15: ['kasier', '1234567689'], 16: ['pepi', '1234567689'], 17: ['godzi', '1234567689'], 18: ['DPS', '1234567689'], 19: ['Lili', '1234567689'], 20: ['Tony', '1234567689'], 21: ['Toncho', '1234567689'], 22: ['Bobby', '1234567689'], 23: ['Krasi', '1234567689'], 24: ['Gosho', '1234567689'], 25: ['Nena', '1234567689'], 26: ['Rusen', '1234567689'], 27: ['user123', 'password123'], 28: ['user456', 'securepass789'], 29: ['user789', '1234567890'], 30: ['user101', 'pass123456'], 31: ['user102', '987654321'], 32: ['user103', 'mypass123'], 33: ['user104', 'nikpass123'], 34: ['user105', 'svet123456'], 35: ['user106', 'dragopass123'], 36: ['user107', 'elenapass123'], 37: ['user108', 'vasilpass123'], 38: ['user109', 'boykopass123'], 39: ['user110', 'dimitpass123'], 40: ['user111', 'asenpass123'], 41: ['user112', 'vazrazhdanepass123'], 42: ['user113', 'svetlapass123'], 43: ['user114', 'annapass123'], 44: ['user115', 'johnpass123'], 45: ['user116', 'emmapass123'], 46: ['user117', 'danielpass123'], 47: ['user118', 'oliviapass123'], 48: ['user119', 'williampass123'], 49: ['user120', 'sophiapass123'], 50: ['user121', 'jamespass123']}

# Filter employees and couriers by company
def filter_by_company(company_id):
    return [e for e, c in employees.items() if c == company_id], [c for c, _ in couriers if _ == company_id]

# Generate JSON data
def generate_json(departureAddress, arrivalAddress, weight, senderId, receiverId, sentDate, companyId):
    employee_list, courier_list = filter_by_company(companyId)
    if not employee_list or not courier_list:
        return None
    employeeId = random.choice(employee_list)
    return json.dumps({
        "departureAddress": departureAddress,
        "arrivalAddress": arrivalAddress,
        "weight": weight,
        "senderId": senderId,
        "receiverId": receiverId,
        "employeeId": employeeId,
        "sentDate": sentDate,
        "courierId": random.choice(courier_list),
        "companyId": companyId
    }, indent=4), (employeeId, *user_details[employeeId])

# Generate the first example for DHL employees
json_data, vector = generate_json("XXXXX", "YYYY", 100, 37, 35, "2024-03-01T19:17:51", 1)
print(json_data)
print(vector)

# Generate the next 4 examples randomly
for _ in range(4):
    json_data, vector = generate_json("XXXXX", "YYYY", 100, 37, 35, "2024-03-01T19:17:51", random.choice(list(companies.keys())))
    print(json_data)
    print(vector)
