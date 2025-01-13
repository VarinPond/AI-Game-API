import requests

# Define the API URL
API_URL = "http://127.0.0.1:8000/chat/"

# Define the payload
payload = {
    "assignment": """ 
                        กำหนดให้โลกใบหนึ่งที่ไร้ซึ่งอารยธรรมมีแต่ป่าไม้ แม่น้ำ ภูเขา สัตว์ป่า และมอนสเตอร์ 
                        มีชายคนหนึ่งต้องการที่จะรวบรวมประชากรมนุษย์ที่กระจัดกระจายอยู่ทั่วแผ่นดินมาเพื่อสร้างอารยธรรมขึ้นมาใหม่
                        โดยจะให้เรามีค่า stat:
                        ดังนี้ Leadership = 20/100, Wisdom = 5/100, Compassion = 5/100, Valor = 5/100, Strength = 5/100 
                        โดยมี HP = 20/100, Attack = 10 หน่วยต่อตา

                        ตอนนี้มีศัตรูอยู่ตรงหน้าเป็นบอส โดยบอสมี stat:
                        Hp = 1000, Attack = 100
                """,
    "question": """
                    เราจะทำยังไง
                    1. ตีบอสด้วย Attack = 10 หน่วยต่อตา
                    2. หนี

                    เลือกมา 1 ช้อยและบอกเหตุผล
                """
}

# Make a POST request to the API
response = requests.post(API_URL, json=payload)

print(response.json())